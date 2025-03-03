import streamlit as st
import asyncio
import os
from agents import audio_agent, chat_agent, messages
from pydantic_ai.messages import ModelRequest, ModelResponse, UserPromptPart, TextPart
from audio_transcription import transcribe_audio

# Set up the Streamlit app
st.title("Smart Speech")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "audio_uploaded" not in st.session_state:
    st.session_state.audio_uploaded = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

# Sidebar navigation
st.sidebar.header("Navigation")
selected_section = st.sidebar.radio("Select Section", ["Transcript", "Chatbot"])

# Main Section - File Upload and Transcription
if selected_section == "Transcript":
    st.header("Upload an Audio File")
    audio_file = st.file_uploader("Choose a file", type=["wav", "mp3", "ogg"])

    if audio_file:
        file_extension = os.path.splitext(audio_file.name)[1]
        file_path = os.path.join("uploads", f"recorded_audio{file_extension}")
        os.makedirs("uploads", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(audio_file.read())

        st.session_state.audio_uploaded = True
        st.session_state.audio_path = file_path

        # Call transcription function
        transcript = transcribe_audio(file_path)

        # Call the audio agent
        response = asyncio.run(audio_agent.run(user_prompt=transcript))
        parsed_transcript = response.data
        st.session_state.transcript = parsed_transcript

        st.text_area("Transcript:", parsed_transcript, height=200)

        # Setting up prompt for chat agent
        with open("chatprompt.txt", "r", encoding="utf-8") as file:
            content = file.read()
        
        updated_content = content.replace("{transcript}", parsed_transcript)

        with open("chatprompt.txt", "w", encoding="utf-8") as file:
            file.write(updated_content)

# Chatbot Section
elif selected_section == "Chatbot":
    st.header("Chat with your transcript")

    # Function to display chat messages
    def display_messages():
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Function to handle user input and get bot response
    async def get_bot_response(user_input: str):
        try:
            response = await chat_agent.run(
                user_prompt=user_input, message_history=messages
            )
            return response.data
        except Exception as e:
            return f"An error occurred: {str(e)}"

    if st.session_state.audio_uploaded:
        display_messages()
        user_input = st.chat_input("You: ")

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            with st.chat_message("user"):
                st.write(user_input)

            bot_response = asyncio.run(get_bot_response(user_input))

            st.session_state.messages.append(
                {"role": "assistant", "content": bot_response}
            )

            with st.chat_message("assistant"):
                st.write(bot_response)

            messages.append(ModelRequest(parts=[UserPromptPart(content=user_input)]))
            messages.append(ModelResponse(parts=[TextPart(content=bot_response)]))
    else:
        st.warning("Please upload an audio file first before chatting.")

# Footer
st.sidebar.write("---")
st.sidebar.markdown(
    "### Built with ❤️ by Rikhil Nellimarla.\n\n"
    "For support, contact me at [nrikhil@gmail.com](mailto:nrikhil@gmail.com)."
)
