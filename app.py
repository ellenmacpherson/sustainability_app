# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    quotes = ["the greatest threat to our planet is the belief that someone else will save it",
    "there is no such thing as ‘away’. When we throw anything away it must go somewhere",
    "we cannot solve our problems with the same thinking we used when we created them",
    "if it can’t be reduced, reused, repaired, rebuilt, refurbished, refinished, resold, recycled, or composted, then it should be restricted, designed or removed from production",
    "we are living on this planet as if we had another one to go to",
    "often when you think you’re at the end of something, you’re at the beginning of something else"]
    randomNumber = randint(0, len(quotes)-1)
    quote = quotes[randomNumber]
    return render_template("index.html", random_quote=quote, **locals())

@app.route("/<name>")
def hello_someone(name):
   return render_template("index.html", name=name.title())

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")


@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result = "Great! You're on our mailing list."
    return render_template("confirmation.html", title="Confirmation", **locals())

# @app.route("/", methods=["POST"])
# def home_confirmation():
#     form_data = request.form
#     email = form_data["email"]
#     result = "Great! You're on our mailing list."
#     return render_template("confirmation.html", title="Confirmation", **locals())


if __name__ == '__main__':
    app.run(debug=True)
