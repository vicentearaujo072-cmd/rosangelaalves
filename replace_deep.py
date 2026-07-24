import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'Cloud La Med Spa | Fair Lawn, NJ | Cosmetic Injectables &amp; Wellness': 'Clínica Estética Rosangela | Tratamentos Faciais e Corporais',
    'Specialists in Non-Surgical Aesthetic Injectables, Medicine, Health, Wellness, and Skin Care in Fair Lawn, NJ.': 'Especialistas em Estética Avançada, Saúde, Bem-Estar e Cuidados com a Pele.',
    'Fair Lawn, NJ': 'Clínica Estética',
    '(201) 773-4558': '(11) 99999-9999',
    'tel:2017734558': 'tel:5511999999999',
    'VASA CLINIC': 'CLÍNICA ROSANGELA',
    'Medical Aesthetics': 'Estética Avançada',
    'Home': 'Início',
    'Services': 'Serviços',
    'Our Team': 'Sobre Nós',
    'Locations': 'Localização',
    'New Patients': 'Contato',
    'Call': 'Ligar',
    'Book Appointment': 'Agendar Avaliação',
    'Menu': 'Menu',
    'Call Us': 'Ligue para nós',
    'Request Appointment': 'Solicitar Avaliação',
    'Accepting New Patients': 'Agendamentos Abertos',
    'VIJAYAWADA <br> <span class="italic text-stone-500">Ultimate Med Spa</span>': 'CLÍNICA <br> <span class="italic text-stone-500">Rosangela</span>',
    'VIJAYAWADA <br> <span class=\\"italic text-stone-500\\">Ultimate Med Spa</span>': 'CLÍNICA <br> <span class=\\"italic text-stone-500\\">Rosangela</span>',
    'Your specialists in non-surgical aesthetic injectables, medicine, health, wellness, and skin care. Achieve true transformation with Dr. Walid Elkhalili.': 'Sua especialista em estética avançada, saúde e bem-estar. Alcance a verdadeira transformação com a Clínica Rosangela.',
    'Book Treatment': 'Agendar Tratamento',
    'View Menu': 'Ver Serviços',
    'Board Certified': 'Especialista',
    'Safe &amp; Sterile': 'Seguro &amp; Estéril',
    'Safe & Sterile': 'Seguro & Estéril',
    'Real Results': 'Resultados Reais',
    'Skin Resurfacing': 'Tratamentos de Pele',
    'Top Doctor <br><span class="font-normal text-stone-500">Awards</span>': 'Profissionais <br><span class="font-normal text-stone-500">Qualificados</span>',
    'Top Doctor <br/><span class="font-normal text-stone-500">Awards</span>': 'Profissionais <br/><span class="font-normal text-stone-500">Qualificados</span>',
    'Leading Physicians <br><span class="font-normal text-stone-500">of the World</span>': 'Tecnologia <br><span class="font-normal text-stone-500\">de Ponta</span>',
    'Leading Physicians <br/><span class="font-normal text-stone-500">of the World</span>': 'Tecnologia <br/><span class="font-normal text-stone-500">de Ponta</span>',
    'Board of Internal <br><span class="font-normal text-stone-500">Medicine</span>': 'Atendimento <br><span class="font-normal text-stone-500">Personalizado</span>',
    'Board of Internal <br/><span class="font-normal text-stone-500">Medicine</span>': 'Atendimento <br/><span class="font-normal text-stone-500">Personalizado</span>',
    '5.0 Stars <br><span class="font-normal text-stone-500">Google Reviews</span>': '5.0 Estrelas <br><span class="font-normal text-stone-500">Avaliações</span>',
    '5.0 Stars <br/><span class="font-normal text-stone-500">Google Reviews</span>': '5.0 Estrelas <br/><span class="font-normal text-stone-500">Avaliações</span>',
    'Our Medical Director': 'Nossa Especialista',
    'Meet Dr. Walid Elkhalili': 'Conheça Rosangela',
    'At Cloud La Med Spa in Fair Lawn, NJ, every treatment blends science and artistry. Led by Dr. Walid Elkhalili, a board-certified internist and expert in aesthetic medicine, our team specializes in creating natural, transformative results.': 'Na Clínica Estética Rosangela, cada tratamento combina ciência e arte. Nossa equipe é especialista em criar resultados naturais e transformadores, focados na sua beleza e auto-estima.',
    'At Cloud La Med Spa in Fair Lawn, NJ, every treatment blends science and artistry.\\n                        Led by Dr. Walid Elkhalili, a board-certified internist and expert in aesthetic medicine, our team specializes in creating natural, transformative results.': 'Na Clínica Estética Rosangela, cada tratamento combina ciência e arte.\\n                        Nossa equipe é especialista em criar resultados naturais e transformadores, focados na sua beleza e auto-estima.',
    'We are a supportive space where your aspirations are heard, your needs are respected, and your beautiful results are celebrated.': 'Somos um espaço acolhedor onde seus desejos são ouvidos, suas necessidades são respeitadas e seus belos resultados são celebrados.',
    'Expertise': 'Especialidade',
    'Board Certified Aesthetic Medicine': 'Especialista em Estética Avançada',
    'Philosophy': 'Filosofia',
    'Inspire Confidence, One Treatment at a Time': 'Inspirando Confiança, Um Tratamento de Cada Vez',
    'Our Expertise': 'Nossas Especialidades',
    'Curated Aesthetic Treatments': 'Tratamentos Estéticos Exclusivos',
    'Advanced technology meets medical expertise.': 'Tecnologia avançada e conhecimento especializado.',
    'Cosmetic Injectables': 'Injetáveis Estéticos',
    'Reduce fine lines and restore volume for smooth, radiant skin.': 'Reduza linhas finas e restaure o volume para uma pele lisa e radiante.',
    'Botox &amp; Dysport': 'Toxina Botulínica',
    'Juvederm &amp; Restylane': 'Preenchimento Facial',
    'Sculptra &amp; Radiesse': 'Bioestimuladores de Colágeno',
    'Kybella': 'Fios de PDO',
    'Book Now': 'Agendar Agora',
    'Skin Rejuvenation': 'Rejuvenescimento Facial',
    'Refresh and restore radiance for glowing, brighter skin.': 'Refresque e restaure o brilho para uma pele radiante e iluminada.',
    'Custom Facials': 'Limpeza de Pele Profunda',
    'SkinPen Microneedling': 'Microagulhamento',
    'Chemical Peels': 'Peelings Químicos',
    'Photofacials (IPL)': 'Luz Intensa Pulsada',
    'Tighten and improve texture for healthy, revitalized skin.': 'Melhore a textura para uma pele saudável e revitalizada.',
    'Opus Plasma': 'Laser Lavieen',
    'CO2 Laser': 'Laser CO2 Fracionado',
    'RF Microneedling': 'Radiofrequência',
    'Laser Hair Removal': 'Depilação a Laser',
    'Body Wellness': 'Bem-Estar Corporal',
    'Revitalize and energize for a healthier body inside and out.': 'Revitalize e energize para um corpo mais saudável por dentro e por fora.',
    'IV Drip Infusions': 'Massagem Modeladora',
    'Hair Restoration': 'Drenagem Linfática',
    'Wellness Support': 'Tratamento para Celulite',
    'New Patient?': 'Novo Paciente?',
    'Request Appointment': 'Solicitar Avaliação',
    'Fill out the form below and our team will contact you to confirm.': 'Preencha o formulário abaixo e nossa equipe entrará em contato para confirmar.',
    'Full Name': 'Nome Completo',
    'Phone': 'Telefone',
    'Email': 'E-mail',
    'Interested In': 'Interesse Em',
    'Facials &amp; Skincare': 'Faciais e Skincare',
    'Laser Treatments': 'Tratamentos a Laser',
    'General Consultation': 'Avaliação Geral',
    'Message (Optional)': 'Mensagem (Opcional)',
    'Send Request': 'Enviar Solicitação',
    '* Note to dev: Connect to autoresponder.': '* Nossa equipe responderá o mais breve possível.',
    'Visit Us': 'Visite-nos',
    '6-20 Plaza Road, 2nd Floor<br>': 'Rua das Flores, 123<br>',
    'Fair Lawn, NJ 07410': 'São Paulo, SP 01000-000',
    'Get Directions': 'Como Chegar',
    'Hours': 'Horário de Funcionamento',
    'Mon - Fri:': 'Seg - Sex:',
    '9am - 6pm': '09:00 - 18:00',
    'Saturday:': 'Sábado:',
    'By Appt': 'Com Agendamento',
    'Sunday:': 'Domingo:',
    'Closed': 'Fechado',
    'Insurance &amp; Payments': 'Pagamentos',
    'We accept major credit cards and offer payment plans. Please note most cosmetic procedures are not covered by insurance.': 'Aceitamos os principais cartões de crédito e oferecemos planos de parcelamento.',
    'Cloud La Med Spa': 'Clínica Estética Rosangela',
    'Blending medical expertise with artistic vision to help you look and feel your best.': 'Combinando especialidade e visão artística para ajudar você a se sentir o seu melhor.',
    'Quick Links': 'Links Rápidos',
    'About Us': 'Sobre Nós',
    'Legal': 'Legal',
    'Privacy Policy': 'Política de Privacidade',
    'Terms of Service': 'Termos de Serviço',
    'Accessibility': 'Acessibilidade',
    '© 2026 Cloud La Med Spa. All Rights Reserved.': '© 2026 Clínica Estética Rosangela. Todos os direitos reservados.',
    'Designed with care for New Jersey.': 'Feito com amor.',
    'assets/4e9b0039d8d0ddda_996f32_4b36ca16ecb440f691ce276.png': 'assets/dona da empresa.jpeg',
    'https://static.wixstatic.com/media/996f32_4b36ca16ecb440f691ce2769d1052f66~mv2.png': 'assets/dona da empresa.jpeg',
    'Cloud La Med Spa Patient Results': 'Resultados Reais',
    'https://static.wixstatic.com/media/11062b_ed81470d7bb5405ea00aad717ac843b3~mv2.jpg': 'assets/antes e depois 2.jpeg',
    'VIJAYAWADA': 'Clínica Estética',
    'Aesthetic Medicine': 'Estética Avançada',
    'Accepting Contato': 'Agendamentos Abertos',
    'Our Especialidade': 'Nossas Especialidades',
}

