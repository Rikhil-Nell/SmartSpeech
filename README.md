# SmartSpeech

SmartSpeech is an intelligent transcription tool that allows you to upload audio files, transcribe them into text, and chat with the transcript using an AI assistant. This enables users to engage in meaningful conversations based on recorded discussions.

## Features

- **Audio Transcription**: Upload audio files in formats like WAV, MP3, and OGG for automatic transcription.
- **Chat with Your Transcript**: Engage in conversations using the extracted transcript as context.
- **Persistent Chat Memory**: Keeps track of interactions to provide coherent responses.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (optional but recommended for dependency management)
- A [GROQ API Key](https://groq.com) for LLM-based chat functionality

### Installation

Clone the repository:

```sh
git clone https://github.com/yourusername/smartspeech.git
cd smartspeech
```

Install dependencies using `uv` (recommended) or `pip`:

```sh
uv venv .venv && source .venv/bin/activate
uv sync
```

Or with `pip`:

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory and add the following:

```sh
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key from Groq.

### Running the Application

Start the SmartSpeech Streamlit app:

```sh
streamlit run app.py
```

### Usage

1. **Upload an Audio File**: Go to the `Transcript` section and upload an audio file.
2. **View Transcription**: The app will transcribe the audio and display the text.
3. **Chat with the Transcript**: Switch to the `Chatbot` section to interact with the transcript contextually.

## Contributing

Feel free to submit issues or pull requests to enhance the project.

## License

MIT License

## Contact

Built with ❤️ by Rikhil Nellimarla. For support, contact me at [nrikhil@gmail.com](mailto:nrikhil@gmail.com).
