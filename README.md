# Jarvis Python

🤖 Jarvis is a Python-based voice assistant that uses speech recognition and text-to-speech to interact with users. It can execute voice commands, open websites and applications, search the web, provide information, and automate everyday tasks. Built as a hands-on project to explore Python, AI, APIs, and automation.

## Features
- Voice recognition using `speech_recognition`
- Text-to-speech using `pyttsx3`
- Open common apps like Google, YouTube, Notepad, and Calculator
- Get top news from NewsAPI
- Ask AI questions using Groq

## Project structure
- `main.py` - command handling and app flow
- `ai.py` - Groq AI integration
- `.env` - stores API keys locally

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   python -m pip install python-dotenv groq speechrecognition pyttsx3 pyautogui requests
   ```
3. Add your API keys to `.env`:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   NEWS_API_KEY=your_news_api_key_here
   ```
4. Run the app:
   ```powershell
   python main.py
   ```

## Notes
- Keep your `.env` file local and do not commit it to GitHub.
- The repository includes a `.gitignore` so virtual environments and secrets are not pushed.
