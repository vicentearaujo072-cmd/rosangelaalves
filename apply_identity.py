import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def apply_new_identity(text):
    t = text
    
    # 1. Colors
    # Backgrounds (Buttons, icons bg)
    t = t.replace('bg-[#E3C15E]', 'bg-[#4A5441]')
    # Text (Highlights, subheadings)
    t = t.replace('text-[#E3C15E]', 'text-[#E06138]')
    # Borders
    t = t.replace('border-[#E3C15E]', 'border-[#4A5441]')
    # Hovers
    t = t.replace('hover:bg-[#d4b04c]', 'hover:bg-[#384031]')
    t = t.replace('hover:text-[#d4b04c]', 'hover:text-[#C5502A]')
    
    # 2. Text Replacements
    # In running text
    t = t.replace('Clínica Estética Rosangela |', 'Rosangela Alves |')
    t = t.replace('Na Clínica Estética Rosangela', 'Na Rosangela Alves Estética Avançada')
    t = t.replace('com a Clínica Estética Rosangela', 'com Rosangela Alves')
    t = t.replace('com a Clínica Rosangela', 'com Rosangela Alves')
    t = t.replace('CLÍNICA ROSANGELA', 'ROSANGELA ALVES')
    t = t.replace('© 2026 Clínica Estética Rosangela', '© 2026 Rosangela Alves')
    
    # Replace the plain text logo in navbar and footer
    t = re.sub(
        r'>Clínica Estética Rosangela</a>',
        r'>ROSANGELA <span class="text-[#E06138]">ALVES</span><br><span class="text-[0.4em] font-light tracking-[0.3em] text-stone-500 block -mt-1">ESTÉTICA AVANÇADA</span></a>',
        t
    )
    
    t = re.sub(
        r'>Clínica Estética Rosangela</span>',
        r'>ROSANGELA <span class="text-[#E06138]">ALVES</span></span>',
        t
    )
    
    # Just in case there's any remaining "Clínica Estética Rosangela" (e.g. title tags)
    t = t.replace('Clínica Estética Rosangela', 'Rosangela Alves')

    return t

def apply_new_identity_escaped(text):
    t = text
    t = t.replace('bg-[#E3C15E]', 'bg-[#4A5441]')
    t = t.replace('text-[#E3C15E]', 'text-[#E06138]')
    t = t.replace('border-[#E3C15E]', 'border-[#4A5441]')
    t = t.replace('hover:bg-[#d4b04c]', 'hover:bg-[#384031]')
    t = t.replace('hover:text-[#d4b04c]', 'hover:text-[#C5502A]')
    
    t = t.replace('Clínica Estética Rosangela |', 'Rosangela Alves |')
    t = t.replace('Na Clínica Estética Rosangela', 'Na Rosangela Alves Estética Avançada')
    t = t.replace('com a Clínica Estética Rosangela', 'com Rosangela Alves')
    t = t.replace('com a Clínica Rosangela', 'com Rosangela Alves')
    t = t.replace('CLÍNICA ROSANGELA', 'ROSANGELA ALVES')
    t = t.replace('© 2026 Clínica Estética Rosangela', '© 2026 Rosangela Alves')
    
    t = re.sub(
        r'>Clínica Estética Rosangela</a>',
        r'>ROSANGELA <span class=\\"text-[#E06138]\\">ALVES</span><br><span class=\\"text-[0.4em] font-light tracking-[0.3em] text-stone-500 block -mt-1\\">ESTÉTICA AVANÇADA</span></a>',
        t
    )
    t = re.sub(
        r'>Clínica Estética Rosangela</span>',
        r'>ROSANGELA <span class=\\"text-[#E06138]\\">ALVES</span></span>',
        t
    )
    t = t.replace('Clínica Estética Rosangela', 'Rosangela Alves')

    return t

# Apply to raw html
content = apply_new_identity(content)

# Apply to Base64 JSON
match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = apply_new_identity_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("New identity applied successfully!")
