import streamlit as st
import time
from game import response_game

def quest():
    st.markdown(st.session_state.response)
    st.subheader(" ")

    rep_1, rep_2, rep_3 = st.columns(3)

    if rep_1.button(st.session_state.button[0]):
        response_game(st.session_state.button[0])
        time.sleep(1)
        st.rerun()
    if rep_2.button(st.session_state.button[1]):
        response_game(st.session_state.button[1])
        time.sleep(1)
        st.rerun()
    if rep_3.button(st.session_state.button[2]):
        response_game(st.session_state.button[2])
        time.sleep(1)
        st.rerun()