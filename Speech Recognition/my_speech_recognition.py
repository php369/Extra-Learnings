# Simple example to convert speech to text using Python

# Using audio file as source
import speech_recognition as sr

file = ("S:/Programming Practice/Speech Recognition/Audio.wav")

# Initializing the recognizer
r = sr.Recognizer()

# Reading the audio file
with sr.AudioFile(file) as source:
    audio = r.record(source)

# Outputting the audio file into text
try:
    print("Audio file contains the following text: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognizer failed to recognize")
except sr.RequestError:
    print("Unable to fetch the data from Google Speech Recognizer")