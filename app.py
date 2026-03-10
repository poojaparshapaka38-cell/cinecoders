import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCJ9PD5WSXvG56IhXvb38yL2vL7TIzbhOo")
        
model = genai.GenerativeModel("models/gemini-1.5-flash")
st.title("🎬 Scriptoria - AI Film Pre-Production System")
st.write("Generate story ideas, characters, scenes and scripts using AI.")

option = st.selectbox(
    "Select Tool",
    ("Story Idea Generator", "Character Generator", "Scene Generator", "Script Generator")
)

theme = st.text_input("Enter movie theme")

if st.button("Generate"):

    if option == "Story Idea Generator":
        prompt = f"Generate a creative movie story idea about {theme}"

    elif option == "Character Generator":
        prompt = f"Create a detailed film character for a movie about {theme}"

    elif option == "Scene Generator":
        prompt = f"Write a cinematic scene for a movie about {theme}"

    elif option == "Script Generator":
        prompt = f"Write a short movie script about {theme} with dialogues"

    response = model.generate_content(prompt)

    st.subheader("Generated Output")
    st.write(response.text)