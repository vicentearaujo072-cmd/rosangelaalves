import os
import re
import json
import base64

directory = r"C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build"

replacements = [
    (r'a especialista Rosangela Alves', r'a especialista Dra. Rosangela Alves'),
    (r"a Rosangela Alves entrega", r"a Dra. Rosangela Alves entrega"),
    (r"Conheça Rosangela", r"Conheça a Dra. Rosangela"),
    (r"Conhe&ccedil;a Rosangela", r"Conhe&ccedil;a a Dra. Rosangela"),
    (r"Com a Rosangela Alves, cada tratamento combina ci[êe]ncia e arte\.\s*Especializados em criar resultados naturais e transformadores, focados na sua beleza e auto-estima\.", r"A Dra. Rosangela Alves possui experiência na área há mais de 15 anos, é formada em estética e cosmetologia, pós-graduada em farmácia estética e com formação em biomedicina estética."),
    (r"Com um espa[çc]o acolhedor onde seus desejos s[ãa]o ouvidos, suas necessidades s[ãa]o respeitadas e seus belos resultados s[ãa]o celebrados\.", r"Com um espaço acolhedor onde seus desejos são ouvidos, a clínica oferece tratamentos que combinam ciência e arte, focados na sua beleza e auto-estima."),
    (r"com a Rosangela\. O resultado", r"com a Dra. Rosangela. O resultado")
]

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Apply replacements on raw HTML
            for old_p, new_p in replacements:
                content = re.sub(old_p, new_p, content, flags=re.DOTALL)
            
            # Now update the base64 ASSET_MAP if it exists
            match = re.search(r'var D = (\{.*?\});\n', content)
            if match:
                try:
                    D = json.loads(match.group(1))
                    for entry in D.get('entries', []):
                        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
                            b64data = entry['b']
                            try:
                                data_str = base64.b64decode(b64data).decode('utf-8')
                                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                                    # Apply replacements on decoded string
                                    for old_p, new_p in replacements:
                                        data_str = re.sub(old_p, new_p, data_str, flags=re.DOTALL)
                                    
                                    new_b64data = base64.b64encode(data_str.encode('utf-8')).decode('utf-8')
                                    entry['b'] = new_b64data
                            except Exception as e:
                                pass
                    new_D_str = json.dumps(D, separators=(', ', ': '))
                    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]
                except Exception as e:
                    pass
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
print("All Dra. Rosangela replacements done.")

