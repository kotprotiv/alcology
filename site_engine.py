from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    html = '''<iframe width="420" height="315"
            src="https://www.youtube.com/embed/M-XtB0R3ri4">
            </iframe>'''
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0')