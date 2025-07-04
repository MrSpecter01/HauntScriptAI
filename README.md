# HauntScript: AI-Driven Horror Story Generator
## HauntScript uses AI to generate spine-chilling horror stories from user prompts, offering an effortless tool for writers, creators, and horror enthusiasts

HauntScript uses AI to generate spine-chilling horror stories from user prompts, offering an effortless tool for writers, creators, and horror enthusiasts. With a simple and intuitive interface, users can shape their story by selecting a horror subgenre, naming characters, defining the situation, and even setting the desired story length. For more control, HauntScript includes an advanced menu that allows temperature adjustment for creativity, uploading a reference .txt file, setting a custom prompt (which overrides all other inputs), adding context, and choosing a preferred vocabulary style. Once the story is generated, users can easily download it as a .txt file, making HauntScript a powerful yet accessible tool for anyone looking to bring terrifying tales to life.

## Visuals/Demo Video of the project:
https://drive.google.com/file/d/122NoGe0eRtMRU64Z9AT0UXdfbDqlbvIC/view?usp=sharing

## Key Features:
- Generate horror stories from user inputs (sub-genre, character, setting, length)
- Advanced controls: creativity (temperature), vocabulary style, additional context
- Upload .txt files for reference-based generation
- Fully AI-generated content using the Gemini API
- Download the final story as a .txt file

## Tech Stack:
- Python 3.x
- Streamlit
- Gemini API (LLM)
- uv for dependency and virtual environment management

## How to use this app:
You need python, git installed and, a valid Gemini API Key in order to setup and run this web-app. You can install them by following any tutorial on the internet.

### Follow these below steps to setup and use the web-app:
1. Clone the repo by using the command: `git clone https://github.com/MrSpecter01/HauntScriptAI.git`
2. Change into the directory: `cd HauntScriptAI`
3. Install UV: `pip install uv`
#### Steps 4 and 5 are optional
4. Setup a Virtual Environment: `uv venv .venv`
5. Activate the Virtual Environment: `.venv\Scripts\activate`
6. Install all the dependencies using the following command: `uv pip install -r requirements.txt`
7. Add your Gemini API Key in the .env file.
8. Start up the StreamLit app: `streamlit run horror.py`
9. Once the app is up and running, you will get a local url for the web-app, use it to open it in your web browser. It will look something like this: `http://localhost:8501`
10. Follow the steps there to generate a Horror Story.

## Future Scope:
This project can be further expanded by to generate stories of more diverse genre and categories. It's core logic can be used to expand beyond horror story generation into other genres as well such as Adventure, Sci-Fi, Slice of Life story generation or even a multi-genre story generation as well. Other utility tools can be added to generate concept images, ideas and short clips similar to the cover image generation that is used in this project to get visual suitable to the story. Combining these various tools and the core generation logic mentioned above, generating a full fledged movie, series, novels or starting material for much more development and creativity can obtained from this project. Various Machine Learning algorithms can also be used in fine-tuning such as RLHF can drastically help the project perform much better.


## Author/Project Developer:
1. AnandKumar V