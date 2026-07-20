import os
import re
import glob

html_files = glob.glob(r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\*.html')

for filepath in html_files:
    if 'index.html' in filepath:
        continue # Skip index, it's already perfect

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "Como Funciona" Image
    # We find the aspect-[4/3] block before "Como Funciona"
    # It looks like:
    # <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-xl bg-stone-200">\n<img alt="..." class="..." src="assets/ad_acne.png"/>\n</div>\n</div>\n<div class="space-y-6 order-1 lg:order-2">\n<span class="text-[#D75C37] font-bold text-xs uppercase tracking-[0.2em]">Como Funciona</span>
    
    # Let's use a regex to capture that specific img tag and replace its src with hero_clinic.png
    pattern_como_funciona = r'(<div class="aspect-\[4/3\].*?<img[^>]*?src=")([^"]+)("[^>]*?>\s*</div>\s*</div>\s*<div class="space-y-6 order-1 lg:order-2">\s*<span[^>]*>Como Funciona</span>)'
    content = re.sub(pattern_como_funciona, r'\g<1>assets/hero_clinic.png\g<3>', content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Fix Footer H2
    content = content.replace('<h2 class="text-2xl font-serif text-white mb-6">Rosangela Alves</h2>', '<div class="text-2xl font-serif text-white mb-6">Rosangela Alves</div>')

    # 3. Add Lazy Loading (Only for images that don't have it, skip logo and hero)
    # We will find all <img> tags.
    img_tags = re.findall(r'<img[^>]*>', content)
    first_hero_seen = False
    
    for img in img_tags:
        new_img = img
        if 'logo-ra.svg' in img:
            continue
        
        # The first non-logo image is the hero
        if not first_hero_seen:
            first_hero_seen = True
            if 'fetchpriority' not in new_img:
                new_img = new_img.replace('<img ', '<img fetchpriority="high" decoding="sync" ')
        else:
            if 'loading=' not in new_img:
                new_img = new_img.replace('<img ', '<img loading="lazy" decoding="async" ')
            if 'width=' not in new_img:
                new_img = new_img.replace('<img ', '<img width="800" height="800" ')
        
        if new_img != img:
            content = content.replace(img, new_img)

    # 4. ARIA Labels
    content = content.replace('<button class="p-2 -mr-2 text-stone-900"', '<button aria-label="Abrir menu" class="p-2 -mr-2 text-stone-900"')
    content = content.replace('<button class="p-2 text-stone-900"', '<button aria-label="Fechar menu" class="p-2 text-stone-900"')
    content = content.replace('<a class="w-10 h-10 rounded-full bg-stone-700 hover:bg-[#D75C37]"', '<a aria-label="Acessar Instagram" class="w-10 h-10 rounded-full bg-stone-700 hover:bg-[#D75C37]"')
    content = content.replace('<a class="w-full flex items-center justify-center gap-3 py-3.5 bg-[#4A5441]"', '<a aria-label="Agendar via WhatsApp" class="w-full flex items-center justify-center gap-3 py-3.5 bg-[#4A5441]"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Subpages optimized and contextualized!")
