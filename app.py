from flask import Flask, request, render_template, redirect, url_for
import requests
import json
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        requirements = request.form["requirements"] #role name, role info, resume & xp, company values, related passions, your experiences,
        scale = request.form["scale"]

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct", 
            prompt=generate_prompt(requirements, scale),
            temperature=1,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(requirements, scale):
    return """Generate a chord progression in the key of {} using the scale of {}.
Represent chords using the following format: [chord name][chord quality][inversion], where chord name can be [A-G], chord quality can be [maj, min, aug, dim], and inversion can be [1, 2, 3].

Example: Cmaj1

Please provide the chord progression in the following format:

[chord][chord][chord][chord]""".format(requirements, scale.capitalize())


# Assume the role of a Professional Cover Letter Writer - you will be writing a cover letter for [name].
#
#Generate a Cover Letter for the role of [role], which has the following requirements: [requirements].
#Your client, [name], has the following experiences, achievements, and resume info: [resume].
#


#flask not scalable...potential switch?

#Writing Cover Letters is hard. Get them done in minutes.