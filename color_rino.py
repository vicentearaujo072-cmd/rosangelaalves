import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the img tag for the rhino icon with the CSS mask approach
old_icon_html = '<img src="assets/icon_rino.png" alt="Rinomodelação" class="w-8 h-8 object-contain transition-all duration-300 group-hover:brightness-0 group-hover:invert" />'

# bg-current inherits the text color of the parent container! 
# The parent has text-[#D75C37] and group-hover:text-white
new_icon_html = '<div class="w-8 h-8 bg-current transition-colors duration-300" style="-webkit-mask-image: url(\'assets/icon_rino.png\'); mask-image: url(\'assets/icon_rino.png\'); -webkit-mask-size: contain; mask-size: contain; -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat; -webkit-mask-position: center; mask-position: center;"></div>'

content = content.replace(old_icon_html, new_icon_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icon colored dynamically using CSS masks!")
