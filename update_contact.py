import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Location Block Replacement
old_location_pattern = r'<div class="mb-8" id="locations">.*?<a class="text-xs font-bold text-stone-900 underline hover:text-\[#E06138\]" href="https://maps\.google\.com/\?q=[^"]+" target="_blank">Como Chegar</a>\s*</div>'

new_location_html = """<div class="mb-8" id="locations">
<h4 class="text-sm font-bold uppercase tracking-wide text-[#2C2C2C] mb-3 flex items-center gap-2">
<iconify-icon class="text-[#D75C37]" icon="solar:map-point-bold"></iconify-icon> Nossa Clínica
</h4>
<address class="not-italic text-sm text-stone-600 space-y-1 mb-4">
    Endereço da Clínica (A definir)<br/>
    Sua Cidade - UF
</address>
<div class="w-full h-48 rounded-xl overflow-hidden shadow-sm border border-stone-200">
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.197410143521!2d-46.661937!3d-23.56133!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjPCsDMzJzQwLjgiUyA0NsKwMzknNDMuMCJX!5e0!3m2!1spt-BR!2sbr!4v1620000000000!5m2!1spt-BR!2sbr" 
        width="100%" 
        height="100%" 
        style="border:0;" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
</div>
</div>"""

# 2. Instagram/Facebook Update
old_social_pattern = r'<a class="w-10 h-10 rounded-full bg-stone-700 hover:bg-\[#4A5441\] text-white flex items-center justify-center transition-colors" href="https://www\.instagram\.com/cloud_la_medspa/" target="_blank">\s*<iconify-icon icon="mdi:instagram" width="20"></iconify-icon>\s*</a>\s*<a class="w-10 h-10 rounded-full bg-stone-700 hover:bg-\[#4A5441\] text-white flex items-center justify-center transition-colors" href="https://www\.facebook\.com/cloudlamedspa" target="_blank">\s*<iconify-icon icon="mdi:facebook" width="20"></iconify-icon>\s*</a>'

new_social_html = """<a class="w-10 h-10 rounded-full bg-stone-700 hover:bg-[#D75C37] text-white flex items-center justify-center transition-colors" href="https://www.instagram.com/drarobiomedica/" target="_blank">
<iconify-icon icon="mdi:instagram" width="20"></iconify-icon>
</a>"""


def apply_changes(text):
    t = text
    t = re.sub(old_location_pattern, new_location_html, t, flags=re.DOTALL)
    t = re.sub(old_social_pattern, new_social_html, t, flags=re.DOTALL)
    return t

def apply_changes_escaped(text):
    t = text
    
    # We must match the escaped versions
    # For location
    old_loc_esc = r'<div class=\\"mb-8\\" id=\\"locations\\">.*?<a class=\\"text-xs font-bold text-stone-900 underline hover:text-\[#E06138\]\\" href=\\"https://maps\.google\.com/\?q=[^"]+\\" target=\\"_blank\\">Como Chegar</a>\s*</div>'
    new_loc_esc = new_location_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    t = re.sub(old_loc_esc, new_loc_esc, t, flags=re.DOTALL)
    
    # For socials
    old_soc_esc = r'<a class=\\"w-10 h-10 rounded-full bg-stone-700 hover:bg-\[#4A5441\] text-white flex items-center justify-center transition-colors\\" href=\\"https://www\.instagram\.com/cloud_la_medspa/\\" target=\\"_blank\\">\s*<iconify-icon icon=\\"mdi:instagram\\" width=\\"20\\"></iconify-icon>\s*</a>\s*<a class=\\"w-10 h-10 rounded-full bg-stone-700 hover:bg-\[#4A5441\] text-white flex items-center justify-center transition-colors\\" href=\\"https://www\.facebook\.com/cloudlamedspa\\" target=\\"_blank\\">\s*<iconify-icon icon=\\"mdi:facebook\\" width=\\"20\\"></iconify-icon>\s*</a>'
    new_soc_esc = new_social_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    t = re.sub(old_soc_esc, new_soc_esc, t, flags=re.DOTALL)
    
    return t

content = apply_changes(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = apply_changes_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Contact info and map updated successfully!")
