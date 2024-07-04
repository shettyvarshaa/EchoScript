import json
from flask import Flask, jsonify
from transcriber import transcriber, speak
from webscraper import fetch_stackoverflow_code

app = Flask(__name__)

@app.route("/", methods=["GET"])
def handle_request():
    command_json = transcriber()
    if command_json:
        command_data = json.loads(command_json)
        command = command_data["command"]
        if "find a java code for simple calculator from stack overflow" in command:
            speak("Searching for Java code on Stack Overflow.")
            code = fetch_stackoverflow_code("java code for simple calculator site:stackoverflow.com")
            if code:
                response = {
                    "message": "Here is the Java code for a simple calculator from Stack Overflow.",
                    "code": code
                }
            else:
                response = {
                    "message": "Could not find the code on Stack Overflow."
                }
        else:
            response = {
                "message": "Command not recognized."
            }
    else:
        response = {
            "message": "Voice command system did not receive a valid command."
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(port=8080)