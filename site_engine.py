from flask import Flask, render_template, request
import requests
from youtube_search import youtube_search

api_key = 'AIzaSyCwO8iVRlarbi_7S7ZR9KQBvGItRcqAFrw'
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/contacts/")
def contacts():
    return render_template('contacts.html')


@app.route("/cats/")
def cats():
    return render_template('cats.html')


@app.route("/cats_search/", methods=["POST"])
def cats_search(): 
    video_url = youtube_search(request.form.get('search_text'))
    video_1 = video_url[0]
    video_2 = video_url[1]
    video_3 = video_url[2]
    video_4 = video_url[3]
    video_5 = video_url[4]
    return render_template('cats_search.html', video_1=video_1, video_2=video_2, video_3=video_3, video_4=video_4, video_5=video_5)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
