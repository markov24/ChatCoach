import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

level = "beginner"
language = "Spanish"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        audio_file = request.form["audio_file"]
        transcript = openai.Audio.transcribe(file=audio_file, model="whisper-1", response_format="text")

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"You are a {level} level teacher for {language}"},
                {"role": "user", "content": transcript}
            ]
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


