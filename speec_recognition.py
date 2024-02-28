import speech_recognition as sr
AUDIO_FILE=("abhi.wav.wav")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
      audio=r.record(source)
try:
    print("speech recognized"+r.recognize_google(audio)
except sr.UnkownValueError:
    print("google sppech recognition couldn't understand")
except sr.RequestError:
    print("could get the result")
