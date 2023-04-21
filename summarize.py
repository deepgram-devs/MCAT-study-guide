import openai
import json, os

API_KEY = os.environ.get('OPEN_AI_KEY')
FOLDER = './jsons'

 # Arbitrarily chosen hyperparameter
CHUNK_SIZE = 500

def get_transcription(transcription_file):
    with open(transcription_file, "r") as file:
        data = json.load(file)
        result = data["results"]["channels"][0]["alternatives"][0]["transcript"]
        return result

def get_chunks(tokens):
    result = []
    start = 0
    end = CHUNK_SIZE if CHUNK_SIZE < len(tokens) else len(tokens)
    while end < len(tokens):
        result.append(tokens[start:end])
        start = end + 1
        end = end + CHUNK_SIZE if end + CHUNK_SIZE < len(tokens) else len(tokens)
    return result

def main(folder_name):
    #Initialization
    openai.api_key = API_KEY

    folder = os.listdir(folder_name)

    for file in folder:
        #summarization call
        transcription = get_transcription(folder_name + '/' + file)
        tokens = transcription.split()
        title = os.path.splitext(file)[0]
        chunks = get_chunks(tokens)

        # We summarize the transcription `CHUNK_SIZE` words at a time.
        transcrption_file = './summaries/' + title + ".txt"
        with open(transcrption_file, "w") as outfile:
            for chunk in chunks:
                content = "Summarize the following text in three sentences or fewer: " + ' '.join(chunk)
                json_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": content}
                        ]
                    )
                # write results
                outfile.write(json_response["choices"][0]["message"]["content"])
                outfile.write('\n')

    print("🥳 We did it! 🥳")
    print("Different runs of this code will produce different summaries of varying quality.")


main(FOLDER)