# The gallery HTML
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
gallery_html_escaped = gallery_html.replace('\\n', '\\\\n').replace('\"', '\\\\\"')

def replace_in_text(text, is_escaped=False):
    t = text
    # Standard string replacements
    for k, v in replacements.items():
        if is_escaped:
            k_esc = k.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
            v_esc = v.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
            t = t.replace(k_esc, v_esc)
        else:
            t = t.replace(k, v)
    
    # Regex replacements for tricky whitespaces
    t = re.sub(
        r'At\s+Clínica\s+Estética\s+Rosangela\s+in\s+Clínica\s+Estética,\s+every\s+treatment\s+blends\s+science\s+and\s+artistry\.',
        'Na Clínica Estética Rosangela, cada tratamento combina ciência e arte.',
        t
    )
    t = re.sub(
        r'Led\s+by\s+Dr\.\s+Walid\s+Elkhalili,\s+a\s+board-certified\s+internist\s+and\s+expert\s+in\s+aesthetic\s+medicine,\s+our\s+team\s+specializes\s+in\s+creating\s+natural,\s+transformative\s+results\.',
        'Nossa equipe é especialista em criar resultados naturais e transformadores, focados na sua beleza e auto-estima.',
        t
    )
    
    # Insert gallery
    if 'id="gallery"' not in t and 'id=\\"gallery\\"' not in t:
        if is_escaped:
            t = t.replace('<!-- Booking / Contato -->', gallery_html_escaped + '\\\\n    <!-- Booking / Contato -->')
            t = t.replace('<!-- Booking / New Patients -->', gallery_html_escaped + '\\\\n    <!-- Booking / New Patients -->')
        else:
            t = t.replace('<!-- Booking / Contato -->', gallery_html + '\\n    <!-- Booking / Contato -->')
            t = t.replace('<!-- Booking / New Patients -->', gallery_html + '\\n    <!-- Booking / New Patients -->')
            
    return t

# 1. First, replace the raw HTML part
content = replace_in_text(content, is_escaped=False)

# 2. Next, find the base64 JSON payload and modify it
match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                # we only care about the chunk that contains "medical-spa-landing-30" or HTML code
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = replace_in_text(data_str, is_escaped=True)
                    # encode back
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                print("Error decoding/encoding JSON entry:", e)
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    # Replace the old var D = ... with the new one
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Full replacement complete!")
