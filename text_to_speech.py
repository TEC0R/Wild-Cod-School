from deepgram import DeepgramClient, SpeakOptions
import streamlit as st
import base64

def text_to_speech(text,model):
    try:
        api = st.secrets["deepgram_api"]
        filename = "reponse_IA.wav"
        SPEAK_OPTIONS = {"text": text}
        deepgram = DeepgramClient(api_key=api)
 
        options = SpeakOptions(
            model=model,
            encoding="linear16",
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")

def play_to_speech():
    audio_file = open(r'reponse_IA.wav', 'rb')
    audio_bytes = audio_file.read()
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    st.markdown(
        f"""
        <audio id="audio" src="data:audio/wav;base64,{audio_base64}" autoplay></audio>
        <script>
        var audio = document.getElementById("audio");
        audio.play();
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    text_to_speech("hello")




