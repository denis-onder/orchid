from flask import Flask, request
from main import handle_speech

app = Flask(__name__)


@app.route("/", methods=['POST'])
def handle_remote_command():
    message = request.json["message"].strip()

    if message and message != "":
        handle_speech(message)
        return "The message is being processed.", 200
    else:
        return "No message provided.", 400


app.run()