# whisper.py

import openai
import constants

# Function to transcribe customer audio complaints using the Whisper model


def transcribe_audio():
    """
    Transcribes an audio file into text using OpenAI's Whisper model.

    Returns:
    str: The transcribed text of the audio file.
    """
    # Load the audio file.
    with open("project/audio/message1.mp3", "rb") as mp3: 
         data = mp3.read()  # Read the audio file data 

    
# from openai import OpenAI
#client = OpenAI()

#with open("audio.mp3", "rb") as f:
#    transcription = client.audio.transcriptions.create(
#        model="gpt-4o-transcribe",
#        file=f,
#        response_format="text"
#    )

#print(transcription)


    # TODO: Call the Whisper model to transcribe the audio file.

    # TODO: Extract the transcription and return it.

    pass  # Replace this with your implementation

# Example Usage (for testing purposes, remove/comment when deploying):
if __name__ == "__main__":
     transcription = transcribe_audio()
     print(transcription)
