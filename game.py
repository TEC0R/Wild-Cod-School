import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
import re


def model(prompt_machine):
    model = ChatGroq(temperature=1, groq_api_key="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", model_name="llama3-70b-8192")

    prompt = prompt_machine

    st.session_state.chain = prompt | model
    st.session_state.historique_chat = ChatMessageHistory()

def memory_model(texte):
    st.session_state.historique_chat.add_user_message(texte)
    
    answer  = st.session_state.chain.invoke({"humain": st.session_state.historique_chat.messages})
    st.session_state.historique_chat.add_ai_message(answer.content)

    return answer.content


def game_1(langue):

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                    Tu es un professeur de {langue}, ton rôle est de me faire deviner de nouveaux mots en me donnant le mot en français bien apparent avec trois réponses potentielle A, B ou C avec un systeme de point et il faut que je te réponde en {langue} et que tu me corrige et enfin tu me donne un exemple d'utilisation de ce mot dans une phrase de tous les jours et tu dois toujours répondre en francais et tu dois toujours donner un mot en {langue} !
                
                """,
            ),
            MessagesPlaceholder(variable_name="humain"),
        ]
    )

    model(prompt)

def game_2(langue):

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                    Tu es un professeur de {langue}, ton rôle est de me faire deviner de nouveaux mots en me donnant la definition en français bien apparent avec trois réponses potentielle A, B ou C avec un systeme de point et il faut que je te réponde en {langue} et que tu me corrige et enfin tu me donne un exemple d'utilisation de ce mot dans une phrase de tous les jours et tu dois toujours répondre en francais et tu dois toujours donner un mot en {langue} !
                
                """,
            ),
            MessagesPlaceholder(variable_name="humain"),
        ]
    )

    model(prompt)
    
def response_game(texte) :
    response = memory_model(texte)
    st.session_state.button = re.findall(r'[A-Z]\)\s(\w+)', response)
    st.session_state.response = re.sub(r'[A-Z]\)\s(\w+)', '', response)


