import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the lucide:gem iconify block in Card 3 with the new image
old_icon_html = '<iconify-icon icon="lucide:gem" width="28"></iconify-icon>'
# The icon_rino.png is black, so to match the Terracotta initial color we can apply a filter or just use it.
# Actually, the user just wants the icon. A black icon might look okay, but since the theme is Terracotta, 
# if we want it to match #D75C37, we can use CSS filter, but that's complex for an exact hex. 
# Alternatively, we just use it as is, and on hover invert it.
new_icon_html = '<img src="assets/icon_rino.png" alt="Rinomodelação" class="w-8 h-8 object-contain transition-all duration-300 group-hover:brightness-0 group-hover:invert" />'

content = content.replace(old_icon_html, new_icon_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Rhinomodeling icon replaced!")
