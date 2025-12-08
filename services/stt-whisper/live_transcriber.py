import queue
import sounddevice as sd
import numpy as np

from faster_whisper import WhisperModel

import scipy.io.wavfile as wav

model = WhisperModel("base", device="cuda", compute_type="float16")

q = queue.Queue()
samplerate = 16000

def callback(indata, frames, time, status):
    q.put(indata.copy())

print("Speak now (Ctrl+C to stop)")

with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
    buffer = []
    while True:
        data = q.get()
        buffer.append(data)

        if len(buffer) > 50: # 5 seconds
            audio = np.concatenate(buffer)
            wav.write("temp.wav", samplerate, audio)
            buffer = []

            segments, _ = model.transcribe("temp.wav")
            for seg in segments:
                print(seg.text)