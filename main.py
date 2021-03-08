import csv
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "amanda"
# app.permanent_session_lifetime = timedelta(minutes=20)


@app.route("/")
def home():
    return render_template("index.html")

    # if request.method == "POST":
    #     session.permanent = True
    #     # name = request.form["name"]
    #     test = request.form["test"]
    #     session["user"] = user
    #     #
    #     # fieldnames = ["name", "test"]
    #     #
    #     # with open("pycharmprojects/mie237-project/data.csv", "a") as inFile:
    #     #     writer = csv.DictWriter(inFile, fieldnames=fieldnames)
    #     #     writer.writerow({"name": name, "test": test})
    #     # return redirect(url_for("user"))
    # else:
    #     return render_template("test.html")

@app.route("/test", methods=["POST", "GET"])
def test():
    questions = ["question 1 ", "question 2"]
    return render_template("test.html", content=questions)

# @app.route("/scores")
# def scores():





@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

# @app.route("/submitted")
# def done():
#     session.pop("user", None)
#     flash("You've finished the assessment")
#     return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host ='0.0.0.0')