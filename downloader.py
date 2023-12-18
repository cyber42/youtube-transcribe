from pytube import YouTube
import tempfile
import os

def download_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    temp_dir = tempfile.mkdtemp()
    audio_file_path = audio_stream.download(output_path=temp_dir)
    return audio_file_path