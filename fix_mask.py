import os
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
icon_path = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\assets\icon_rino.png'

with open(icon_path, 'rb') as img_f:
    encoded_string = base64.b64encode(img_f.read()).decode('utf-8')

b64_uri = f"data:image/png;base64,{encoded_string}"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the url('assets/icon_rino.png') with url('data:image/png;base64,...')
content = content.replace("url('assets/icon_rino.png')", f"url('{b64_uri}')")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected base64 mask!")
