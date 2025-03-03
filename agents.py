from dataclasses import dataclass
from typing import List

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.groq import GroqModel, GroqModelSettings
from pydantic_ai.messages import ModelMessage

from settings import Settings

settings = Settings()

groq_settings = GroqModelSettings(
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
)

# Audio Transcription Agent

llm = "llama-3.3-70b-versatile"

model = GroqModel(
    model_name=llm,
    api_key=settings.groq_key,
)

with open("audioprompt.txt", "r") as file:
    audio_prompt = file.read()

audio_agent = Agent(
    model=model,
    model_settings=groq_settings,
    system_prompt=audio_prompt,
    retries=3,
)

# Chat Agent

llm = "llama-3.3-70b-versatile"

model = GroqModel(
    model_name=llm,
    api_key=settings.groq_key,
)

with open("chatprompt.txt", "r") as file:
    chat_prompt = file.read()

chat_agent = Agent(
    model=model,
    model_settings=groq_settings,
    system_prompt=chat_prompt,
    retries=3,
)

messages: List[ModelMessage] = []
