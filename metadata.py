from pytube import YouTube
from datetime import datetime

def fetch_metadata(video_url):
    yt = YouTube(video_url)
    return {
        'title': yt.title,
        'publication_date': str(yt.publish_date),
        'channel': yt.author,
        'quality': yt.streams.get_highest_resolution().resolution,
        'views': yt.views,
        'video_length': yt.length
    }