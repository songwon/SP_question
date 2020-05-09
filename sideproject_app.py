from flask import Flask
app = Flask("my flask app")
from flask import render_template


@app.route("/home")
def home():
    return render_template("sideproject_p3.html")

@app.route("/intro")
def intro():
    return render_template("sideproject_p1.html")

@app.route("/Booklist")
def Booklist():
    return render_template("sideproject_p2.html")



app.run("0.0.0.0", port=5000, debug=True)