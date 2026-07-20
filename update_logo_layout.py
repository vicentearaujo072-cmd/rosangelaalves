import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_logo_html = """<a href="#" class="flex flex-col items-center justify-center group">
    <img src="assets/logo-ra.svg" alt="Rosangela Alves Logo" class="h-14 w-auto object-contain mb-1 group-hover:scale-105 transition-transform duration-300" />
    <div class="text-lg font-bold tracking-widest text-stone-900 uppercase leading-none">
        ROSANGELA <span class="text-[#D75C37]">ALVES</span>
    </div>
    <div class="text-[0.45rem] font-light tracking-[0.3em] text-stone-500 mt-1 uppercase">ESTÉTICA AVANÇADA</div>
</a>"""

new_logo_html = """<a href="#" class="flex items-center gap-3 group">
    <img src="assets/logo-ra.svg" alt="Rosangela Alves Logo" class="h-10 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform duration-300 shrink-0" />
    <div class="flex flex-col justify-center">
        <div class="text-base sm:text-xl font-bold tracking-widest text-stone-900 uppercase leading-none">
            ROSANGELA <span class="text-[#D75C37]">ALVES</span>
        </div>
        <div class="text-[0.45rem] sm:text-[0.55rem] font-light tracking-[0.25em] sm:tracking-[0.3em] text-stone-500 mt-1 uppercase">ESTÉTICA AVANÇADA</div>
    </div>
</a>"""

def update_logo_layout(text):
    t = text
    if old_logo_html in t:
        t = t.replace(old_logo_html, new_logo_html)
    return t

def update_logo_layout_escaped(text):
    t = text
    old_escaped = old_logo_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    new_escaped = new_logo_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    if old_escaped in t:
        t = t.replace(old_escaped, new_escaped)
    return t

content = update_logo_layout(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = update_logo_layout_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Logo layout updated successfully!")
