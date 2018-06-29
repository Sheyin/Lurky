# These functions will be making external API calls using requests
# Much of this will be from the requests documentation as I learn how to use it.

import requests
import datetime
from secret import openWeatherMapKey

zipCode = 61801

# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&APPID={APIKEY}
# Only send 1 request every 10 min at most

#requestText = 'https://api.openweathermap.org/data/2.5/weather?zip=' + zipCode + ',us&APPID=' + openWeatherMapKey

def main():
	r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=' + str(zipCode) + ',us&APPID=' + str(openWeatherMapKey))

	print('json: ')
	print(r.json())

	currentTime = datetime.datetime.now().time()
	print("The current time is: " + str(currentTime) + ", don't make another request until late least ten minutes.")



	# Store so I can use data locally instead of constantly making api calls while tweaking
	api_result = open("result.txt", "w")
	api_result.write(str(r.json())
	#api_result.close()
	#print('text: ')
	#print(r.text)

	temperatures = r["main"]
	currentTempKelvin = temperatures["temp"]
	currentTemp = currentTempKelvin * (9/5) - 459.67
	print(currentTemp)

	print("The weather in " + r["name"] + " is " + r["weather"]["main"] + " and " + r["weather"]["description"] + ". The temperature will be a low of... ")
