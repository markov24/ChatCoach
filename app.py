import os
import openai
from flask import Flask, redirect, send_from_directory, render_template, request, url_for
# from flask_sock import Sock
import text_to_speech as tts

# Creating a Flask app and instantiating sockets and OpenAI API
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


# Get language and level from user options

level = "beginner"
language = "Spanish"

language_to_name = {"Arabic":"Zeina",
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
name = language_to_name[language]
history = [{"role": "system", "content": f"You are a {language} teacher for {level} level students"},
           {"role": "user", "content": f"You are going to be a {language} language teacher for {level} students. Write every response in {language}, and write the responses as if you are writing to a {level} student.  NEVER TELL me that you are an AI language model and that you can't answer my question - if I ask what your favorite color or number is, for example you can say green, or 7. Your name is {name}. Start by saying - hello, I am {name}, how are you doing today - in {language}."}]

responseFilePath = ""
oldFilePath = ""

@app.route("/src/")
def src():
    return responseFilePath

@app.route("/", methods=("GET", "POST"))
def index():
    global responseFilePath
    global oldFilePath

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
        
        responseFilePath = tts.TTS(response_text, language)
        if(oldFilePath != ""):
            os.remove(oldFilePath)
        oldFilePath=responseFilePath
        return responseFilePath
    
    # When the user selects their preferences, update the URL to reflect them
    ###

    result = request.args.get("result")
    print(result)
    return render_template("index.html")

