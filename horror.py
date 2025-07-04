"""
This is the main script that drives the HauntScript AI

generates horror stories based on user's preferences
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.promptmaker import craft_horror_prompt
from utils.covergen import generate_cover_image


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
    #8757
    generation_config["temperature"] = inputs["Creativity (temperature)"]

    system_instruction = ("Follow the number of lines specified in the user prompt, with about 15 words per line."
    "Add brief descriptive detail only if relevant — do not rename or substitute any provided terms."
    )

    response = model.generate_content([system_instruction,prompt])
    cover_image = generate_cover_image(response.text) if inputs['Cover Image'] == "Yes" else "No"
    return prompt, response.text, cover_image  # Assuming response.text returns the story
