import argparse

def parse_arguments(args):
    parser = argparse.ArgumentParser(description='Transcribe YouTube videos using speech-to-text technology.')
    parser.add_argument('video_url', help='YouTube video link for transcription.')
    parser.add_argument('-o', '--output-file', help='Specifies output file destination.', default=None)
    parser.add_argument('-c', '--cache-folder', help='Sets a directory for caching transcribed files.', default=None)
    parser.add_argument('--api-key', help='API key for the transcription service.', required=True)
    return parser.parse_args(args)