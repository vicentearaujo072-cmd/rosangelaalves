import os
import re
import glob

html_files = glob.glob(r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The footer currently has: class="bg-[#2C2C2C] text-stone-300 pt-20 pb-10 text-sm font-light"
    # I want to change it to: pb-28 lg:pb-10 so that on mobile there is plenty of space for the sticky bottom button!
    old_footer_class = 'class="bg-[#2C2C2C] text-stone-300 pt-20 pb-10 text-sm font-light"'
    new_footer_class = 'class="bg-[#2C2C2C] text-stone-300 pt-20 pb-28 lg:pb-10 text-sm font-light"'
    
    content = content.replace(old_footer_class, new_footer_class)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer responsive padding patched for all pages!")
