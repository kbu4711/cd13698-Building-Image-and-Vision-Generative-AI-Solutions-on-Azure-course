# whisper.py

import openai
import constants
import librosa

# Function to transcribe customer audio complaints using the Whisper model


def transcribe_audio():
    """
    Transcribes an audio file into text using OpenAI's Whisper model.

    Returns:
    str: The transcribed text of the audio file.
    """
    # Load the audio file.
    


    audio, sample_rate = librosa.load("audio/message1.mp3", sr=None)
    print("load")
    print(audio)
    print(sample_rate)


    # TODO: Call the Whisper model to transcribe the audio file.

    # TODO: Extract the transcription and return it.

    pass  # Replace this with your implementation

# Example Usage (for testing purposes, remove/comment when deploying):
if __name__ == "__main__":
     transcription = transcribe_audio()
     print(transcription)
