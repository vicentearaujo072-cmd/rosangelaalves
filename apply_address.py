import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SEO Tags
content = content.replace('[CIDADE]', 'Campo Grande')
content = content.replace('[BAIRRO]', 'São Francisco')
content = content.replace('[ESTADO]', 'MS')

# 2. Update Schema Address
content = content.replace('"streetAddress": "Endereço exato da clínica"', '"streetAddress": "R. Dr. Dolor Ferreira de Andrade, 87"')
content = content.replace('"postalCode": "00000-000"', '"postalCode": "79010-060"')

# 3. Update the physical address text next to map
old_address_html = 'Endereço da Clínica (A definir)<br/>\n    Sua Cidade - UF'
new_address_html = 'R. Dr. Dolor Ferreira de Andrade, 87<br/>\n    São Francisco, Campo Grande - MS'
content = content.replace(old_address_html, new_address_html)

# 4. Update WhatsApp Number
content = content.replace('5511999999999', '5567992110677')

# 5. Update Map Embed URL
old_map_url = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.197410143521!2d-46.661937!3d-23.56133!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjPCsDMzJzQwLjgiUyA0NsKwMzknNDMuMCJX!5e0!3m2!1spt-BR!2sbr!4v1620000000000!5m2!1spt-BR!2sbr'
new_map_url = 'https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=pt-BR&amp;q=R.%20Dr.%20Dolor%20Ferreira%20de%20Andrade,%2087%20S%C3%A3o%20Francisco,%20Campo%20Grande%20-%20MS&amp;t=&amp;z=16&amp;ie=UTF8&amp;iwloc=B&amp;output=embed'
content = content.replace(old_map_url, new_map_url)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Location parameters fully configured!")
