from groq import Groq
from settings import Settings

settings = Settings()

client = Groq(api_key=settings.groq_key)


def transcribe_audio(file_path: str) -> str:
    """
    Transcribes the audio file located at `file_path` using the Groq API.

    Args:
        file_path (str): The path to the audio file to be transcribed.

    Returns:
        str: The transcribed text.
    """
    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(file_path, file.read()),
            model="whisper-large-v3-turbo",
            response_format="json",
            language="en",
            temperature=0.0,
        )
    return transcription.text
