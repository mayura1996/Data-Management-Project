import requests, json

def getData(latitude,longitude):
	api_key = "45e9292ce7650f91dee4f30b642c87df"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"


	lat=latitude
	lon=longitude

	# Start_Lat
	# Start_Lng
	# Temperature(F)
	# Humidity(%)
	# Pressure(in)
	# Wind_Speed(mph)
		# instance = [[ 3.03697120e+01, -32.08479140e+01,  10.11000000e+01,  18.40000000e+01,
		# 1.51094556e+08,  1.77802993e+00]]


	complete_url = base_url + "appid=" + api_key + "&lat=" + str(lat) + "&lon=" + str(lon)


	response = requests.get(complete_url)

	x = response.json()

	if x["cod"] != "404":

		y = x["main"]

		current_temperature = y["temp"]

		current_pressure = y["pressure"]
		# pressureIN = int(current_pressure)/
		current_humidity = y["humidity"]

		z = x["weather"]

		weather_description = z[0]["description"]

		print(" Temperature (in kelvin unit) = " +
						str(current_temperature) +
			"\n atmospheric pressure (in hPa unit) = " +
						str(current_pressure) +
			"\n humidity (in percentage) = " +
						str(current_humidity) +
			"\n wind speed = " +
						str(x["wind"]["speed"]))

		temperature = float(current_temperature) * 1.8 - 459.67
		pressure = float(current_pressure)*0.02953
		humidity = float(current_humidity)
		windSpeed=float(x["wind"]["speed"])*2.23694

		print(" Temperature (in Farenheit unit) = " +
					str(temperature) +
		"\n atmospheric pressure (in inches) = " +
					str(pressure) +
		"\n humidity (in percentage) = " +
					str(humidity) +
		"\n wind speed = " +
					str(windSpeed))

		return lat,lon,temperature,pressure,humidity,windSpeed
	else:
		print(" City Not Found ")

