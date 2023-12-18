import sys
from cli import parse_arguments
from downloader import download_audio
from transcriber import transcribe_audio
from metadata import fetch_metadata
from cache import check_cache, save_to_cache
from models import Transcription, VideoMetadata
from utils import output_to_file_or_stdout

def main():
    args = parse_arguments(sys.argv[1:])

    # Check cache first
    cached_data = check_cache(args.video_url, args.cache_folder)
    if cached_data:
        output_to_file_or_stdout(cached_data, args.output_file)
        return

    # Download audio and fetch metadata
    # print(f'Fetching metadata from {args.video_url}...')    
    metadata = fetch_metadata(args.video_url)
    # print(f'Downloading audio from "{metadata["title"]}"...')
    audio_file_path = download_audio(args.video_url)

    # Transcribe audio
    # print(f'Transcribing audio from "{audio_file_path}"...')
    transcription_text = transcribe_audio(audio_file_path, args.api_key)

    # Create models
    transcription = Transcription(text=transcription_text)
    video_metadata = VideoMetadata(
        title=metadata['title'],
        publication_date=metadata['publication_date'],
        channel=metadata['channel'],
        quality=metadata['quality'],
        views=metadata['views'],
        video_length=metadata['video_length']
    )

    # Combine data
    output_data = {
        "metadata": video_metadata.to_dict(),
        "transcription": transcription.to_dict()
    }

    # Save to cache and output
    save_to_cache(output_data, args.video_url, args.cache_folder)
    output_to_file_or_stdout(output_data, args.output_file)

if __name__ == "__main__":
    main()