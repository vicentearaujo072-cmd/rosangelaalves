import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def update_hero(text):
    t = text
    # 1. Update the image
    old_img = r'<img alt="Rosangela Alves Patient Results" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700" src="assets/bd2f87eb119d22c3_11062b_ed81470d7bb5405ea00aad7.jpg"/>'
    new_img = '<img alt="Rosangela Alves Hero" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700" src="assets/hero_clinic.png"/>'
    
    # 2. Update the Hero Title
    # <h1 class="text-4xl sm:text-5xl lg:text-7xl font-medium text-stone-900 leading-[1.1] tracking-tight">Clínica Estética <br/> <span class="italic text-stone-500">Ultimate Med Spa</span></h1>
    old_h1_pattern = r'<h1 class="([^"]*)">[^<]*<br/>\s*<span class="([^"]*)">Ultimate Med Spa</span></h1>'
    
    t = t.replace(old_img, new_img)
    t = re.sub(
        old_h1_pattern,
        r'<h1 class="\1">Rosangela Alves <br/> <span class="\2">Estética Avançada</span></h1>',
        t
    )
    
    return t

def update_hero_escaped(text):
    t = text
    old_img_esc = r'<img alt=\\"Rosangela Alves Patient Results\\" class=\\"w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700\\" src=\\"assets/bd2f87eb119d22c3_11062b_ed81470d7bb5405ea00aad7.jpg\\"/>'
    new_img_esc = '<img alt=\\"Rosangela Alves Hero\\" class=\\"w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700\\" src=\\"assets/hero_clinic.png\\"/>'
    
    old_h1_pattern_esc = r'<h1 class=\\"([^"]*)\\">[^<]*<br/>\s*<span class=\\"([^"]*)\\">Ultimate Med Spa</span></h1>'
    
    t = t.replace(old_img_esc, new_img_esc)
    t = re.sub(
        old_h1_pattern_esc,
        r'<h1 class=\"\1\">Rosangela Alves <br/> <span class=\"\2\">Estética Avançada</span></h1>',
        t
    )
    return t

content = update_hero(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = update_hero_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero updated successfully!")
