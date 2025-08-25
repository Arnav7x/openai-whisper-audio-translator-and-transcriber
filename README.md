# OpenAI Whisper Audio Translator

This is a Flask web application that uses OpenAI's Whisper API to transcribe audio files and then translate the transcribed text into different languages using GPT-4.

## Features

- Upload audio files (MP3, M4A, WAV, etc.)
- Automatic speech-to-text transcription using Whisper
- Translation into multiple languages using GPT-4
- Web-based interface

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up OpenAI API Key

Create a `.env` file in the project root and add your OpenAI API key:

```bash
# Create .env file
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
```

**Important:** 
- Replace `your_actual_api_key_here` with your real OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **NEVER commit the `.env` file to version control** - it contains your secret API key!
- The `.gitignore` file is already configured to exclude it

### 3. Run the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

## How to Use

1. Open your web browser and go to `http://localhost:5000`
2. Select the target language for translation
3. Upload an audio file
4. Click "Translate Audio"
5. Wait for the transcription and translation to complete
6. View the results

## Supported Audio Formats

- MP3
- M4A
- WAV
- FLAC
- And other common audio formats

## Supported Languages

- English
- Hindi
- Spanish
- French
- German
- Japanese
- Chinese
- Arabic
- Russian
- Portuguese
- Italian

## Troubleshooting

- Make sure you have a valid OpenAI API key
- Ensure your audio file is not corrupted
- Check that you have sufficient OpenAI API credits
- For large audio files, the process may take longer

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls
# openai-whisper-audio-translator-and-transcriber
