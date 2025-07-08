# HauntScript AI - Project Documentation

## Overview
HauntScript AI is a web-based application that generates custom horror stories using Google's Gemini AI. Users can create personalized horror narratives by specifying genre, characters, situations, and various creative parameters.

## Quick Start

### Prerequisites
- Python 3.x
- Google Gemini API key
- Git

### Installation
```bash
git clone https://github.com/MrSpecter01/HauntScriptAI.git
cd HORROR
pip install uv
uv pip install -r requirements.txt
```

### Configuration
1. Create `.env` file in root directory
2. Add your Gemini API key:
   ```
   api_key=your_gemini_api_key_here
   ```

### Run Application
```bash
streamlit run app.py
```
Access at: `http://localhost:8501`

## Project Structure

```
HORROR/
├── app.py              # Main Streamlit application
├── horror.py           # Core story generation logic
├── utils/
│   ├── promptmaker.py  # AI prompt engineering
│   ├── covergen.py     # Cover image generation
│   └── formatting.py   # Output formatting
├── requirements.txt    # Dependencies
├── .env               # API keys (create this)
└── README.md          # Project information
```

## Core Features

### Basic Story Generation
- **Genre Selection**: Psychological, Supernatural, Gore, Thriller, Classic
- **Character Input**: Custom character names
- **Situation Definition**: Story setting and context
- **Length Control**: Adjustable story length (lines)

### Advanced Options
- **Creativity Control**: Temperature adjustment (0.3-1.0)
- **Reference Upload**: Upload .txt files for story inspiration
- **Custom Prompts**: Override all settings with custom prompts
- **AI Prompt Enhancement**: Automatic prompt rephrasing
- **Vocabulary Styles**: Simple, Complex, Child-like, Adult
- **Cover Image Generation**: AI-generated story covers
- **Additional Context**: Extra story information

## Technical Implementation

### AI Models Used
- **Gemini 2.5 Flash**: Primary story generation
- **Gemini 2.0 Flash**: Prompt engineering and refinement
- **Gemini 2.0 Flash Preview**: Image generation

### Key Technologies
- **Frontend**: Streamlit
- **Backend**: Python 3.x
- **AI Integration**: Google Generative AI
- **Image Processing**: Pillow (PIL)
- **Environment Management**: python-dotenv

## API Usage

### Core Function
```python
def generate_horror_story(inputs, custom_prompt):
    """
    Generate horror story based on user inputs
    
    Args:
        inputs (dict): User preferences and settings
        custom_prompt (str): Optional custom prompt override
    
    Returns:
        tuple: (prompt_used, generated_story, cover_image)
    """
```

### Configuration Parameters
```python
generation_config = {
    "temperature": 0.77,  # Adjustable creativity
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}
```

## User Workflow

1. **Input Story Parameters**
   - Select horror genre
   - Enter character name
   - Define situation
   - Set story length

2. **Configure Advanced Settings** (Optional)
   - Adjust creativity level
   - Upload reference files
   - Set vocabulary style
   - Add context information

3. **Generate Story**
   - Click "Generate Story"
   - AI processes inputs
   - Story and cover generated

4. **Download Results**
   - Download story as TXT file
   - Download cover image (if generated)

## File Outputs

### Story Download Format
```
User Inputs: {user_preferences}
Prompt Used: {ai_prompt}
Date: {generation_date}

----- STORY -----
{generated_story}
----- END -----
```

### Supported File Types
- **Input**: .txt files for references
- **Output**: .txt files for stories, .png for covers

## Error Handling

### Common Issues
- **API Key Missing**: Check `.env` file configuration
- **Network Issues**: Ensure internet connectivity for AI calls
- **Invalid File Upload**: Only .txt files accepted for references
- **Generation Failures**: Retry with different parameters

### Debug Tips
- Check Streamlit logs for detailed error messages
- Verify API key validity
- Ensure all dependencies are installed
- Test with minimal inputs first

## Customization Options

### Prompt Engineering
- Custom prompt override functionality
- AI-assisted prompt rephrasing
- Reference-based story generation

### Creative Controls
- Temperature adjustment for creativity
- Vocabulary complexity selection
- Genre-specific story generation

### Visual Elements
- Experimental cover image generation
- Story-appropriate visual themes
- Downloadable image outputs

## Performance Notes

### Optimization
- Session state management for user experience
- Efficient API calls with appropriate model selection
- Modular architecture for maintainability

### Limitations
- Requires internet connection for AI generation
- API rate limits may apply
- Cover image generation is experimental

## Security Considerations

- API keys stored in environment variables
- No user data persistence
- Input validation for file uploads
- Secure credential management

## Future Enhancements

### Planned Features
- Multi-genre support beyond horror
- User profile management
- Story history and favorites
- Batch story generation

### Technical Improvements
- Database integration for story storage
- Enhanced error handling
- Performance monitoring
- Automated testing implementation

## Support

### Common Commands
```bash
# Install dependencies
uv pip install -r requirements.txt

# Run application
streamlit run app.py

# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### Troubleshooting
1. **Import Errors**: Reinstall dependencies
2. **API Failures**: Check API key configuration
3. **UI Issues**: Clear browser cache and reload
4. **File Errors**: Verify file permissions and formats

---

**Developer**: AnandKumar V  
**Framework**: Streamlit + Google Gemini AI  
**Version**: 1.0  
**Last Updated**: July 2025