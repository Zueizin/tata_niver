import streamlit as st
import datetime
import random
from PIL import Image
import altair as alt
import pandas as pd
import numpy as np
import os

# Configuração da página
st.set_page_config(
    page_title="Feliz Aniversário!",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS personalizado
st.markdown(
    """
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
        0%,
        100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-20px);
        }
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
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.2);
        }
        100% {
            transform: scale(1);
        }
    }
    .botao-mensagem {
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
                unsafe_allow_html=True,
            )

# Cabeçalho festivo
st.markdown(
    '<div class="title">Feliz Aniversário Tata! 🎂</div>', unsafe_allow_html=True
)

# *** ADICIONANDO UMA ÚNICA IMAGEM NO TOPO ***
try:
    imagem1 = Image.open("imagens/1.jpeg")
    st.image(imagem1, caption="Felicidade!", use_container_width=True)
except FileNotFoundError:
    st.error("Erro: A imagem \'1.jpeg\' não foi encontrada.")

# Botão de surpresa
if st.button("🎁 Clique para uma surpresa!", use_container_width=True):
    st.session_state.show_surprise = True

# Mostrar mensagem secreta com player de áudio e outra imagem
if st.session_state.get("show_surprise"):
    st.markdown(
        f"""
        <div class=\'surprise\'>
        <h2 style=\'color: #ff1493;\'>🎉 SURPRESA! 🎉</h2>
        <p style=\'font-size: 1.8rem;\'>Você é incrível e merece todo o amor do mundo! 💖</p>
        {youtube_embed_code}
    """,
        unsafe_allow_html=True,
    )
    st.balloons()

# Mostrar balões
show_balloons(5)

st.subheader("Mensagens Especiais:")
col_botoes = st.columns(3)

Aurelio = "Olá, feliz aniversário! Te desejo tudo de bom, que teus sonhos se realizem e que você tenha cada vez mais saúde. Obrigado por tudo, todos os momentos com você foram repletos de felicidade. Sinto saudades! Ass: Aurelio Comunello Carneiro"
if col_botoes[0].button("Mensagem", key="botao1", use_container_width=True, help=Aurelio):
    st.info(Aurelio)

Baiano = "Sempre continue sendo essa pessoa que transborda felicidade e carinho, você é muito especial para mim, obrigado pelos momentos incríveis que já me proporcionou. Feliz aniversário Tata ❤️. Ass: Baiano"
if col_botoes[1].button("Mensagem", key="botao2", use_container_width=True, help=Baiano):
    st.info(Baiano)

Tiago = "Ola tata , mais um aninho completo , as coisas passam tão rápido.Ainda ontem estava no Crescer a mudar do sétimo c para o oitavo b,e n fazia ideia da importante amizade que iria conhecer e ter.Poucas palavras conseguem expressar o que significa tê-la como amiga , muitos dias de tristeza em que seu sorriso e os rapazes fizeram do meu dia algo feliz e alegre.Esse tempo passou e só resta agradecer pelos momentos vividos e das aprendizagens obtidas.Tenho muito carinho por ti independente dos novos ciclos,e da distância que permanece.Espero que aproveites teu dia da melhor forma possível.Desejo-te sucesso na tua nova fase e q consigas aquilo que desejas pra ser feliz e estar feliz.Obrigado e beijinhos 😁🥳   Ass: Tiago Magalhães"
if col_botoes[2].button("Mensagem", key="botao3", use_container_width=True, help=Tiago):
    st.info(Tiago)

# Mensagem personalizada
nome = "Tata"
mensagem = f"""
<div class="message">
Querida {nome},<br><br>
Feliz Aniversário Tata, fizemos esse site para demonstrar um pouco o quanto você é importante para nós
 e queremos que saiba que mesmo com a distância estamos sempre com você para tudo que precisar.
<br><br>
Com carinho,<br>
Seus amigos
</div>
"""
st.markdown(mensagem, unsafe_allow_html=True)

# *** ADICIONANDO GRÁFICO DISTÂNCIA X FELICIDADE ***
st.subheader("Gráfico Distância x Felicidade")
# Criar dados para o gráfico (função exponencial decrescente)
distancia = list(range(0, 101, 10))
felicidade = [100 * np.exp(-0.1 * d) for d in distancia]  # Exponencial decrescente
df = pd.DataFrame({"Distância (km)": distancia, "Felicidade": felicidade})

# Criar o gráfico de dispersão com uma linha
chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X("Distância (km)", scale=alt.Scale(domain=[0, max(distancia)])),
    y="Felicidade",
    tooltip=["Distância (km)", "Felicidade"]
).properties(
    title="Felicidade em Função da Distância",
).interactive()

# Exibir o gráfico
st.altair_chart(chart, use_container_width=True)

# *** ADICIONANDO MÚLTIPLAS IMAGENS EM COLUNAS ***
st.subheader("Mais fotos:")
cols = st.columns(3)

try:
    imagem2 = Image.open("imagens/2.jpeg")
    cols[0].image(imagem2, caption="...", use_container_width=True)
except FileNotFoundError:
    cols[0].error("Imagem \'2.jpeg\' não encontrada.")

try:
    imagem3 = Image.open("imagens/3.jpeg")
    cols[1].image(imagem3, caption="...", use_container_width=True)
except FileNotFoundError:
    cols[1].error("Imagem \'3.jpeg\' não encontrada.")

try:
    imagem4 = Image.open("imagens/4.jpeg")
    cols[2].image(imagem4, caption="...", use_container_width=True)
except FileNotFoundError:
    cols[2].error("Imagem \'4.jpeg\' não encontrada.")

# Adicionando mais imagens
cols2 = st.columns(3)
try:
    imagem5 = Image.open("imagens/5.jpeg")
    cols2[0].image(imagem5, caption="...", use_container_width=True)
except FileNotFoundError:
    cols2[0].error("Imagem \'5.jpeg\' não encontrada.")

try:
    imagem6 = Image.open("imagens/6.jpeg")
    cols2[2].image(imagem6, caption="...", use_container_width=True)
except FileNotFoundError:
    cols2[2].error("Imagem \'6.jpeg\' não encontrada.")

# Contador de idade
data_nascimento = datetime.date(2005, 5, 15)
hoje = datetime.date.today()
idade = (
    hoje.year
    - data_nascimento.year
    - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
)

st.markdown(
    f"""
<div class="message">
🎈 Parabéns pelos {idade} anos! 🎈
</div>
""",
    unsafe_allow_html=True,
)

# Rodapé
st.markdown('<div class="footer">Feito com carinho</div>', unsafe_allow_html=True)

# Mais balões no final
show_balloons(5)
