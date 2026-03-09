import streamlit as st
from openai import OpenAI

# Replace with your OpenAI API key
client = OpenAI(api_key="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")

st.title("🎬 Scriptoria - AI Film Pre Production System")

idea = st.text_input("Enter Movie Idea")
genre = st.text_input("Enter Genre")

if st.button("Generate Script"):

    if idea and genre:

        prompt = f"Write a short movie script. Idea: {idea}. Genre: {genre}. Include characters and scenes."

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            result = response.output_text

            st.subheader("Generated Script")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter both idea and genre.")