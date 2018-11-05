import os
from flask import Flask, render_template, request, redirect, session, g, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("test-base.html")

@app.route('???', methods=["GET", "POST"])
def getuser():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.write(request.form["username"])
        return render_template("got-user.html")

    return render_template('test.html')

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), 
            debug = True)
# Code in here will only execute when the file is run directly (i.e. not in a test suite)
