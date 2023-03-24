from flask import Flask, request, jsonify
# from api.functions import process_audio_file
from werkzeug.wrappers import request as werkzeug_request
import os
import whisper

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to Feel app"

@app.route('/transcribe', methods=['POST'])

def transcribe():

    audio_file = request.files['file']
    audio_file.save("audio.wav")
    model = whisper.load_model("medium")
    result=model.transcribe(audio_file)
    # num_speakers=2
    # model_size="large"

    # transcript=process_audio_file(audio_file, model_size, num_speakers)
    os.remove("audio.wav")

    return jsonify({'transcript': result['text']})




if __name__ == "__main__":
    app.run(debug=False)

















    #     with contextlib.closing(wave.open("temp_audio.wav", 'r')) as f:
    #     frames = f.getnframes()
    #     rate = f.getframerate()
    #     duration = frames / float(rate)

    # audio = Audio()
    # embedding_model = PretrainedSpeakerEmbedding(
    #     "speechbrain/spkrec-ecapa-voxceleb",
    #     device=torch.device("cuda"))

    # segments = cluster_speakers("temp_audio.wav", result, 2, audio, embedding_model, duration)

    # transcript = ""
    # for (i, segment) in enumerate(segments):
    #     if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
    #         transcript += "\n" + segment["speaker"] + ' ' + str(datetime.timedelta(seconds=round(segment["start"]))) + '\n'
    #     transcript += segment["text"][1:] + ' '