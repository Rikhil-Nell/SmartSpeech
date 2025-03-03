import os
from groq import Groq
from settings import Settings
import pprint

# Initialize the Groq client
settings = Settings()
client = Groq(api_key=settings.groq_key)

# Specify the path to the audio file
filename = "recorded_audio.wav"  # Replace with your audio file!

# Open the audio file
with open(filename, "rb") as file:
    # Create a translation of the audio file
    translation = client.audio.transcriptions.create(
        file=(filename, file.read()),  # Required audio file
        model="whisper-large-v3",  # Required model to use for translation
        prompt="Specify context or spelling",  # Optional
        response_format="verbose_json",  # Optional
        temperature=0.0,  # Optional
    )
    # Print the translation text
    pprint.pprint(translation)
