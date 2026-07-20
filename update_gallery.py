import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the owner image
content = content.replace('assets/dona da empresa.jpeg', 'assets/owner_professional.png')

old_gallery_regex = r'<!-- Before & After Gallery -->.*?<!-- Booking / Contato -->'

new_gallery_html = """<!-- Before & After Gallery -->
<section class="py-24 bg-[#FDFCFB]" id="gallery">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-16 space-y-4">
            <span class="text-[#E3C15E] font-bold text-xs uppercase tracking-[0.2em]">Resultados Reais</span>
            <h2 class="text-4xl font-medium text-stone-900">Antes e Depois</h2>
            <p class="text-stone-500 font-light">Confira as transformações reais de nossos pacientes em diferentes tratamentos.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/ad_botox.png" alt="Botox" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center">Botox</h3>
            </div>
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/ad_olheira.png" alt="Preenchimento de Olheira" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center">Preenchimento de Olheira</h3>
            </div>
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/ad_full_face.png" alt="Full Face" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center">Full Face</h3>
            </div>
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/ad_rino.png" alt="Rinomodelação" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center">Rinomodelação</h3>
            </div>
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/ad_acne.png" alt="Cicatrizes de Acne" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center">Cicatrizes de Acne</h3>
            </div>
            <div class="space-y-4">
                <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-lg group">
                    <img src="assets/new_antes_depois_6.png" alt="Enzima para Gordura Localizada" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>
                <h3 class="text-lg font-bold text-stone-900 text-center uppercase">Enzima para Gordura Localizada</h3>
            </div>
        </div>
    </div>
</section>
<!-- Booking / Contato -->"""

# Update raw HTML
content = re.sub(old_gallery_regex, new_gallery_html, content, flags=re.DOTALL)

# Update base64 HTML
match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = data_str.replace('assets/dona da empresa.jpeg', 'assets/owner_professional.png')
                    # Escape the new gallery html exactly how json dumps it
                    new_gallery_html_escaped = new_gallery_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
                    old_gallery_regex_escaped = r'<!-- Before & After Gallery -->.*?<!-- Booking / Contato -->'
                    new_data_str = re.sub(old_gallery_regex_escaped, new_gallery_html_escaped, new_data_str, flags=re.DOTALL)
                    
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery updated successfully!")
