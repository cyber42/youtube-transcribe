# YouTubeTranscribe Command Line Tool
A project to transcribe Youtube videos and podcasts.

## Overview
This tool transcribes YouTube videos using speech-to-text technology and provides a feature to cache transcriptions to avoid repeated processing.

## Replicate.com API Model
The tool uses the `meronym/speaker-transcription` model from replicate.com, which provides the following features:
- Transcribes English speech segments from an audio file.
- Identifies individual speakers and annotates the transcript with timestamps and speaker labels.
- Outputs global information about the number of detected speakers and an embedding vector for each speaker.

### Model Description
The model consists of two main components:
- A pre-trained speaker diarization pipeline from the pyannote.audio package.
- OpenAI’s Whisper model for English speech transcription.

### Run Time
It takes about 1 minute to transcribe a 4 minute video, which will incur fees on replicate.com.

## Installation Instructions
1. Clone the repository.
2. Install the dependencies using Python 3.12.0 with `pip install -r requirements.txt`.

## Usage Examples
Transcribe a video and output to stdout:
```
python main.py <YouTube-Video-URL> --api-key <Your-API-Key>
```
Transcribe a video and save to a file:
```
python main.py <YouTube-Video-URL> --output-file output.json --api-key <Your-API-Key>
```
Use a cache folder to avoid reprocessing:
```
python main.py <YouTube-Video-URL> --cache-folder ./cache --api-key <Your-API-Key>
```

## Documentation
The output format is a JSON object with metadata and transcription fields.

## Contributing
Contributions and pull requests to `youtube-transcribe` are welcome. Please ensure that your code adheres to the project's coding standards.

## Experimental Project
Tested how `gpt-engineer` works, based on the prompt file below.

Observations about `gpt-engineer`:
 - The resulted software is fully functional and it works on Python 3.12.0.
 - Does not generate much comments or docstrings, despite instructed.
 - Does not use typing despite instructed.
 - Used the wrong library first (used youtube-dl, which seems to have issues now)
 - Always generates the same project strucutre with a run.sh file trying to create environment locally.
 - Halicinated the likes attibute in meta data, which I removed manually.
 - Had small datetime / str type issue, which I fixed.
 - Despite having explaned the whole replicate API in the prompt, it regularly returns the transcription file path on the replicate.com server, instead of loading it up. I fixed this with an incremental modification prompt.
 - The README.md file was stopped being generated at it's half.

# THE COMPLETE PROMPT USED TO BUILD THIS REPO

PROJECT SPECIFICATION: YOUTUBETRANSCRIBE COMMAND LINE TOOL

GOALS
- Develop a command-line tool named `youtubetranscribe`.
- The tool transcribes YouTube videos using speech-to-text technology.
- Provides a feature to cache transcriptions to avoid repeated processing.

FEATURES
1. **Command Line Interface**:
   - **Primary Argument**: YouTube video link for transcription.
   - **Optional Arguments**:
     - `-o` or `--output-file`: Specifies output file destination. Defaults to stdout.
     - `-c` or `--cache-folder`: Sets a directory for caching transcribed files.
     - API Key and User Credentials: Specified on the command line if needed.
   - **Command Line Tool**:
     - Instead of only having a main.py file, the tool can be used on the command line with an executable named: `youtubetranscribe.py`
     - When `-o` and `--output-file` is omitted, the tool's output can be pipelined to the next command line too in the pipeline.

2. **Downloading Audio**:
   - Downloads the audio of the specified YouTube video to a temporary location.

3. **Transcription using Replicate.com API**:
   - Utilizes the `https://replicate.com/meronym/speaker-transcription` model for transcription with speaker diarization.
   - Requires an API key, specified via command line, environment variable, or env file.
   - Deletes the temporary audio file post-transcription.

4. **Metadata Download**:
   - Downloads metadata including title, upload date, channel, quality, views, and video length.

5. **Output Format**:
   - JSON format including fields:
     - `title`
     - `publication date`
     - `channel`
     - `quality`
     - `views`
     - `video length`
     - `transcription-text`

6. **Caching Mechanism**:
   - Saves transcriptions in the specified cache folder.
   - Cache filenames incorporate the video title and identifier.
   - If a video is already cached, skips download and transcription process.

DATA MODELS
1. **Video Metadata Model**:
   - Title: String
   - Publication Date: DateTime
   - Channel: String
   - Quality: String
   - Views: Integer
   - Video Length: Duration

2. **Transcription Model**:
   - Text: String

LIBRARIES USED
1. **pytube**:
   - Rely on pytube for loading any data from Youtube, avoid using youtube_dl
2. **replicate**:
   - Use it according to the API details in APPENDIX

SOFTWARE DOCUMENTATION
 1. **README.md** file with:
   - Summary
   - Installation instructions
   - Documentation, output format
   - Usage examples
 2. **Docstrings**:
   - Functions and classes should be documented
   - Use the typing module and type annotations

