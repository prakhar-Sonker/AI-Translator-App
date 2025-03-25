import streamlit as st
import speech_recognition as sr
from googletrans import Translator

st.title("🌍 AI Translator App")

# Initialize Translator
translator = Translator()

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now!")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your speech."
        except sr.RequestError:
            return "Error connecting to the speech recognition service."

# UI Components
st.write("Enter a sentence or click the 🎤 button to speak.")

# Add speech button
if st.button("🎤 Speak"):
    spoken_text = recognize_speech()
    st.text_area("Recognized Text", spoken_text)

# Text Input
user_input = st.text_area("Enter text to translate:", key="text_input")

# Language Selection
target_language = st.selectbox(
    "Select target language",
    ["fr - French", "es - Spanish", "de - German", "hi - Hindi", "zh - Chinese"]
)

# Extract language code
lang_code = target_language.split(" - ")[0]

# Translate Button
if st.button("Translate"):
    if user_input:
        translated_text = translator.translate(user_input, dest=lang_code).text
        st.success(f"**Translated Text:** {translated_text}")
    else:
        st.warning("Please enter text to translate!")

