import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def unify_colors(text):
    t = text
    # Standardize Terracotta
    t = re.sub(r'(?i)#E3C15E', '#D75C37', t) # Gold -> Terracotta
    t = re.sub(r'(?i)#d4b04c', '#D75C37', t) # Dark Gold -> Terracotta
    t = re.sub(r'(?i)#E06138', '#D75C37', t) # Orange-ish Terracotta -> Unified Terracotta
    
    # Standardize Light Beige/Cream instead of Blue-gray
    t = re.sub(r'(?i)#D1DDE8', '#EAE4D9', t) # Blue-gray -> Warm Beige
    return t

content = unify_colors(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = unify_colors(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors unified successfully!")
