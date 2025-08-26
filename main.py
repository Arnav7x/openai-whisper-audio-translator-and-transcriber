import os
import sys
import tempfile
import sounddevice as sd
from scipy.io.wavfile import write as wav_write
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def transcribe_and_translate(audio_file_path, target_language):
    """
    Transcribe an audio file and translate it to the target language
    """
    try:
        # Initialize OpenAI client with API key from environment
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Check if file exists
        if not os.path.exists(audio_file_path):
            print(f"❌ Error: File '{audio_file_path}' not found!")
            return
        
        # Check file format
        supported_formats = ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']
        file_extension = audio_file_path.lower().split('.')[-1]
        
        if file_extension not in supported_formats:
            print(f"❌ Error: Unsupported file format '{file_extension}'")
            print(f"Supported formats: {', '.join(supported_formats)}")
            return
        
        print(f"🎵 Processing audio file: {audio_file_path}")
        print(f"🌍 Target language: {target_language}")
        print("⏳ Transcribing audio...")
        
        # Open and transcribe the audio file
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        
        print(f"✅ Transcription: {transcript.text}")
        print("⏳ Translating...")
        
        # Translate the transcribed text
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You will be provided with a sentence in English, and your task is to translate it into {target_language}"},
                {"role": "user", "content": transcript.text}
            ],
            temperature=0,
            max_tokens=256
        )
        
        translation = response.choices[0].message.content
        print(f"✅ Translation ({target_language}): {translation}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def record_audio(seconds: int = 10, samplerate: int = 16000, channels: int = 1) -> str:
    """Record audio from the microphone and save to a temporary WAV file. Returns the file path."""
    try:
        print(f"🎙️ Recording for {seconds} seconds... Speak now.")
        audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.wait()
        temp_fd, temp_path = tempfile.mkstemp(suffix=".wav")
        os.close(temp_fd)
        wav_write(temp_path, samplerate, audio)
        print(f"✅ Saved recording to: {temp_path}")
        return temp_path
    except Exception as e:
        print(f"❌ Recording failed: {e}")
        return ""

def main():
    print("🎵 OpenAI Whisper Audio Translator (Terminal Version)")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set!")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        return
    
    # Check command line arguments
    audio_file = None
    target_language = None

    # Support: python main.py --record 5 English (record 5 seconds)
    if len(sys.argv) >= 2 and sys.argv[1] == "--record":
        try:
            rec_seconds = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else 10
            target_language = sys.argv[3] if len(sys.argv) >= 4 else "English"
        except Exception:
            rec_seconds = 10
            target_language = "English"
        audio_file = record_audio(seconds=rec_seconds)
        if not audio_file:
            return
        print(f"🎯 Using recorded audio, target language: {target_language}")
    elif len(sys.argv) >= 3:
        # Use command line arguments: python main.py <file> <language>
        audio_file = sys.argv[1]
        target_language = sys.argv[2]
        print(f"🎯 Using command line arguments:")
        print(f"   File: {audio_file}")
        print(f"   Language: {target_language}")
    else:
        # Interactive mode
        print("Usage:")
        print("  python3 main.py <audio_file> <language>")
        print("  python3 main.py --record [seconds] <language>")
        print("Example: python3 main.py --record 8 English")
        print("\nOr run without arguments for interactive mode:")
        
        # Choose record or file upload
        mode = input("Choose mode - record (r) or file (f): ").strip().lower()
        if mode == 'r':
            try:
                rec_seconds = int(input("Seconds to record (default 10): ") or 10)
            except ValueError:
                rec_seconds = 10
            audio_file = record_audio(seconds=rec_seconds)
            target_language = input("Target language (default English): ").strip() or "English"
        else:
            # Get audio file path
            audio_file = input("📁 Enter the path to your audio file: ").strip()
            if not audio_file:
                print("❌ No file path provided!")
                return
            # Get target language
            print("\n🌍 Available languages:")
            languages = [
                "English", "Hindi", "Spanish", "French", "German", "Japanese", 
                "Chinese", "Arabic", "Russian", "Portuguese", "Italian"
            ]
            for i, lang in enumerate(languages, 1):
                print(f"  {i}. {lang}")
            try:
                choice = int(input(f"\nSelect language (1-{len(languages)}): "))
                if 1 <= choice <= len(languages):
                    target_language = languages[choice - 1]
                else:
                    print("❌ Invalid choice! Using English as default.")
                    target_language = "English"
            except ValueError:
                print("❌ Invalid input! Using English as default.")
                target_language = "English"
    
    print(f"\n🎯 Processing: {audio_file} → {target_language}")
    print("-" * 50)
    
    # Process the audio file
    transcribe_and_translate(audio_file, target_language)
    
    print("\n✨ Done!")

if __name__ == "__main__":
    main()