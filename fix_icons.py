import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_icons(text):
    t = text
    # Trust Strip
    t = t.replace('solar:medal-ribbon-bold-duotone', 'lucide:award')
    t = t.replace('solar:diploma-bold-duotone', 'lucide:shield-check')
    t = t.replace('solar:heart-pulse-bold-duotone', 'lucide:heart-handshake')
    t = t.replace('solar:star-bold-duotone', 'lucide:star')
    
    # Services
    t = t.replace('solar:syringe-bold-duotone', 'lucide:syringe')
    t = t.replace('solar:magic-stick-3-bold-duotone', 'lucide:sparkles')
    t = t.replace('solar:stars-bold-duotone', 'lucide:flower-2')
    t = t.replace('solar:accessibility-bold-duotone', 'lucide:person-standing')
    
    return t

content = replace_icons(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = replace_icons(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons replaced with lucide successfully!")
