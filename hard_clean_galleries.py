import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

correct_gallery = """<!-- Before & After Gallery -->
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
"""

def clean_galleries(text):
    # 1. Remove all gallery sections completely
    t = re.sub(r'<!-- Before & After Gallery -->\s*<section[^>]*?id="gallery".*?</section>', '', text, flags=re.DOTALL)
    t = re.sub(r'<!-- Before & After Gallery -->\s*<section[^>]*?id=\\"gallery\\".*?</section>', '', t, flags=re.DOTALL)
    
    # Also remove any stranded gallery sections
    t = re.sub(r'<section[^>]*?id="gallery".*?</section>', '', t, flags=re.DOTALL)
    t = re.sub(r'<section[^>]*?id=\\"gallery\\".*?</section>', '', t, flags=re.DOTALL)
    
    # Also clean up stranded comments
    t = t.replace('<!-- Before & After Gallery -->', '')
    
    # Now insert the correct one exactly once before Booking / Contato
    if '<!-- Booking / Contato -->' in t:
        t = t.replace('<!-- Booking / Contato -->', correct_gallery + '\n<!-- Booking / Contato -->', 1)
        
    return t

def clean_galleries_escaped(text):
    correct_gallery_escaped = correct_gallery.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    
    t = re.sub(r'<!-- Before & After Gallery -->\s*<section[^>]*?id="gallery".*?</section>', '', text, flags=re.DOTALL)
    t = re.sub(r'<!-- Before & After Gallery -->\s*<section[^>]*?id=\\"gallery\\".*?</section>', '', t, flags=re.DOTALL)
    t = re.sub(r'<section[^>]*?id="gallery".*?</section>', '', t, flags=re.DOTALL)
    t = re.sub(r'<section[^>]*?id=\\"gallery\\".*?</section>', '', t, flags=re.DOTALL)
    t = t.replace('<!-- Before & After Gallery -->', '')

    if '<!-- Booking / Contato -->' in t:
        t = t.replace('<!-- Booking / Contato -->', correct_gallery_escaped + '\\\\n<!-- Booking / Contato -->', 1)
        
    return t


content = clean_galleries(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = clean_galleries_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hard cleaned all duplicate galleries!")
