from faster_whisper import WhisperModel

model = WhisperModel("base", device="cuda", compute_type="float16")

segments, info = model.transcribe("test.wav")

print("Language", info.language)

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")