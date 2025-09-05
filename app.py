import streamlit as st
from gtts import gTTS
import base64
from pathlib import Path

# --------- PAGE CONFIG ------------
st.set_page_config(page_title="Text-to-Speech", page_icon="🔊", layout="centered")

# --------- LOAD CSS ------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------- TITLE & IMAGE ------------
st.markdown("<p class='subtitle'>Build :- by Prabhant Tiwari</p>", unsafe_allow_html=True)
st.markdown("<h1 class='title'>Text-to-Speech</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    text = st.text_area("", placeholder="Write text here...", height=120)

# --------- BUTTONS & AUDIO ------------
if st.button("🎙️ Generate Audio"):
    if text.strip():
        tts = gTTS(text, lang="hi")
        output_file = "output.mp3"
        tts.save(output_file)

        audio_file = open(output_file, "rb").read()
        audio_b64 = base64.b64encode(audio_file).decode()
        st.audio(audio_file, format="audio/mp3")

        st.markdown(
            f'<a href="data:audio/mp3;base64,{audio_b64}" download="speech.mp3">'
            '<button>👇Download</button></a>',
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please write some text first.")
