import csv
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "amanda"
# app.permanent_session_lifetime = timedelta(minutes=20)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    questions = ["1. An allergist claims that 50% of the patients she tests are allergic to some type of weed. "
                 "What is the probability that exactly 3 of her next 4 patients are allergic to weeds? "
                 "(Please round your answer to 2 d.p.) ",
                 "2. A pair of fair dice is tossed. Find the probability of getting a roll with a total of 8. "
                 "(Please round your answer to 2 d.p.) ",
                 "3. The length of time for one individual to be served at a cafeteria is a random variable having "
                 "an exponential distribution with a mean of 4 minutes. What is the variance of this distribution?  "
                 "(Please round your answer to 2 d.p.) ",
                 "4. The probability that a doctor correctly diagnoses a particular illness is 0.7. Given that "
                 "the doctor makes an incorrect diagnosis, the probability that the patient files a lawsuit is 0.9. "
                 "What is the probability that the doctor makes an incorrect diagnosis and the patient sues? "
                 "(Please round your answer to 2 d.p.) ",
                 "5. The waiting time, in minutes, between successive speeders spotted by a radar unit is a continuous "
                 "random variable with CDF F(x) = 1 − e^(−0.5x), x ≥ 0. (0 otherwise)  Find the probability of waiting "
                 "less than 3 minutes between successive speeders. (Please round your answer to 2 d.p.) "]
    return render_template("test.html", questions=questions)


@app.route("/handle_data", methods=['POST'])
def handle_data():
    answer = request.form["answer[]"]
    return answer




if __name__ == "__main__":
    app.run(host ='0.0.0.0')