import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def upgrade_icons(text):
    t = text
    
    # 1. Upgrade Trust Strip
    # Add 'group' class to the wrappers
    t = re.sub(
        r'<div class="flex items-center gap-3">(\s*<div class="w-10 h-10 rounded-full bg-\[#4A5441\]/20 flex items-center justify-center text-\[#E06138\]">)',
        r'<div class="flex items-center gap-3 group">\1',
        t
    )
    # Replace the circle container and icon
    t = re.sub(
        r'<div class="w-10 h-10 rounded-full bg-\[#4A5441\]/20 flex items-center justify-center text-\[#E06138\]">\s*<iconify-icon icon="solar:([^"]+)-linear" width="24"></iconify-icon>\s*</div>',
        r'<div class="w-12 h-12 rounded-full bg-[#4A5441]/10 flex items-center justify-center text-[#D75C37] group-hover:bg-[#D75C37] group-hover:text-white transition-all duration-300 group-hover:-translate-y-1 shadow-sm">\n<iconify-icon icon="solar:\1-bold-duotone" width="26"></iconify-icon>\n</div>',
        t
    )
    # Force 5.0 estrelas to use stars-bold-duotone instead of minimalistic
    t = t.replace('solar:stars-minimalistic-bold-duotone', 'solar:star-bold-duotone')
    
    # 2. Upgrade Services Cards
    # Injetáveis
    t = re.sub(
        r'<div class="w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform">\s*<iconify-icon icon="solar:syringe-linear" width="24"></iconify-icon>\s*</div>',
        r'<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg">\n<iconify-icon icon="solar:syringe-bold-duotone" width="28"></iconify-icon>\n</div>',
        t
    )
    # Rejuvenescimento Facial
    t = re.sub(
        r'<div class="w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform">\s*<iconify-icon icon="solar:face-scan-circle-linear" width="24"></iconify-icon>\s*</div>',
        r'<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg">\n<iconify-icon icon="solar:magic-stick-3-bold-duotone" width="28"></iconify-icon>\n</div>',
        t
    )
    # Tratamentos de Pele
    t = re.sub(
        r'<div class="w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform">\s*<iconify-icon icon="solar:bolt-linear" width="24"></iconify-icon>\s*</div>',
        r'<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg">\n<iconify-icon icon="solar:stars-bold-duotone" width="28"></iconify-icon>\n</div>',
        t
    )
    # Bem-Estar Corporal
    t = re.sub(
        r'<div class="w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform">\s*<iconify-icon icon="solar:body-linear" width="24"></iconify-icon>\s*</div>',
        r'<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg">\n<iconify-icon icon="solar:accessibility-bold-duotone" width="28"></iconify-icon>\n</div>',
        t
    )
    
    # 3. Small fix in text (e.g., Injetáveis Estéticos missing accents due to ASCII)
    t = t.replace('Injetǭveis EstǸticos', 'Injetáveis Estéticos')
    t = t.replace('Tratamentos de Pele', 'Tratamentos de Pele')

    return t

def upgrade_icons_escaped(text):
    t = text
    t = re.sub(
        r'<div class=\\"flex items-center gap-3\\">(\s*<div class=\\"w-10 h-10 rounded-full bg-\[#4A5441\]/20 flex items-center justify-center text-\[#E06138\]\\">)',
        r'<div class=\"flex items-center gap-3 group\">\1',
        t
    )
    
    t = re.sub(
        r'<div class=\\"w-10 h-10 rounded-full bg-\[#4A5441\]/20 flex items-center justify-center text-\[#E06138\]\\">\s*<iconify-icon icon=\\"solar:([^"]+)-linear\\" width=\\"24\\"></iconify-icon>\s*</div>',
        r'<div class=\"w-12 h-12 rounded-full bg-[#4A5441]/10 flex items-center justify-center text-[#D75C37] group-hover:bg-[#D75C37] group-hover:text-white transition-all duration-300 group-hover:-translate-y-1 shadow-sm\">\\n<iconify-icon icon=\"solar:\1-bold-duotone\" width=\"26\"></iconify-icon>\\n</div>',
        t
    )
    t = t.replace('solar:stars-minimalistic-bold-duotone', 'solar:star-bold-duotone')
    
    t = re.sub(
        r'<div class=\\"w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform\\">\s*<iconify-icon icon=\\"solar:syringe-linear\\" width=\\"24\\"></iconify-icon>\s*</div>',
        r'<div class=\"w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg\">\\n<iconify-icon icon=\"solar:syringe-bold-duotone\" width=\"28\"></iconify-icon>\\n</div>',
        t
    )
    t = re.sub(
        r'<div class=\\"w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform\\">\s*<iconify-icon icon=\\"solar:face-scan-circle-linear\\" width=\\"24\\"></iconify-icon>\s*</div>',
        r'<div class=\"w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg\">\\n<iconify-icon icon=\"solar:magic-stick-3-bold-duotone\" width=\"28\"></iconify-icon>\\n</div>',
        t
    )
    t = re.sub(
        r'<div class=\\"w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform\\">\s*<iconify-icon icon=\\"solar:bolt-linear\\" width=\\"24\\"></iconify-icon>\s*</div>',
        r'<div class=\"w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg\">\\n<iconify-icon icon=\"solar:stars-bold-duotone\" width=\"28\"></iconify-icon>\\n</div>',
        t
    )
    t = re.sub(
        r'<div class=\\"w-12 h-12 bg-\[#D1DDE8\]/50 rounded-xl flex items-center justify-center text-stone-700 mb-6 group-hover:scale-110 transition-transform\\">\s*<iconify-icon icon=\\"solar:body-linear\\" width=\\"24\\"></iconify-icon>\s*</div>',
        r'<div class=\"w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white group-hover:-translate-y-2 group-hover:rotate-6 transition-all duration-300 shadow-sm group-hover:shadow-lg\">\\n<iconify-icon icon=\"solar:accessibility-bold-duotone\" width=\"28\"></iconify-icon>\\n</div>',
        t
    )
    
    t = t.replace('Injetǭveis EstǸticos', 'Injetáveis Estéticos')
    t = t.replace('Tratamentos de Pele', 'Tratamentos de Pele')

    return t

content = upgrade_icons(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = upgrade_icons_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons upgraded successfully!")
