import queue
import sounddevice as sd
import numpy as np
from TTS.api import TTS
import pyttsx3
from faster_whisper import WhisperModel
import soundfile as sf

import scipy.io.wavfile as wav

model = WhisperModel("base", device="cuda", compute_type="float16")
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
tts = pyttsx3.init()
tts.setProperty("rate", 170)
fs = 16000
seconds = 5

print("Speak now...")
audio = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait()

wav.write("user.wav", fs, audio)

segments, info = model.transcribe("user.wav")
text = ""
for segment in segments:
    text += segment.text


print("You said:", text)

# tts.tts_to_file(text=text, file_path="reply.wav")
print("Speaking back...")
# sd.play(sd.read("reply.wav"), fs)
# sd.wait()

tts.say(text)
tts.runAndWait()
