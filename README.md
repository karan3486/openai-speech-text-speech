---

# Voice-Driven AI Chatbot

A Flask-based web application for real-time voice-driven AI interaction. This project transcribes audio files, generates intelligent responses using OpenAI GPT, and provides audio feedback using text-to-speech (TTS).
![image](https://github.com/user-attachments/assets/274c77ee-071f-4fd3-aea7-7cf8386d7b1b)
![image](https://github.com/user-attachments/assets/7912cd56-d71c-43d4-b9d7-95d6a895725d)




---

## Features

- **Audio Transcription**: Uses the Whisper model to transcribe audio files.
- **AI Response Generation**: Leverages OpenAI GPT-3.5 Turbo for intelligent and context-aware responses.
- **Text-to-Speech Feedback**: Converts AI responses into audio using OpenAI TTS-1.
- **Seamless Integration**: Modular design for easy enhancements and scalability.

---

## Technology Stack

- **Backend Framework**: Flask
- **Audio Transcription**: Whisper
- **AI Response Generation**: OpenAI GPT-3.5 Turbo
- **Text-to-Speech**: Open AI tts-1
- **Utilities**: Werkzeug for secure file handling, Dotenv for managing environment variables

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/voice-driven-ai-chatbot.git
   cd voice-driven-ai-chatbot
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     API_KEY=your_openai_api_key
     ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   - Open your browser and go to `http://127.0.0.1:5000`.

---

## Usage

1. Upload an audio file in the **"Transcribe"** section.
2. The system will:
   - Transcribe the audio using Whisper.
   - Generate a response with GPT-3.5 Turbo.
   - Convert the response to speech and return it as an audio file.
3. Download or play the generated audio file from the provided link.

---

---

## Dependencies

- Flask
- OpenAI
- Whisper
- gTTS
- Werkzeug
- Python-dotenv

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- **Multi-Language Support**: Expand transcription and TTS capabilities.
- **Mobile App Integration**: Build a mobile-friendly version of the application.
- **Real-Time Streaming**: Support for live audio transcription and response.

---

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

---

## Contributions

Contributions are welcome! Please fork the repository and create a pull request with your improvements or suggestions.

---
\
