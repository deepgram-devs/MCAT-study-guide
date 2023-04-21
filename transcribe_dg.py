from deepgram import Deepgram
import asyncio, json, os

DEEPGRAM_API_KEY = os.environ.get('DG_KEY')
PREFIX = "phone_call"
FILENAME = "../audios/" + PREFIX + ".m4a"
PARAMS = {'punctuate': True, 'diarize':True, 'tier': 'enhanced', 'model':'whisper'}

async def main():

    # Initialization
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    print("Currently transcribing ", FILENAME)

    # start transcribing
    with open(FILENAME, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = await deepgram.transcription.prerecorded(source, PARAMS)
        print(response)
        json_object = json.dumps(response, indent=4)

    # write results
    transcrption_file = './data_dg/' + PREFIX + '.json'
    with open(transcrption_file, "w") as outfile:
      outfile.write(json_object)
    
    print("Bag secured 💰😤💪")

asyncio.run(main())




