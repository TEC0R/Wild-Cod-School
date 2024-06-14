import streamlit as st
from acceuil import acceuil
from game_one import game_one
from game_two import game_two
from choise_game import choise_game
from chat import chat


if "choise" in st.session_state:
    if st.session_state.choise == 1:
        game_one()
    if st.session_state.choise == 2:
        chat()
    if st.session_state.choise == 3:
        game_two()

elif "info" in st.session_state:
    choise_game()
    
else :
    acceuil()


