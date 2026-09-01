import os
import datetime
import subprocess
import webbrowser

import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
from dotenv import load_dotenv

from ai import ask_ai

load_dotenv()



def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise RuntimeError("NEWS_API_KEY is missing. Add it to your .env file.")

    url = f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["totalResults"] == 0:
        speak("Sorry boss, no news is available right now.")
        return

    speak("Here are today's top news")

    for article in data["articles"][:5]:
        title = article["title"]
        print(title)
        speak(title)


def take_screenshot():
    image = pyautogui.screenshot()
    image.save("screenshot.png")
    speak("Screenshot taken successfully")


def write_text(text):
    pyautogui.write(text)
    speak("I have written it boss")


def process_command(command):

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad"

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator"

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return current_time

    elif "news" in command:
        get_news()
        return "Here are today's top news"

    elif "screenshot" in command:
        take_screenshot()
        return "Screenshot taken"

    elif "write" in command:
        text = command.replace("write", "")
        write_text(text)
        return "I have written it boss"

    elif "good job" in command:
        speak("Thank you boss")
        return "Thank you boss"


    else:
        answer = ask_ai(command)
        speak(answer)
        return answer


def main_process():

    while True:

        wake_word = take_command()

        if "jarvis" in wake_word:

            speak("Yes boss, how can I help you?")

            while True:

                command = take_command()

                process_command(command)


main_process()
