import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title for Local SEO
old_title = r'<title>Rosangela Alves \| EstǸtica Avanada \| Tratamentos Faciais e Corporais</title>'
new_title = '<title>Clínica de Estética em [CIDADE]: Botox e Preenchimento | Rosangela Alves</title>'
# Since the original title had some encoding issues in powershell output, I will match it loosely
content = re.sub(r'<title>.*?</title>', new_title, content)

# 2. Update Meta Description for Local SEO
old_desc = r'<meta name="description" content="[^"]+"/>'
new_desc = '<meta name="description" content="Procurando Clínica de Estética em [CIDADE]? A Dra. Rosangela Alves é referência em Botox, Preenchimento de Olheiras, Rinomodelação e Enzimas no [BAIRRO]. Agende agora!"/>'
content = re.sub(old_desc, new_desc, content)

# 3. Inject JSON-LD Schema Markup for Local Business (This is the Holy Grail of Local SEO)
schema_markup = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "Rosangela Alves - Estética Avançada",
  "image": "https://www.instagram.com/drarobiomedica/",
  "@id": "",
  "url": "",
  "telephone": "+5511999999999",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Endereço exato da clínica",
    "addressLocality": "[CIDADE]",
    "addressRegion": "[ESTADO]",
    "postalCode": "00000-000",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -23.550520,
    "longitude": -46.633308
  },
  "department": [
    {
      "@type": "MedicalSpecialty",
      "name": "Botox",
      "description": "Aplicação de Toxina Botulínica"
    },
    {
      "@type": "MedicalSpecialty",
      "name": "Preenchimento Facial",
      "description": "Preenchimento de Olheiras e Rinomodelação"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/drarobiomedica/"
  ]
}
</script>
"""

# Insert schema right before closing </head>
content = content.replace('</head>', schema_markup + '\n</head>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Local SEO optimized successfully!")
