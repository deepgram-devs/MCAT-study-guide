# MCAT-study-guide
Code for creating an MCAT study guide using Deepgram and GPT. If you'd like to see a video tutorial explaining the structure of this code and showcasing a demo of this code, check out [this link](https://www.youtube.com/watch?v=ybelIFV0aj8)

<img width="637" alt="Screen Shot 2023-06-06 at 7 25 24 AM" src="https://github.com/deepgram-devs/MCAT-study-guide/assets/57232352/e7bad18a-768e-4c87-91f7-baffd638593f">

**Folders**:

- `audios` - place the audios you wish to transcribe and summarize in here! By default, the starter code comes with a phone call audio (`phone_call.m4a`) that you can transcribe and summarize just to test out the code.

- `outptus` - contains the .json outputs of dg_transcribe.py

- `summaries` - contains the .txt outputs of summarize.py

**Files**:

- `yt_dl.py` - The file which takes in a list of YouTube video URLs and outputs an .mp3 download of each video's audio.

- `dg_transcribe.py` - Given a folder, all audio files of a specified mimetype will be transcribed. (API key needed. To get one, sign up for Deepgram [here](https://dpgr.am/youtube))

- `summarize.py` - Given a long transcript from the output of `dg_transcribe.py`, 


To produce a summary of a YouTube video, run the above files in the order they are listed, filling in the appropriate parameters inside each file. As a quick overview, here is how the code works (Illustrated below)

Given an audio file, Deepgram's latest AI Nova (top left) will transcribe it. The result will be a JSON output (bottom left) containing a full transcript of the audio with word-level timestamps. This transcript is then passed into ChatGPT's API (bottom right) to yield a summary (top right), which is then printed into a file that will be located in the `summaries` folder.


<img width="1425" alt="Screen Shot 2023-06-06 at 7 26 51 AM" src="https://github.com/deepgram-devs/MCAT-study-guide/assets/57232352/b6c649d5-6bb0-41f4-b2a8-d1f866f8d73a">
