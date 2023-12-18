import os
import json
import hashlib

def generate_cache_filename(video_url):
    video_id = hashlib.md5(video_url.encode('utf-8')).hexdigest()
    return f"{video_id}.json"

def check_cache(video_url, cache_folder):
    if not cache_folder:
        return None
    cache_filename = generate_cache_filename(video_url)
    cache_file_path = os.path.join(cache_folder, cache_filename)
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'r') as cache_file:
            return json.load(cache_file)
    return None

def save_to_cache(data, video_url, cache_folder):
    if not cache_folder:
        return
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)
    # print(f'Saving to cache at {cache_folder}...')
    cache_filename = generate_cache_filename(video_url)
    cache_file_path = os.path.join(cache_folder, cache_filename)
    with open(cache_file_path, 'w') as cache_file:
        json.dump(data, cache_file)