import speech_recognition as sr
from os import path
from pydub import AudioSegment

sound = AudioSegment.from_mp3("test.mp3")
sound.export('test.wav', format='wav')

AUDIO_FILE = 'test.wav'
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    print("Transcription:", r.recognize_google(audio))