API DOCUMENTATION
- **Replicate.com API**:
  - Model: `meronym/speaker-transcription`
  - Description: Provides Whisper transcription with speaker diarization.
  - Authentication: Requires API key.
  - Endpoint: The specific endpoint for the transcription service.
  - Input: Audio file.
  - Output: Transcribed text with speaker separation.

USE CASES
1. **Transcribing a YouTube Video**:
   - User provides a YouTube video link.
   - The tool downloads the audio, transcribes it, and retrieves metadata.
   - Outputs data in JSON format.

2. **Using Cached Transcriptions**:
   - User requests transcription of a previously processed video.
   - The tool checks the cache and retrieves the stored transcription and metadata.

3. **Specifying Output Location**:
   - User specifies an output file path.
   - The tool writes the JSON output to the specified file.

APPENDIX, replicate.com documentation

Install the Python client:

pip install replicate

Next, copy your API token and authenticate by setting it as an environment variable:

export REPLICATE_API_TOKEN=<paste-your-token-here>

Find your API token in your account settings.

Then, run the model:

import replicate
output = replicate.run(
    "meronym/speaker-transcription:9950ee297f0fdad8736adf74ada54f63cc5b5bdfd5b2187366910ed5baf1a7a1",
    input={"audio": open("path/to/file", "rb")}
)
print(output)

To learn more, take a look at the guide to get started with Python.

Inputs
audio file
Audio file
prompt string
Optional text to provide as a prompt for each Whisper model call.
Output schema
This is the raw JSON schema describing the model's ouput structure.

{
  "type": "string",
  "title": "Output",
  "format": "uri"
}"

APPENDIX, The readme of the meronym/speaker-transcription model:

"Readme
This pipeline transcribes (English-only) speech segments from an audio file, identifies the individual speakers and annotates the transcript with timestamps and speaker labels. An optional prompt string can guide the transcription by providing additional context. The pipeline outputs additional global information about the number of detected speakers and an embedding vector for each speaker to describe the quality of their voice.

Model description
There are two main components involved in this process:

a pre-trained speaker diarization pipeline from the pyannote.audio package (also available as a stand-alone diarization model without transcription):

pyannote/segmentation for permutation-invariant speaker segmentation on temporal slices
speechbrain/spkrec-ecapa-voxceleb for generating speaker embeddings
AgglomerativeClustering for matching embeddings across temporal slices
OpenAI’s whisper model for general-purpose English speech transcription (the medium.en model size is used for a good balance between accuracy and performance).

The audio data is first passed in to the speaker diarization pipeline, which computes a list of timestamped segments and associates each segment with a speaker. The segments are then transcribed with whisper.

Input format
The pipeline uses ffmpeg to decode the input audio, so it supports a wide variety of input formats - including, but not limited to mp3, aac, flac, ogg, opus, wav.

The prompt string gets injected as (off-screen) additional context at the beginning of the first Whisper transcription window for each segment. It won’t be part of the final output, but it can be used for guiding/conditioning the transcription towards a specific domain.

Output format
The pipeline outputs a single output.json file with the following structure:

{
  "segments": [
    {
      "speaker": "A",
      "start": "0:00:00.497812",
      "stop": "0:00:09.762188",
      "transcript": [
        {
          "start": "0:00:00.497812",
          "text": " What are some cool synthetic organisms that you think about, you dream about?"
        },
        {
          "start": "0:00:04.357812",
          "text": " When you think about embodied mind, what do you imagine?"
        },
        {
          "start": "0:00:08.017812",
          "text": " What do you hope to build?"
        }
      ]
    },
    {
      "speaker": "B",
      "start": "0:00:09.863438",
      "stop": "0:03:34.962188",
      "transcript": [
        {
          "start": "0:00:09.863438",
          "text": " Yeah, on a practical level, what I really hope to do is to gain enough of an understanding of the embodied intelligence of the organs and tissues, such that we can achieve a radically different regenerative medicine, so that we can say, basically, and I think about it as, you know, in terms of like, okay, can you what's the what's the what's the goal, kind of end game for this whole thing? To me, the end game is something that you would call an"
        },
        {
          "start": "0:00:39.463438",
          "text": " anatomical compiler. So the idea is you would sit down in front of the computer and you would draw the body or the organ that you wanted. Not molecular details, but like, here, this is what I want. I want a six legged, you know, frog with a propeller on top, or I want I want a heart that looks like this, or I want a leg that looks like this. And what it would do if we knew what we were doing is put out, convert that anatomical description into a set of stimuli that would have to be given to cells to convince them to build exactly that thing."
        },
        {
          "start": "0:01:08.503438",
          "text": " Right? I probably won't live to see it. But I think it's achievable. And I think what that if, if we can have that, then that is basically the solution to all of medicine, except for infectious disease. So birth defects, right, traumatic injury, cancer, aging, degenerative disease, if we knew how to tell cells what to build, all of those things go away. So those things go away, and the positive feedback spiral of economic costs, where all of the advances are increasingly more"
        },
      ]
    }
  ],
  "speakers": {
    "count": 2,
    "labels": [
      "A",
      "B"
    ],
    "embeddings": {
      "A": [<array of 192 floats>],
      "B": [<array of 192 floats>]
    }
  }
}