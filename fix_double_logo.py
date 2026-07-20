import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_logo_html = """<a href="#" class="flex items-center gap-3 group">
    <img src="assets/logo-ra.svg" alt="Rosangela Alves Logo" class="h-10 sm:h-12 w-auto object-contain group-hover:scale-105 transition-transform duration-300 shrink-0" />
    <div class="flex flex-col justify-center">
        <div class="text-base sm:text-xl font-bold tracking-widest text-stone-900 uppercase leading-none">
            ROSANGELA <span class="text-[#D75C37]">ALVES</span>
        </div>
        <div class="text-[0.45rem] sm:text-[0.55rem] font-light tracking-[0.25em] sm:tracking-[0.3em] text-stone-500 mt-1 uppercase">ESTÉTICA AVANÇADA</div>
    </div>
</a>"""

def fix_header_logo(text):
    t = text
    # Regex to match the malformed double anchor and the trailing div
    # <a class="flex items-center gap-3 group" href="#">
    # <a href="#" class="flex items-center gap-3 group">
    # ...
    # </a>
    # <div class="hidden md:block">...</div>
    # </a>
    
    # We can match it generally:
    # r'<a[^>]*class="flex items-center gap-3 group"[^>]*>\s*<a href="#" class="flex items-center gap-3 group">.*?</a>\s*<div class="hidden md:block">.*?</div>\s*</a>'
    
    pattern = r'<a[^>]*class="flex items-center gap-3 group"[^>]*>\s*<a href="#" class="flex items-center gap-3 group">.*?</a>\s*<div class="hidden md:block">.*?</div>\s*</a>'
    
    # Replace it with just the new logo html
    t = re.sub(pattern, new_logo_html, t, flags=re.DOTALL)
    return t

def fix_header_logo_escaped(text):
    t = text
    new_logo_escaped = new_logo_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    
    # Same pattern but taking escaping into account
    pattern = r'<a[^>]*class=\\"flex items-center gap-3 group\\"[^>]*>\s*<a href=\\"#\\" class=\\"flex items-center gap-3 group\\">.*?</a>\s*<div class=\\"hidden md:block\\">.*?</div>\s*</a>'
    
    t = re.sub(pattern, new_logo_escaped, t, flags=re.DOTALL)
    return t


content = fix_header_logo(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = fix_header_logo_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Double logo fixed successfully!")
