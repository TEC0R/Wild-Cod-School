import streamlit as st
import base64
import os

def image(picture_name, picture_texte,width=100,height=100):
    image_path = os.path.join("picture", f"{picture_name}.png")
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode()

    return f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width}% height={height} padding= 0>
        </div>
    """

def acceuil():

    st.markdown(image("image","logo",width="auto",height=100), unsafe_allow_html=True)

    st.markdown("<style>.st-emotion-cache-enabax{text-align: center;}.st-emotion-cache-12rcsx5 p{font-size: xx-large;}</style>", unsafe_allow_html=True)

    st.title("Bonjour !")

    st.subheader("Quel est votre username ?")
    username = st.text_input(" ")

    st.subheader("Quel est la langue que vous souhaitez travailler ?")
    langue = st.selectbox("",("Anglais", "Espagnol", "Allemand"))

    if st.button("Submit"):
        st.session_state.info = {"username": username, "langue": langue}
        st.rerun()







