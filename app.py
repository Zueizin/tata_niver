import streamlit as st
import datetime
import random
from PIL import Image  # Importe a biblioteca Pillow para trabalhar com imagens

# Configuração da página
st.set_page_config(
    page_title="Feliz Aniversário!",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS personalizado
st.markdown("""
    <style>
    .title {
        font-size: 4rem !important;
        color: #ff69b4 !important;
        text-align: center;
        margin-bottom: 30px;
    }
    .message {
        font-size: 1.5rem !important;
        text-align: center;
        margin: 20px 0;
    }
    .balloon {
        font-size: 2rem;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-style: italic;
        color: #666;
    }
    .surprise {
        animation: pulse 1.5s infinite;
        text-align: center;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

# Link para a música (agora o código de incorporação do YouTube)
youtube_embed_code = """
<iframe width="560" height="315" src="https://www.youtube.com/embed/YOSQcHP7xUc?si=gZOUjodkmJWpZurL&start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
"""

# Função para mostrar balões animados
def show_balloons(num):
    balloons = "🎈🎉🎊🎁🎂🍰🥳"
    cols = st.columns(num)
    for col in cols:
        with col:
            delay = random.uniform(0, 2)
            st.markdown(
                f'<div class="balloon" style="animation-delay: {delay}s;">'
                f'{random.choice(balloons)}</div>',
                unsafe_allow_html=True
            )

# Cabeçalho festivo
st.markdown('<div class="title">Feliz Aniversário Tata! 🎂</div>', unsafe_allow_html=True)

# *** ADICIONANDO UMA ÚNICA IMAGEM NO TOPO ***
try:
    imagem1 = Image.open("imagens/1.jpeg")  # Caminho corrigido
    st.image(imagem1, caption="Um bolo especial!", use_container_width=True)
except FileNotFoundError:
    st.error("Erro: A imagem '1.jpeg' não foi encontrada.")

# Botão de surpresa
if st.button("🎁 Clique para uma surpresa!", use_container_width=True):
    st.session_state.show_surprise = True

# Mostrar mensagem secreta com player de áudio e outra imagem
if st.session_state.get("show_surprise"):
    st.markdown(f"""
        <div class='surprise'>
        <h2 style='color: #ff1493;'>🎉 SURPRESA! 🎉</h2>
        <p style='font-size: 1.8rem;'>Você é incrível e merece todo o amor do mundo! 💖</p>
        {youtube_embed_code}
    """, unsafe_allow_html=True)
    st.balloons()

# Mostrar balões
show_balloons(10)

# Mensagem personalizada
nome = "Tata"
mensagem = f"""
<div class="message">
Querida {nome},<br><br>
aaaaaaaaaaaaaaaaaaaa<br>
aaaaaaaaaaaaaaaaaaaa<br>
aaaaaaaaaaaaaaaaaaaa<br>
aaaaaaaaaaaaaaaaaaaa.<br><br>
Com carinho,<br>
Seus amigos
</div>
"""
st.markdown(mensagem, unsafe_allow_html=True)

# *** ADICIONANDO MÚLTIPLAS IMAGENS EM COLUNAS ***
st.subheader("Mais pictures:")
cols = st.columns(2)

try:
    imagem2 = Image.open("imagens/2.jpeg")  # Caminho corrigido
    cols[0].image(imagem2, caption="Celebrando!", use_container_width=True)
except FileNotFoundError:
    cols[0].error("Imagem '2.jpeg' não encontrada.")

try:
    imagem3 = Image.open("imagens/3.jpeg")  # Caminho corrigido
    cols[1].image(imagem3, caption="Mais festa!", use_container_width=True)
except FileNotFoundError:
    cols[1].error("Imagem '3.jpeg' não encontrada.")

# Contador de idade
data_nascimento = datetime.date(2005, 5, 15)
hoje = datetime.date.today()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

st.markdown(f"""
<div class="message">
🎈 Parabéns pelos {idade} anos! 🎈
</div>
""", unsafe_allow_html=True)

# Rodapé
st.markdown('<div class="footer">Feito com carinho</div>', unsafe_allow_html=True)

# Mais balões no final
show_balloons(10)
