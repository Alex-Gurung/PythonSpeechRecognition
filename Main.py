import speech_recognition as sr #Comment out the parts that you don't want to run
from geopy.geocoders import Nominatim
import forecastio
#Setup speech
r = sr.Recognizer()

#with sr.Microphone() as source:
#	print("Say something!")
#	audio = r.listen(source)
#try:
#    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#except sr.UnknownValueError:
#    print("Google Speech Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#This is code necessary for it to start listening for input
'''with sr.Microphone() as source:
	print("What is your name?")
	audio = r.listen(source)

#Below are the try and except blocks for google speech recognition \
try:
	name = r.recognize_google(audio)
	print("Hello, %s, my name is Ultron." % name)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))'''

#This is code necessary for it to start listening for input
with sr.Microphone() as source:
	print("Where do you live(Weather)?:") #Input should be in the form of address + zipcode, as otherwise the resulting location may be wrong
	audio = r.listen(source)

geolocater = Nominatim()
#geolocater = GeocoderDotUS(format_string="%s, Herndon VA")
#Below are the try and except blocks for google speech recognition
try:
	place = r.recognize_google(audio)
	print(place)
	location = geolocater.geocode(place)
	lat = location.latitude
	print ("Latidude: %s" % lat)
	long = location.longitude
	print ("Longitude: %s" % long)
	api_key = "161ff436ccbe7edb13357271e3462ae6" #Free from http://developer.forecast.io
	forecast = forecastio.load_forecast(api_key, lat, long)
	byHour = forecast.hourly()
	print (byHour.summary.encode('utf8'))
	print "Icon" + byHour.icon
	print "Temperatures: "
	for hourlyData in byHour.data:
		print hourlyData.temperature
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
