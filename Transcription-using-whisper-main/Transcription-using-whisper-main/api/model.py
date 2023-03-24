

import whisper
import pickle

model = whisper.load_model("medium")
pickle.dump(model,open('srmodel.pkl','wb'))

