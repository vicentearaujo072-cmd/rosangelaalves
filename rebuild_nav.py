import os
import re

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean Desktop Nav
desktop_nav_pattern = r'<nav class="hidden lg:flex items-center gap-8 text-\[13px\] font-medium text-stone-600 uppercase tracking-wide">.*?</nav>'
new_desktop_nav = """<nav class="hidden lg:flex items-center gap-8 text-[13px] font-medium text-stone-600 uppercase tracking-wide">
<a class="hover:text-[#D75C37] transition-colors" href="#home">Início</a>
<a class="hover:text-[#D75C37] transition-colors" href="#services">Serviços</a>
<a class="hover:text-[#D75C37] transition-colors" href="#team">Sobre Nós</a>
<a class="hover:text-[#D75C37] transition-colors" href="#locations">Contato</a>
</nav>"""
content = re.sub(desktop_nav_pattern, new_desktop_nav, content, flags=re.DOTALL)

# 2. Clean Mobile Nav
mobile_nav_pattern = r'<nav class="flex-1 overflow-y-auto p-6 flex flex-col gap-6 text-sm font-medium uppercase tracking-wide text-stone-600">.*?</nav>'
new_mobile_nav = """<nav class="flex-1 overflow-y-auto p-6 flex flex-col gap-6 text-sm font-medium uppercase tracking-wide text-stone-600">
<a class="mobile-link hover:text-[#D75C37]" href="#home">Início</a>
<a class="mobile-link hover:text-[#D75C37]" href="#services">Serviços</a>
<a class="mobile-link hover:text-[#D75C37]" href="#team">Sobre Nós</a>
<a class="mobile-link hover:text-[#D75C37]" href="#locations">Contato</a>
</nav>"""
content = re.sub(mobile_nav_pattern, new_mobile_nav, content, flags=re.DOTALL)

# 3. Rebuild Services Section
services_pattern = r'<section class="py-24 bg-\[#F8F9FA\]" id="services">.*?</section>\s*<!--'
new_services = """<section class="py-24 bg-[#EAE4D9]/20" id="services">
<div class="max-w-7xl mx-auto px-4 sm:px-6">
<div class="text-center max-w-2xl mx-auto mb-16 space-y-4">
<span class="text-[#D75C37] font-bold text-xs uppercase tracking-[0.2em]">Nossas Especialidades</span>
<h2 class="text-4xl font-medium text-stone-900">Tratamentos Estéticos Exclusivos</h2>
<p class="text-stone-500 font-light">Tecnologia avançada e conhecimento especializado para o seu melhor resultado.</p>
</div>
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- Card 1 -->
<a href="botox-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:sparkles" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Toxina Botulínica</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Suavize rugas e linhas de expressão com o tratamento não cirúrgico mais popular do mundo. Resultados naturais.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

<!-- Card 2 -->
<a href="harmonizacao-facial-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:scan-face" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Harmonização Facial</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Equilíbrio e proporção perfeitos para o seu rosto. Realçamos sua beleza natural sem exageros.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

<!-- Card 3 -->
<a href="rinomodelacao-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:gem" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Rinomodelação</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Corrija imperfeições no nariz sem cirurgia. Procedimento rápido, seguro e com resultado imediato.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

<!-- Card 4 -->
<a href="preenchimento-olheiras-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:eye" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Preenchimento de Olheiras</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Restaure o volume da região dos olhos, diminua o aspecto de cansaço e recupere seu olhar iluminado.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

<!-- Card 5 -->
<a href="enzimas-gordura-localizada-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:activity" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Enzimas (Gordura)</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Aplicação de enzimas para quebra de gordura localizada. Tratamento corporal focado em definição.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

<!-- Card 6 -->
<a href="cicatrizes-acne-campo-grande.html" class="group bg-white rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all duration-300 border border-stone-100 flex flex-col hover:-translate-y-1">
<div class="w-14 h-14 bg-[#D75C37]/10 rounded-2xl flex items-center justify-center text-[#D75C37] mb-6 group-hover:bg-[#4A5441] group-hover:text-white transition-colors duration-300 shadow-sm">
<iconify-icon icon="lucide:droplet" width="28"></iconify-icon>
</div>
<h3 class="text-xl font-bold text-stone-900 mb-3 group-hover:text-[#D75C37] transition-colors">Cicatrizes de Acne</h3>
<p class="text-sm text-stone-500 leading-relaxed mb-6 flex-1">Protocolos avançados para renovação celular e alisamento da pele afetada por cicatrizes profundas.</p>
<div class="flex items-center text-[#D75C37] text-sm font-bold uppercase tracking-widest gap-2">
<span>Saiba Mais</span>
<iconify-icon icon="lucide:arrow-right" class="group-hover:translate-x-2 transition-transform duration-300"></iconify-icon>
</div>
</a>

</div>
</div>
</section>
<!--"""

content = re.sub(services_pattern, new_services, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Nav cleaned and Services rebuilt as 6 subpage links!")
