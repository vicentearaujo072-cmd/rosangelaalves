import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text using regex to handle varying whitespace/newlines
content = re.sub(
    r'At\s+Cloud\s+La\s+Med\s+Spa\s+in\s+Fair\s+Lawn,\s+NJ,\s+every\s+treatment\s+blends\s+science\s+and\s+artistry\.',
    'Na Clínica Estética Rosangela, cada tratamento combina ciência e arte.',
    content
)

content = re.sub(
    r'Led\s+by\s+Dr\.\s+Walid\s+Elkhalili,\s+a\s+board-certified\s+internist\s+and\s+expert\s+in\s+aesthetic\s+medicine,\s+our\s+team\s+specializes\s+in\s+creating\s+natural,\s+transformative\s+results\.',
    'Nossa equipe é especialista em criar resultados naturais e transformadores, focados na sua beleza e auto-estima.',
    content
)

content = re.sub(
    r'VIJAYAWADA',
    'Clínica Estética',
    content
)

# Insert gallery before the booking section
gallery_html = """
<!-- Before & After Gallery -->
<section class="py-24 bg-[#FDFCFB]" id="gallery">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-16 space-y-4">
            <span class="text-[#E3C15E] font-bold text-xs uppercase tracking-[0.2em]">Resultados</span>
            <h2 class="text-4xl font-medium text-stone-900">Antes e Depois</h2>
            <p class="text-stone-500 font-light">Confira as transformações reais de nossos pacientes.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 1.jpeg" alt="Antes e Depois 1" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 2.jpeg" alt="Antes e Depois 2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 3.jpeg" alt="Antes e Depois 3" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 4.jpeg" alt="Antes e Depois 4" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 5.jpeg" alt="Antes e Depois 5" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
            <div class="aspect-square rounded-2xl overflow-hidden shadow-lg group">
                <img src="assets/antes e depois 6.jpeg" alt="Antes e Depois 6" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
            </div>
        </div>
    </div>
</section>
"""

# check if gallery is already there to prevent duplication
if 'id="gallery"' not in content:
    content = content.replace('<!-- Booking / Contato -->', gallery_html + '\n    <!-- Booking / Contato -->')
    # also try replacing by the section ID just in case
    content = content.replace('<section class="py-24 bg-white relative" id="booking">', gallery_html + '\n    <section class="py-24 bg-white relative" id="booking">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed successfully")
