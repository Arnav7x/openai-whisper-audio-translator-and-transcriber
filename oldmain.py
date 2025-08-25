# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
from openai import OpenAI

client = OpenAI(api_key=os.getenv("openaikey"))
import os 
# audio_file= open("audio.mp3", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)

audio_file= open("hindi.m4a", "rb")
transcript = client.audio.translate("whisper-1", audio_file,language="en")

print(transcript)