# streamlit_grinch_app.py
# App temático do Grinch — "Serviços para Roubar o Natal" (paródia / diversão)
# Como rodar: 
# 1) crie um ambiente virtual (opcional): python -m venv .venv
# 2) ative e instale dependências: pip install streamlit
# 3) rode: streamlit run streamlit_grinch_app.py

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Oficina do Grinch", page_icon="🎄", layout="wide")

# CSS customizado (cores temáticas e pequena animação de neve)
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #0b3d0b 0%, #08320a 100%);
    color: #fff;
}
.header {
    font-family: 'Comic Sans MS', 'Segoe UI', Tahoma, sans-serif;
}
.grinch-card {
    background: rgba(0,0,0,0.25);
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}
.small-muted { color: #e9e9e9; opacity: 0.8; font-size:12px }
.button-green {
    background: linear-gradient(90deg, #71d06b, #3aa13a);
    color: black;
    font-weight: 700;
}
/* snow dots */
@keyframes snow {
  0% {transform: translateY(-10vh);} 
  100% {transform: translateY(110vh);} 
}
.snowflake {
  position: fixed;top:-10vh;left:0;z-index:0;opacity:0.7;
  animation: snow 30s linear infinite;
}
</style>
""", unsafe_allow_html=True)

# a few decorative snowflakes (purely visual)
st.markdown("""
<div class='snowflake'>❄️ ❄️ ❄️</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("A Oficina do Grinch")
st.sidebar.write("Bem-vindo ao único serviço que promete deixar o Natal... mais memorável. Sim, quando chega perto do natal, pessoas como nós simplesmente... vamos ficando mais esquisitas")


# Header
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("# 🎄 Oficina do Grinch — Planos para 'Roubar' o Natal")
    st.markdown("Um site oferecendo serviços ridiculamente ineficazes para quem quer viver como o Grinch, mas as vezes tem 5 empregos, muitos freelas, e não tem tempo")
with col2:
    st.markdown("**Status:** ✅ Online (safely fictitious)")
    st.markdown(f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.markdown("---")

# Main content
st.markdown("<div class='grinch-card'>", unsafe_allow_html=True)
st.subheader('Nossos "serviços"')
st.write("Escolha um plano e receba um kit imaginário — perfeito para festas temáticas, teatro escolar ou para quem quer se fantasiar de vilão natalino (responsavelmente!).")

plans = [
    {"nome":"Plano Sussurro", "preco":"Grátis", "descricao":"Sugestões de piadas secas e como dar bons foras."},
    {"nome":"Plano Meia-Noite", "preco":"R$ 9,99", "descricao":"Acesso a memes exclusivos do Grinch e ideias de decoração sinistra e fofa. Além disso, guia de como fazer provas de psicanálise"},
    {"nome":"Plano Mestre do Roubo (teatral)", "preco":"R$ 24,99", "descricao":"Kit digital com roteiro teatral, trilha sonora sugerida (livre de direitos) e ideias de atuação. Acompanha o livro Eu estou doida maluca, nao respondo ngm, n to apta pra contato social"}
]

for p in plans:
    with st.container():
        c1, c2 = st.columns([6,1])
        with c1:
            st.markdown(f"**{p['nome']}** — _{p['preco']}_")
            st.write(p['descricao'])
        with c2:
            if st.button(f"Selecionar: {p['nome']}", key=p['nome']):
                st.success(f"Você selecionou {p['nome']} — confirmação enviada.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Interactive: Criador de 'Plano Grinch' (puramente lúdico)
st.markdown("## Crie seu Plano Grinch")
with st.form(key='plan_form'):
    name = st.text_input('Nome do plano (ex: "Roubada no Trenó")')
    mood = st.selectbox('Tom', ['Sátira', 'Teatral', 'Meme'])
    audience = st.multiselect('Ideal para', ['Festa entre amigos', 'Peça escolar', 'Foto de perfil', 'Vídeo TikTok'])
    accept = st.checkbox('Confirmo que isto é pq estou ficando esquisita perto do natal')
    submit = st.form_submit_button('Gerar plano')

if submit:
    if not accept:
        st.error('Você precisa confirmar, não é você, sou eu')
    else:
        st.balloons()
        st.success('Plano criado! Aqui vai um resumo:')
        st.write(f"**{name or 'Plano Grinch Sem Nome'}** — Tom: {mood}")
        st.write('Público-alvo:', ', '.join(audience) if audience else 'Ninguém específico — só você')
        st.write('\n**Dicas para encenação (inofensivas):**')
        st.write('- Vista um suéter verde exagerado.')
        st.write('- Pratique uma risada dramática e olhares de desdém cômico.')
        st.write('- Prepare um discurso ridiculamente melodramático sobre por que não gosta de músicas alegres.')
        st.write('- Faça um vídeo curto para redes sociais com legenda humorística.')

st.markdown('---')

# Fake 'Ordem de Serviço' (não envia nada real)
st.markdown('## Pedido de Orçamento ')
with st.form('ordem_form'):
    cliente = st.text_input('Seu nome')
    email = st.text_input('E-mail (não será usado)')
    mensagem = st.text_area('Mensagem para o Grinch')
    enviar = st.form_submit_button('Enviar pedido')

if enviar:
    st.info('Obrigado — seu pedido foi recebido pelo nosso sistema imaginário do Polo Norte.')
    st.write('Resumo do pedido:')
    st.write(f'- Nome: {cliente or "Anônimo Grinch"}')
    st.write(f'- E-mail: {email or "não informado"}')
    st.write(f'- Mensagem: {mensagem or "-"}')

st.markdown('---')

st.markdown('<br><br>')

# Easter egg: ativar modo "Grinch Verdadeiro" (só muda o texto)
if st.checkbox('Ativar Modo Grinch'):
    st.markdown('> Você ouviu um cacoete de risada maligna...')

# small credits
st.markdown('\n---\n')
st.markdown('Feito com carinho pelo BIG e sua esposa. 🎭')

# end of file