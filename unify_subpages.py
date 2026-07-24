import os
import re
import glob

html_files = glob.glob(r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\*.html')

def unify_colors(text):
    t = text
    # Standardize Terracotta
    t = re.sub(r'(?i)#E3C15E', '#D75C37', t) # Gold -> Terracotta
    t = re.sub(r'(?i)#d4b04c', '#D75C37', t) # Dark Gold -> Terracotta
    t = re.sub(r'(?i)#E06138', '#D75C37', t) # Orange-ish Terracotta -> Unified Terracotta
    
    # Standardize Light Beige/Cream instead of Blue-gray
    t = re.sub(r'(?i)#D1DDE8', '#EAE4D9', t) # Blue-gray -> Warm Beige
    return t

for filepath in html_files:
    if 'index.html' in filepath:
        continue # Skip index

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = unify_colors(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors unified on all subpages!")
