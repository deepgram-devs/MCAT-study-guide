# MCAT-study-guide
Code for creating an MCAT study guide using Deepgram and GPT

Folders:

- audios - place the audios you wish to transcribe and summarize in here!

- outptus - contains the .json outputs of dg_transcribe.py

- summaries - contains the .txt outputs of summarize.py


Files:

- yt_dl.py - The file which takes in a list of YouTube video URLs and outputs an .mp3 download of each video's audio.

- dg_transcribe.py - Given a folder, all audio files of a specified mimetype will be transcribed. (API key needed)

- summarize.py - Given a long transcript from the output of dg_transcribe.py, 


To produce a summary of a YouTube video, run the above files in the order they are listed, filling in the appropriate parameters inside each file.
