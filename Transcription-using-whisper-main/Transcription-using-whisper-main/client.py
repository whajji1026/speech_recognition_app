import requests

# server url
URL = "http://127.0.0.1:5000/transcribe"


# audio file 
FILE_PATH = "Transcription-using-whisper-main/records/record.mp3"


if __name__ == "__main__":

    # open files
    file = open(FILE_PATH, "rb")

    # package stuff to send and perform POST request
    values = {"file": (FILE_PATH, file, "audio.wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print("Predicted: {}".format(data["text"]))