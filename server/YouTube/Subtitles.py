import requests
import urllib

class Subtitles:

    youtube_url_base = 'http://www.youtube.com/watch?v='
    
    session = None

    def __init__(self):
        self.session = requests.session()
        self.session.proxies = urllib.getproxies()
        print self.session

    def get_subtitles_url(self, video_id):
        video_page_source = self.session.get(self.youtube_url_base + video_id)        
        subtitles_url = video_page_source.text.split('''TTS_URL': "''')
        subtitles_url = subtitles_url[1].split('",')[0]
        subtitles_url = subtitles_url.replace('\\', '').replace('u0026', '&').replace('&caps=asr', '')
        subtitles_url += '&caps=asr&type=track&fmt=1&name&lang=en&key=yttt1&kind=asr'
        return subtitles_url
    
    def get_subtitles(self, video_id):
        subtitles_url = self.get_subtitles_url(video_id)
        print subtitles_url
        return self.session.get(subtitles_url).text
