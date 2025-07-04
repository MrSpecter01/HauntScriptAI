"""
This the main web-app that user interact to generate the horror story of their choice.

"""

import io
import streamlit as st
from PIL import Image
from utils.promptmaker import rephrase_prompt
from utils.formatting import format_txt
from horror import generate_horror_story

# Initializing all the session state variables
for key in ["story", "story_prompt", "poster", "user_inputs"]:
    if key not in st.session_state:
        st.session_state[key] = None


st.title("HauntScriptAI")
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
    #8757
    rephrase = st.checkbox("Re-phrase prompt with AI")
    user_prompt = rephrase_prompt(user_prompt) if rephrase else user_prompt
    extra_context = st.text_input("Additional Context/info: ")
    vocab_list = ["None","Simple", "Complex", "Child-like", "Adult", "Custom"]
    vocab_select = st.selectbox("Choose a Vocabulary style", vocab_list, index=0)
    vocab = st.text_input("Custom Vocabulary Style") if vocab_select == "Custom" else vocab_select
    cover_pic = st.checkbox("Generate a cover Image for the story (experimental)")
    cover_image = "Yes" if cover_pic else "No"



user_inputs = {
    'Genre':style,
    'MC':character_name,
    'Situation':story_situation,
    'Number Of Lines': num_of_lines,
    'Creativity (temperature)': temp,
    'References':references,
    'Vocabulary Style':vocab,
    'Additional Context/info':extra_context,
    'Cover Image': cover_image
    }

if st.button("Generate Story"):
    with st.spinner("Generating your Horror Story..."):
        try:
            story_prompt, story, poster = generate_horror_story(user_inputs, user_prompt)

            st.session_state.story_prompt = story_prompt
            st.session_state.story = story
            st.session_state.poster = poster
            st.session_state.user_inputs = user_inputs

        except Exception as e:
            st.error(f"An error occurred: {e}")


if st.session_state.story_prompt:
    st.subheader("Prompt Used:")
    st.write(st.session_state.story_prompt)

if isinstance(st.session_state.poster, Image.Image):
    st.subheader("Cover Image:")
    st.image(st.session_state.poster, width=400)

if st.session_state.story:
    st.subheader("Your Horror Story:")
    st.write(st.session_state.story)


    col1, col2 = st.columns([2, 2])

    with col1:
        if st.session_state.story:
            st.download_button(
                label="Download story as TXT",
                data=format_txt(
                    st.session_state.user_inputs,
                    st.session_state.story_prompt,
                    st.session_state.story
                ),
                file_name="HauntScriptAI.txt",
                mime="text/plain"
            )

    with col2:
        if isinstance(st.session_state.poster, Image.Image):
            img_buffer = io.BytesIO()
            st.session_state.poster.save(img_buffer, format="PNG")
            img_buffer.seek(0)
            st.download_button(
                label="Download Image",
                data=img_buffer,
                file_name="HauntScriptAI_cover.png",
                mime="image/png"
            )
