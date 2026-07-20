import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add lazy loading and decoding async to all images except hero
# Find all img tags
img_tags = re.findall(r'<img[^>]*>', content)
for img in img_tags:
    # Check if it's the hero image (assets/hero_clinic.png)
    if 'hero_clinic.png' in img or 'logo-ra.svg' in img:
        # Preload critical images: add decoding="sync"
        if 'decoding=' not in img:
            new_img = img.replace('<img ', '<img fetchpriority="high" decoding="sync" ')
            content = content.replace(img, new_img)
    else:
        # Lazy load below-the-fold images
        new_img = img
        if 'loading=' not in new_img:
            new_img = new_img.replace('<img ', '<img loading="lazy" decoding="async" ')
        # Add a default width/height aspect ratio to prevent layout shifts if missing
        if 'width=' not in new_img and 'height=' not in new_img:
            new_img = new_img.replace('<img ', '<img width="800" height="800" ')
        
        content = content.replace(img, new_img)

# 2. Add aria-labels to icon-only links for Accessibility
content = content.replace('<button class="p-2 -mr-2 text-stone-900"', '<button aria-label="Abrir menu" class="p-2 -mr-2 text-stone-900"')
content = content.replace('<button class="p-2 text-stone-900"', '<button aria-label="Fechar menu" class="p-2 text-stone-900"')
content = content.replace('<a class="w-10 h-10 rounded-full bg-stone-700 hover:bg-[#D75C37]', '<a aria-label="Acessar Instagram" class="w-10 h-10 rounded-full bg-stone-700 hover:bg-[#D75C37]')
content = content.replace('<a class="w-full flex items-center justify-center gap-3 py-3.5 bg-[#4A5441]', '<a aria-label="Agendar via WhatsApp" class="w-full flex items-center justify-center gap-3 py-3.5 bg-[#4A5441]')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Optimization complete!")
