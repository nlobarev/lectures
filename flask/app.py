from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/hello/<string:name>")
def hello(name):
    name = name.capitalize()
    return render_template("hello.html", name=name)
