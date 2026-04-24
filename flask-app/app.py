from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app deployed automatically by Jenkins! Webhook triggered the build and deployment process."