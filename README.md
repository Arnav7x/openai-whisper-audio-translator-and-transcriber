# OpenAI Whisper Audio Translator

This is a terminal-based application that uses OpenAI's Whisper API to transcribe audio files and then translate the transcribed text into different languages using GPT-4.

## Features

- Upload or record audio (MP3, M4A, WAV, etc.)
- Automatic speech-to-text transcription using Whisper
- Translation into multiple languages using GPT-4
- Terminal-only interface (no web server)

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

Transcribe and translate an existing audio file:
```bash
python3 main.py path/to/your_audio_file.m4a English
```

Or record from your microphone (default 10s) and translate:
```bash
python3 main.py --record 10 English
```

Interactive mode (choose record or file):
```bash
python3 main.py
```

## Supported Audio Formats

- MP3
- M4A
- WAV
- FLAC
- MP4
- MPEG / MPGA
- OGA / OGG
- WEBM

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
