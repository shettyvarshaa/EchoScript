import json
from transcriber import transcriber, speak
from webscraper import fetch_stackoverflow_code

def main():
    command_json = transcriber()
    if command_json:
        command_data = json.loads(command_json)
        command = command_data["command"]
        speak(f"Searching for {command} on Stack Overflow.")
        code = fetch_stackoverflow_code(command + " site:stackoverflow.com")
        if code:
            print("Scraped Code:\n", code)
            speak(f"Here is the code related to {command} from Stack Overflow.")
        else:
            speak("Could not find the code on Stack Overflow.")
    else:
        speak("Voice command system did not receive a valid command.")

if __name__ == "__main__":
    main()