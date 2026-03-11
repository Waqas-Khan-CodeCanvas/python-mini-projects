# # pip install vosk soundfile

# import vosk
# import soundfile as sf
# import json

# # ------------------ CONFIG ------------------
# model_path = r"C:\Users\waqas\Desktop\ctk\vosk-model-small-en-us-0.15"
# audio_file = "output.mp3"
# output_text_file = "output.txt"
# # -------------------------------------------

# # Load Vosk model
# model = vosk.Model(model_path)

# # Open audio file
# data, samplerate = sf.read(audio_file)
# if len(data.shape) > 1:  # Convert to mono if stereo
#     import numpy as np
#     data = data.mean(axis=1)

# # Initialize recognizer
# rec = vosk.KaldiRecognizer(model, samplerate)

# # Process audio in chunks
# for i in range(0, len(data), 4000):
#     chunk = data[i:i+4000].tobytes()
#     rec.AcceptWaveform(chunk)

# # Get final result
# final_result = json.loads(rec.FinalResult())
# recognized_text = final_result.get('text', '')

# # Save to text file
# with open(output_text_file, 'w', encoding='utf-8') as f:
#     f.write(recognized_text)

# print(f"Transcription saved to {output_text_file}")
# print("Recognized Text:", recognized_text)



# pip install vosk pydub numpy

import vosk
from pydub import AudioSegment
import numpy as np
import json

# ------------------ CONFIG ------------------
model_path = r"C:\Users\waqas\Desktop\ctk\vosk-model-small-en-us-0.15"
audio_file = "output.mp3"
output_text_file = "output.txt"
# -------------------------------------------

# Load Vosk model
model = vosk.Model(model_path)

# Convert MP3 to WAV in memory
audio = AudioSegment.from_mp3(audio_file)
audio = audio.set_channels(1).set_frame_rate(16000)  # mono 16kHz
samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

# Convert to 16-bit PCM bytes
samples = (samples * 32767).astype(np.int16).tobytes()

# Initialize recognizer
rec = vosk.KaldiRecognizer(model, 16000)

# Process audio in chunks
chunk_size = 4000
for i in range(0, len(samples), chunk_size):
    rec.AcceptWaveform(samples[i:i+chunk_size])

# Get final result
final_result = json.loads(rec.FinalResult())
recognized_text = final_result.get('text', '')

# Save to text file
with open(output_text_file, 'w', encoding='utf-8') as f:
    f.write(recognized_text)

print(f"Transcription saved to {output_text_file}")
print("Recognized Text:", recognized_text)
