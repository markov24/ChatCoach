import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

level = "beginner"
language = "Spanish"

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
example = [f"Greet the student in {i} and ask the student what they want to learn today? " for i in world]


@app.route("/", methods=("GET", "POST"))

def index():
    if request.method == "POST":
        print("POST RECEIVED")
        audio_file = request.files["audio_data"]
        # audio_file.save("static/temp.wav")
        transcript = openai.Audio.transcribe(file=audio_file, model="whisper-1", response_format="text")

        



        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"You are a {level} level teacher for {language}, limit your response to within two sentences"},
                {"role": "user", "content": transcript}
            ]
        )

        response2 = [openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"You are a {level} level teacher for {language}, limit your response to within two sentences"},
                {"role": "user", "content": i}
            ]
        ) for i in example]


        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)


