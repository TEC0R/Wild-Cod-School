import streamlit as st
import time
from game import game_1, response_game
from quest import quest
from acceuil import image


def game_one():
    st.set_page_config(layout="centered")
    st.markdown(image("image","logo",width="auto",height=100), unsafe_allow_html=True)
    st.markdown("<style>p{font-size: large;} .st-emotion-cache-12rcsx5 p{font-size: xx-large;}.st-emotion-cache-ocqkz7{text-align: center;}</style>", unsafe_allow_html=True)
    st.markdown("<style>.st-emotion-cache-ocqkz7{visibility: hidden;}</style>", unsafe_allow_html=True)

    if "response" not in st.session_state:  
        st.markdown("<style>.st-emotion-cache-ocqkz7{visibility: visible;}</style>", unsafe_allow_html=True)
        st.session_state.response = f"Bonjour, je m'appel {st.session_state.info['username']}"
        game_1(st.session_state.info['langue'])
        response_game(st.session_state.response)
        time.sleep(1)
        quest()
    else :
        st.markdown("<style>.st-emotion-cache-ocqkz7{visibility: visible;}</style>", unsafe_allow_html=True)
        time.sleep(1)
        quest()