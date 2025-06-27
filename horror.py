"""
This is the main script that drives the HauntScript AI

generates horror stories based on user's preferences
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
from promptmaker import craft_horror_prompt, rephrase_prompt
from format_txt import format_txt

# Load API key from .env
load_dotenv()
api_key = os.getenv("api_key")

# Configure Gemini
genai.configure(api_key=api_key)

# Model configuration
generation_config = {
    "temperature": 0.77,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)

def generate_horror_story(inputs, custom_prompt):
    """ used to generate a horror story based on the inputs from the user"""
    genre = inputs["Genre"]
    mc = inputs["MC"]
    situation = inputs["Situation"]
    no_of_lines = inputs["Number Of Lines"]
    references = inputs["References"]
    vocabulary = inputs["Vocabulary Style"]
    context = inputs["Additional Context/info"]

    prompt = custom_prompt if custom_prompt != '' else craft_horror_prompt(genre.lower(),mc, situation, no_of_lines, references, vocabulary, context)

    generation_config["temperature"] = inputs["Creativity (temperature)"]

    response = model.generate_content(prompt)
    return prompt, response.text  # Assuming response.text returns the story

# Streamlit App UI
st.title("Horror Story Generator")
st.write("Enter the details below to generate your custom Horror Story:")

genre_list = ["None","Psychological", "Supernatural", "Gore", "Thriller", "Classic", "Custom Genre"]
style = st.selectbox("Choose a horror style", genre_list, index=0)
style = st.text_input("Custom Genre") if style == "Custom Genre" else style
character_name = st.text_input("Character Name", placeholder="Give your MC's name here..")
story_situation = st.text_input("Situation", placeholder="What is the situation/setting of your story?")
num_of_lines = st.number_input("Number Of Lines", min_value=1, value=5)
with st.expander("+ Advanced Options"):
    temp = st.slider("Creativity (Temperature)", 0.3, 1.0, 0.77, step=0.01)
    uploaded_file = st.file_uploader("Upload a reference text file", type=["txt"])
    if uploaded_file is not None:
        # Read file as string
        references = uploaded_file.read().decode("utf-8")
    else:
        references = ""
    user_prompt = st.text_area("Custom prompt override", placeholder="Enter your own full prompt here... (Only this prompt will be used to generate, no other settings will be applied)")
    rephrase = st.checkbox("Re-phrase prompt with AI")
    user_prompt = rephrase_prompt(user_prompt) if rephrase else user_prompt
    extra_context = st.text_input("Additional Context/info: ")
    vocab_list = ["None","Simple", "Complex", "Child-like", "Adult", "Custom"]
    vocab_select = st.selectbox("Choose a Vocabulary style", vocab_list, index=0)
    vocab = st.text_input("Custom Vocabulary Style") if vocab_select == "Custom" else vocab_select


user_inputs = {
    'Genre':style,
    'MC':character_name,
    'Situation':story_situation,
    'Number Of Lines': num_of_lines,
    'Creativity (temperature)': temp,
    'References':references,
    'Vocabulary Style':vocab,
    'Additional Context/info':extra_context
    }

if st.button("Generate Story"):
    with st.spinner("Generating your Horror Story..."):
        try:
            story_prompt, story = generate_horror_story(user_inputs, user_prompt)
            st.subheader("Prompt Used:")
            st.write(story_prompt)
            st.subheader("Your Horror Story:")
            st.write(story)
            st.download_button(
                label="Download as TXT",
                data=format_txt(user_inputs, story_prompt, story),
                file_name="HauntScriptAI.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
