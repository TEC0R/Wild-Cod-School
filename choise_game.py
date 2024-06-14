import streamlit as st
from streamlit_card import card
from acceuil import image

def choise_game():
    st.set_page_config(layout="wide")
    st.markdown(image("image","logo",width="auto",height=100), unsafe_allow_html=True)

    choise_1, choise_2, choise_3 = st.columns(3)

    with choise_1:
        choise_1 = card(
        title="Chasse aux mots",
        text="Trouve la bonne traduction",
        )

        if choise_1:
            st.session_state.choise = 1

    with choise_2:
        choise_2 = card(
        title="Chat",
        text="Mise en situation"
        )

        if choise_2:
            st.session_state.choise = 2

    with choise_3:
        choise_3 = card(
        title="Definimots",
        text="Trouver le mot lié à la définition",
        )

        if choise_3:
            st.session_state.choise = 3