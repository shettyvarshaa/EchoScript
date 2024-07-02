import speech_recognition as sr
import pyttsx3
import json
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_for_activation():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'start coding' to start voice commands...")
        audio = recognizer.listen(source)
        try:
            phrase = recognizer.recognize_google(audio)
            print(f"Phrase received: {phrase}")
            return phrase.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

def transcriber():
    speak("Voice command system activated.")
    while True:
        activation_phrase = listen_for_activation()
        if activation_phrase == "start coding":
            speak("Voice command system activated. Please say your command.")
            command = listen_for_command()
            if command:
                result = {
                    "command": command
                }
                return json.dumps(result)
        else:
            time.sleep(1)