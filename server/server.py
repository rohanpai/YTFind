from flask import Flask, abort
from codecs import decode
from YouTube.Subtitles import Subtitles

import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/subtitles/<video_id>')
def subtitles(video_id):
    subs = Subtitles()
    subtitles = subs.get_subtitles_url(video_id)
    return subtitles

if __name__ == '__main__':
    app.debug = True
    app.run()

