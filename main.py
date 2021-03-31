import csv
from flask import Flask, redirect, url_for, render_template, request, Response, g
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    start = datetime.now().strftime("%H:%M:%S")
    return render_template("test.html", start=start)


@app.route("/handle_data", methods=['POST'])
def handle_data():
    score = 0
    start = request.form.get('start')
    end = datetime.now().strftime("%H:%M:%S")
    if request.form.get('a1', type=float) == 0.25: score +=1
    if request.form.get('a2', type=float) == 0.14: score +=1
    if request.form.get('a3', type=float) == 16: score +=1
    if request.form.get('a4', type=float) == 0.27: score +=1
    if request.form.get('a5', type=float) == 0.78: score +=1

    return 'Please copy and paste the bolded line into an email ' \
           'and send it to ' \
           '<em>amandacynthia.chow@mail.utoronto.ca. </em>' \
           'And then you are all finished! Thanks again for your participation. </p>' \
           '<br>' \
           '<b>Score: {},  Start time: {},  End time: {}</b>'.format(score, start, end)



if __name__ == "__main__":
    app.run()
    print(handle_data)

