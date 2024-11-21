import os

# Directory structure
project_structure = {
    "app.py": "from flask import Flask, render_template, request, jsonify, send_file\n"
              "from utility import transcribe_audio, get_reply, generate_tts, init_openai_api\n\n"
              "app = Flask(__name__)\n\n"
              "# Initialize OpenAI API\n"
              "init_openai_api(\".env\")\n\n"
              "@app.route(\"/\")\ndef index():\n    return render_template(\"index.html\")\n\n"
              "@app.route(\"/transcribe\", methods=[\"POST\"])\n"
              "def transcribe():\n    audio_file = request.files[\"audio\"]\n"
              "    transcription = transcribe_audio(audio_file)\n    return jsonify({\"transcription\": transcription})\n\n"
              "@app.route(\"/reply\", methods=[\"POST\"])\n"
              "def reply():\n    data = request.json\n    question = data.get(\"text\", \"\")\n"
              "    reply = get_reply(question)\n    tts_audio_path = generate_tts(reply)\n"
              "    return jsonify({\"reply\": reply, \"audio_url\": tts_audio_path})\n\n"
              "@app.route(\"/audio/<filename>\")\n"
              "def audio(filename):\n    return send_file(f\"./static/audio/{filename}\")\n\n"
              "if __name__ == \"__main__\":\n    app.run(debug=True)\n",
    "templates/index.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n"
                            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
                            "    <title>Speech-to-Text</title>\n    <link rel=\"stylesheet\" href=\"/static/css/style.css\">\n"
                            "</head>\n<body>\n    <div class=\"container\">\n"
                            "        <h1>Real-Time Speech-to-Text and Text-to-Speech</h1>\n"
                            "        <button id=\"start-recording\">Start Recording</button>\n"
                            "        <button id=\"stop-recording\">Stop Recording</button>\n"
                            "        <div id=\"transcription\"></div>\n"
                            "        <div id=\"reply\"></div>\n"
                            "        <audio id=\"audio-player\" controls></audio>\n"
                            "    </div>\n    <script src=\"/static/js/main.js\"></script>\n</body>\n</html>\n",
    "static/css/style.css": "body {\n    font-family: Arial, sans-serif;\n    text-align: center;\n    padding: 20px;\n}\n"
                            "button {\n    margin: 10px;\n    padding: 10px 20px;\n    background-color: #007BFF;\n"
                            "    color: white;\n    border: none;\n    border-radius: 5px;\n    cursor: pointer;\n}\n"
                            "button:hover {\n    background-color: #0056b3;\n}\n",
    "static/js/main.js": "document.getElementById(\"start-recording\").addEventListener(\"click\", () => {\n"
                         "    console.log(\"Start recording clicked\");\n});\n\n"
                         "document.getElementById(\"stop-recording\").addEventListener(\"click\", () => {\n"
                         "    console.log(\"Stop recording clicked\");\n});\n",
    "utility.py": "import whisper\nimport openai\nfrom gtts import gTTS\nimport os\n\n"
                  "def transcribe_audio(audio_file):\n"
                  "    model = whisper.load_model(\"base\")\n"
                  "    audio = whisper.load_audio(audio_file)\n"
                  "    result = model.transcribe(audio)\n    return result[\"text\"]\n\n"
                  "def get_reply(prompt):\n"
                  "    response = openai.Completion.create(\n"
                  "        model=\"text-davinci-002\",\n"
                  "        prompt=f\"Q: {prompt}\\nA:\",\n"
                  "        max_tokens=100\n"
                  "    )\n    return response[\"choices\"][0][\"text\"].strip()\n\n"
                  "def generate_tts(text, output_dir=\"static/audio\"):\n"
                  "    os.makedirs(output_dir, exist_ok=True)\n"
                  "    filepath = os.path.join(output_dir, \"response.mp3\")\n"
                  "    tts = gTTS(text=text, lang=\"en\")\n"
                  "    tts.save(filepath)\n    return filepath\n\n"
                  "def init_openai_api(env_path=\".env\"):\n"
                  "    with open(env_path) as env:\n"
                  "        for line in env:\n            key, value = line.strip().split(\"=\")\n"
                  "            os.environ[key] = value\n"
                  "    openai.api_key = os.environ.get(\"API_KEY\")\n"
                  "    openai.organization = os.environ.get(\"ORG_ID\")\n",
    "requirements.txt": "flask\nwhisper\ngtts\nopenai\nnumpy\n",
}

# Create files and directories
for path, content in project_structure.items():
    dirs, filename = os.path.split(path)
    if dirs:
        os.makedirs(dirs, exist_ok=True)
    with open(path, "w") as file:
        file.write(content)

print("Project files created successfully!")
