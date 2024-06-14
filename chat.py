import streamlit as st
from typing import Generator
from groq import Groq
from acceuil import image
from text_to_speech import text_to_speech, play_to_speech


def chat():
    st.set_page_config(layout="centered")
    st.markdown("<style>.st-emotion-cache-ocqkz7{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown(image("image","logo",width="auto",height=100), unsafe_allow_html=True)
    st.subheader(" ")

    client = Groq(
        api_key= st.secrets["groq_api_key"],
    )

    machine_prompt = {
        "role": "system",
        "content": f"Tu es un professeur de {st.session_state.info['langue']}, ton rôle est d'ameliorer les conversations que je peux avoir en {st.session_state.info['langue']} et quand tu me parle tu dois toujours dire tes phrase d'abord en {st.session_state.info['langue']} puis en Français et par contre si je ne parle pas en {st.session_state.info['langue']} tu devras t'enerver !!"
    }

    # Initialize chat history and selected model
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add machine prompt and initial message from the assistant
        st.session_state.messages.append(machine_prompt)
        st.session_state.messages.append({"role": "assistant", "content": "Bonjour! Comment puis-je vous aider aujourd'hui ?"})

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = None



    # Display chat messages from history on app rerun
    for message in st.session_state.messages[1:]:
        avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])


    def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
        """Yield chat response content from the Groq API response."""
        for chunk in chat_completion:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


    if prompt := st.chat_input("Enter your prompt here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user", avatar='👨‍💻'):
            st.markdown(prompt)

        # Fetch response from Groq API
        try:
            chat_completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": m["role"],
                        "content": m["content"]
                    }
                    for m in st.session_state.messages
                ],
                max_tokens=300,
                stream=True
            )

            # Use the generator function with st.write_stream
            with st.chat_message("assistant", avatar="🤖"):
                chat_responses_generator = generate_chat_responses(chat_completion)
                full_response = st.write_stream(chat_responses_generator)
                if st.session_state.info['langue'] == "Anglais":
                    text_to_speech(full_response,"aura-athena-en")
                    play_to_speech()
        except Exception as e:
            st.error(e, icon="🚨")

        # Append the full response to session_state.messages
        if isinstance(full_response, str):
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response})
        else:
            # Handle the case where full_response is not a string
            combined_response = "\n".join(str(item) for item in full_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": combined_response})
            
    st.markdown("<style>.st-emotion-cache-ocqkz7{visibility: visible;}</style>", unsafe_allow_html=True)
