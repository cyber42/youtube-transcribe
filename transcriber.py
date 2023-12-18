import replicate
import os
import requests

# def transcribe_audio(audio_file_path, api_key):
#     os.environ['REPLICATE_API_TOKEN'] = api_key
#     output = replicate.run(
#         "meronym/speaker-transcription:9950ee297f0fdad8736adf74ada54f63cc5b5bdfd5b2187366910ed5baf1a7a1",
#         input={"audio": open(audio_file_path, "rb")}
#     )
#     os.remove(audio_file_path)  # Delete the temporary audio file
#     return output


def fetch_transcription_text(url):
    """
    Fetches the transcription text from the temporary file URL provided by the replicate.com API.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()

def parse_transcription_json(transcription_json):
    """
    Parses the JSON content to extract the transcription text.
    """
    segments = transcription_json.get('segments', [])
    transcription_text = ''
    for segment in segments:
        for transcript in segment.get('transcript', []):
            transcription_text += transcript.get('text', '') + ' '
    return transcription_text.strip()

def transcribe_audio(audio_file_path, api_key):
    """
    Transcribes the audio file using the replicate.com API and returns the transcription text.
    """
    replicate.api_token = api_key
    model = "meronym/speaker-transcription:9950ee297f0fdad8736adf74ada54f63cc5b5bdfd5b2187366910ed5baf1a7a1"
    with open(audio_file_path, "rb") as audio_file:
        transcription = replicate.run(model, input={"audio": audio_file})
    
    os.remove(audio_file_path)  # Delete the temporary audio file

    # Fetch the transcription text from the temporary file URL
    transcription = fetch_transcription_text(transcription)
    # transcription = parse_transcription_json(transcription)
    
    return transcription