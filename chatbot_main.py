import openai
import streamlit as st
import os
from streamlit_chat import message as msg

# openai.api_key = os.getenv("API_KEY_CHATBOT")
openai.api_key = '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'

st.title("Chat Bot com Chat GPT")
st.write("***")

if 'conversa' not in st.session_state:
    st.session_state.conversa = []

pergunta = st.text_input("O que deseja perguntar ?")
botaoEnviar = st.button("Perguntar")
if botaoEnviar:
    st.session_state.conversa.append({"role": "user", "content": pergunta})
    retornoOpenAi = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state.conversa
    )
    st.session_state.conversa.append(
        {"role": "assistant",
        "content": retornoOpenAi['choices'][0]['message']['content']})

if len(st.session_state.conversa) > 0:
    for i in range(len(st.session_state.conversa)):
        if i % 2 == 0:
            msg("Você: " + st.session_state.conversa[i]['content'], is_user=True)
        else:
            msg("Resposta IA: " + st.session_state.conversa[i]['content'])
