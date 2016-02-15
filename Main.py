import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


with sr.Microphone() as source:
	print("What is your name?")
	audio = r.listen(source)

name = r.recognize_google(audio)
if (name.lower() == "jarvis"):
	print("Hello, Jarvis. Time for you to die.")
else:
	print("Hello, %s, my name is Ultron." % name)