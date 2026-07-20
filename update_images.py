import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'assets/antes e depois 1.jpeg': 'assets/new_antes_depois_1.png',
    'assets/antes e depois 2.jpeg': 'assets/new_antes_depois_2.png',
    'assets/antes e depois 3.jpeg': 'assets/new_antes_depois_3.png',
    'assets/antes e depois 4.jpeg': 'assets/new_antes_depois_4.png',
    'assets/antes e depois 5.jpeg': 'assets/new_antes_depois_5.png',
    'assets/antes e depois 6.jpeg': 'assets/new_antes_depois_6.png',
    'assets/dona da empresa.jpeg': 'assets/dona da empresa.jpeg',
}

def replace_in_text(text):
    t = text
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

# 1. First, replace the raw HTML part
content = replace_in_text(content)

# 2. Next, find the base64 JSON payload and modify it
match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = replace_in_text(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images updated successfully!")
