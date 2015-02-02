from flask import Flask, abort, jsonify
from codecs import decode
from YouTube.Subtitles import Subtitles

import requests
import xmltodict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/subtitlesText/<video_id>')
def subtitlesText(video_id):
    subs = Subtitles()
    subtitles = subs.get_subtitles(video_id)
    subtitles_dict =  xmltodict.parse(str(subtitles))
    return jsonify(subtitles_dict)

@app.route('/api/subtitlesURL/<video_id>')
def subtitlesURL(video_id):
    subs = Subtitles()
    subtitles = subs.get_subtitles_url(video_id)
    return subtitles

if __name__ == '__main__':
    app.debug = True
    app.run()

