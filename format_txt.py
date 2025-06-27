"""
contains 1 function, used to format the story to write into TXT
format_txt(inputs:dict, prompt:str, story:str) -> str:
    takes 1 dictionary + 2 strings as arguments
    dictionary contains the inputs used to generate the story, prompt is the prompt used to generate the story, story is the generated story
    formatted story is the output string in the desired format
"""
from datetime import datetime

def format_txt(inputs:dict, prompt:str, story:str) -> str:
    """Takes user input choices as a dictionary, the prompt used to generate the story, the story and returns a formatted string to write """

    formatted_story = (f"User Inputs:\n {inputs}\n\nPrompt Used: \n{prompt}\n\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\n----- STORY -----\n{story}\n----- END -----")
    return formatted_story