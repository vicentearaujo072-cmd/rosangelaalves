import os
import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the whole `<div class="lg:col-span-3 p-8 lg:p-16 bg-white"> ... </div>` and replace it entirely.
pattern = r'<div class="lg:col-span-3 p-8 lg:p-16 bg-white">.*?<!-- Info Side -->'

new_block = """<div class="lg:col-span-3 p-8 lg:p-16 bg-white flex flex-col justify-center">
<div class="mb-10">
<span class="text-[#D75C37] font-bold text-xs uppercase tracking-[0.2em] mb-2 block">Agendamento Rápido</span>
<h2 class="text-3xl md:text-5xl font-serif text-stone-900 mb-4 leading-tight">Fale Conosco pelo <br/>WhatsApp</h2>
<p class="text-stone-500 font-light max-w-md text-sm md:text-base leading-relaxed">
    Valorizamos um atendimento direto e exclusivo para cada paciente. Clique no botão abaixo para falar diretamente com a nossa equipe no WhatsApp, tirar dúvidas e agendar o seu tratamento.
</p>
</div>

<div class="space-y-8">
<div class="flex items-start gap-4 p-6 bg-[#EAE4D9]/20 rounded-2xl border border-stone-100">
    <div class="w-12 h-12 rounded-full bg-[#4A5441]/10 flex items-center justify-center text-[#4A5441] shrink-0">
        <iconify-icon icon="lucide:message-circle" width="24"></iconify-icon>
    </div>
    <div>
        <h4 class="font-bold text-stone-900 mb-1 text-sm">Sem formulários complexos</h4>
        <p class="text-xs text-stone-500 leading-relaxed">Sua consulta está a apenas um clique de distância. Nossa recepção responderá prontamente com todas as informações necessárias.</p>
    </div>
</div>

<div class="pt-4">
<a class="w-full sm:w-auto inline-flex items-center justify-center gap-3 py-5 px-10 bg-[#2C2C2C] text-white rounded-full text-sm font-bold uppercase tracking-widest hover:bg-[#4A5441] transition-all shadow-lg hover:shadow-xl hover:-translate-y-1 group" href="https://wa.me/5511999999999" target="_blank">
    <iconify-icon icon="mdi:whatsapp" width="24" class="group-hover:scale-125 transition-transform duration-300"></iconify-icon>
    Agendar via WhatsApp
</a>
<p class="text-[10px] text-stone-400 mt-4 max-w-md">
    * Você será redirecionado para o WhatsApp. Atendimento em horário comercial.
</p>
</div>
</div>
</div>
<!-- Info Side -->"""

def replace_form(text):
    t = text
    t = re.sub(pattern, new_block, t, flags=re.DOTALL)
    return t

def replace_form_escaped(text):
    t = text
    esc_pattern = r'<div class=\\"lg:col-span-3 p-8 lg:p-16 bg-white\\">.*?<!-- Info Side -->'
    esc_new_block = new_block.replace('\\n', '\\\\n').replace('\"', '\\\\\"')
    t = re.sub(esc_pattern, esc_new_block, t, flags=re.DOTALL)
    return t

content = replace_form(content)

match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    new_data_str = replace_form_escaped(data_str)
                    new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                    entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Form replaced with WhatsApp CTA successfully!")
