import openai
import json, os
import time as t

API_KEY = os.environ.get('OPEN_AI_KEY')
PREFIX = "phone_call"
FILENAME = "./results/" + PREFIX + ".json"
CHUNK_SIZE = 500

def get_transcription(transcription_file):
    with open(transcription_file, "r") as file:
        data = json.load(file)
        result = data['text']
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

def main(filename):
    start = t.time()
    #Initialization
    openai.api_key = API_KEY
    print("Currently summarizing ", FILENAME)
    print()

    #summarization call
    transcription = get_transcription(FILENAME)
    tokens = transcription.split()

    chunks = get_chunks(tokens)

    # Count tokens: Token package (Sandra) - tiktoken
    # Example prompt: Give an example body and output for a summary!! Absolutely flawless!!!!!

    transcrption_file = './summaries/' + PREFIX + "c" + ".txt"
    with open(transcrption_file, "w") as outfile:
        for chunk in chunks:
            content = "Summarize the following text in thirty words or fewer: " + ' '.join(chunk)
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

    speed = t.time() - start

    print("Seconds to complete: ", speed)
    print("🥳 We did it! 🥳")


main(FILENAME)