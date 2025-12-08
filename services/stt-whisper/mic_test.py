import sounddevice as sd
import scipy.io.wavfile as wav

fs = 16000
print("Recording for 5 seconds")

recording = sd.rec(int(5*fs), samplerate=fs, channels=1)

sd.wait()
wav.write("test.wav", fs, recording)
print("Saved test.wav")