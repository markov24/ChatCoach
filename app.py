import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    # if request.method == "POST":
    #     audio_file = request.form["audio_file"]
    #     transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="text")
    #     return redirect(url_for("index", result=transcript))
        # animal = request.form["animal"]
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(animal),
        #     temperature=0.6,
        # )
        # return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
