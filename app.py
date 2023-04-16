import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from flask_sock import Sock
import text_to_speech as tts

# Creating a Flask app and instantiating sockets and OpenAI API
app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
# socketio = SocketIO(app)
sock = Sock(app)

@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)

# Get language and level from user options

level = "beginner"
language = "Spanish"

temp_value = "HEllo my friend."

world = {"Arabic":"Zeina",
                        "Chinese":"Zhiyu",
                        "Danish":"Naja",
                        "Dutch":"Lotte",
                        "English":"Salli",
                        "French":"Léa",
                        "German":"Hans",
                        "Hindi":"Aditi",
                        "Icelandic":"Karl",
                        "Italian":"Giorgo",
                        "Japanese":"Mizuki",
                        "Korean":"Seoyeon",
                        "Norwegian":"Liv",
                        "Polish":"Ewa",
                        "Portuguese":"Cristiano",
                        "Romanian":"Carmen",
                        "Russian":"Tatyana",
                        "Spanish":"Miguel",
                        "Swedish":"Astrid",
                        "Turkish":"Filiz",
                        }

# Conversation begins by telling GPT how to act:
history = [{"role": "system", "content": f"You are a {level} level teacher for {language}"},]
example = [f"Greet the student in {i} and ask the student what they want to learn today? " for i in world]


@app.route("/", methods=("GET", "POST"))
def index():
    # When User sends a .wav file, transcribe it and generate a response, then send the response as audio
    if request.method == "POST":
        print("POST RECEIVED")
        audio_file = request.files["audio_data"]    # get the .wav that was POSTed from record.js
        audio_file.save("static/temp.wav")          # save the .wav to /static/

        audio_file = open("static/temp.wav", "rb")  # open .wav to be read
        
        transcript = openai.Audio.transcribe(file=audio_file, model="whisper-1", response_format="text") # GPT transcription ;)
        
        print("Transcript: " + transcript)
        history.append({"role":"user", "content":transcript})   # append user's message to conversation history

        response = openai.ChatCompletion.create(                # generate GPT's response
            model="gpt-3.5-turbo",
            messages=history
        )
        response_text = response['choices'][0]['message']['content']

        history.append({"role":"assistant", "content":response_text}) # append GPT's response to conversation history

        print("Response: " + response_text)
        print("History: ")
        for thing in history:
            print(thing['content'])
        
        response_file_path = tts.TTS(response_text, language)
        return redirect("index.html")
    
    # When the user selects their preferences, update the URL to reflect them
    ###

    result = request.args.get("result")
    print(result)
    return render_template("index.html")

# # Handle messages recieved over 'connect' channel
# @socketio.on('connect')
# def connect():
#     emit('after connect', {'data':'Fuck sockets...'})

# # @socketio.on('Value changed')
# # def value_changed(message):
# #     temp_value = message['data']
# #     emit('update value', message, broadcast=True)


# # Sockets handle app instantiation
# if __name__ == '__main__':
#     socketio.run(app)
