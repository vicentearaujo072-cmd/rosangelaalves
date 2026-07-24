import os
import re

mapping = {
    'botox-campo-grande.html': 'assets/process_botox.png',
    'cicatrizes-acne-campo-grande.html': 'assets/process_acne.png',
    'enzimas-gordura-localizada-campo-grande.html': 'assets/process_enzimas.png',
    'harmonizacao-facial-campo-grande.html': 'assets/process_harmonizacao.png',
    'preenchimento-olheiras-campo-grande.html': 'assets/process_olheiras.png',
    'rinomodelacao-campo-grande.html': 'assets/process_rino.png'
}

base_dir = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build'

for filename, img_path in mapping.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The pattern finds the image inside the aspect-[4/3] block before "Como Funciona"
    # We previously forced it to assets/hero_clinic.png
    pattern_como_funciona = r'(<div class="aspect-\[4/3\].*?<img[^>]*?src=")[^"]+(".*?>\s*</div>\s*</div>\s*<div class="space-y-6 order-1 lg:order-2">\s*<span[^>]*>Como Funciona</span>)'
    
    # Replace the src with the specific image for this procedure
    content = re.sub(pattern_como_funciona, r'\g<1>' + img_path + r'\g<2>', content, flags=re.DOTALL | re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Procedure-specific images injected into subpages!")
