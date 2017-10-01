from flask import Flask
from flask import request
import requests
from youtube_search import youtube_search

api_key = 'AIzaSyCwO8iVRlarbi_7S7ZR9KQBvGItRcqAFrw'
app = Flask(__name__)


@app.route("/")
def index():
    html = '''
            <!DOCTYPE HTML>
            <html>
             <head>
              <meta charset="utf-8">
              <title>Поиск видео на YouTube</title>
             </head>
             <body>
              <p><b>Как насчет немного видео с котятами?</b><br>
              </p>
            
             </body>
            </html>
                '''
    text = 'Котята'
    video_url = youtube_search(text)
    for url in video_url:
        html +=  '''<iframe width="420" height="315"
                    src="{}">
                    </iframe><br>'''.format(url)
    html += '</body></html>'
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)