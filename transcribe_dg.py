from deepgram import Deepgram
import asyncio, json, os

'''
 Sign up at https://console.deepgram.com/signup
 to get an API key and 12,000 minutes
 for free!
'''
dg_key = os.environ.get('DG_KEY')
dg = Deepgram(dg_key)


'''
The most common audio formats and encodings we support 
include mp3, mp4, mp2, aac, wav, flac, pcm, m4a, ogg, opus, and webm,
So feel free to adjust the `MIMETYPE` variable as needed
'''
MIMETYPE = 'mp3'

#Note: You can use '.' if your audio is in the root
DIRECTORY = './audios'  


# Feel free to modify your model's parameters as you wish!
options = {
    "punctuate": True,
    "numerals":True,
    "model": 'general',
    "tier": 'nova'
}

# This function calls on the Deepgram model to transcribe
# every file in the `DIRECTORY` folder that ends with the 
# mimetype specified by `MIMETYPE`
def main():
    audio_folder = os.listdir(DIRECTORY)
    for audio_file in audio_folder:
        if audio_file.endswith(MIMETYPE):
          with open(f"{DIRECTORY}/{audio_file}", "rb") as f:
              source = {"buffer": f, "mimetype":'audio/'+MIMETYPE}
              res = dg.transcription.sync_prerecorded(source, options)
              with open(f"./{audio_file[:-4]}.json", "w") as transcript:
                  json.dump(res, transcript, indent=4)
    return

main()