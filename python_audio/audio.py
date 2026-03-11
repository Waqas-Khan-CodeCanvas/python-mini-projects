# # Step 1: Install gTTS if you haven't already
# # pip install gTTS

# from gtts import gTTS
# import os

# # Input text
# text = input("Enter the text you want to convert to audio: ")

# # Create gTTS object
# tts = gTTS(text=text, lang='en')  # you can change 'en' to other supported languages

# # Save the audio file
# audio_file = "output.mp3"
# tts.save(audio_file)

# # Play the audio (works on Windows)
# os.system(f'start {audio_file}')

# print(f"Audio saved as {audio_file}")


import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 120)     # Speed of speech
engine.setProperty('volume', 1.5)   # Volume (0.0 to 1.0)

# Choose voice (Windows example)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for first voice, 1 for another

# Input text
text = "In a quiet village where the sky brushes the fields in hues of gold, young Mia discovered a map leading to forgotten treasures. Little did she know, her cat Whiskers had a secret: he was the guardian of the map, tasked with guiding Mia to not only the treasure but also to her destiny."

# Generate speech
engine.say(text)
engine.runAndWait()

# Optional: Save to file
engine.save_to_file(text, 'output.mp3')
# engine.runAndWait()
