import requests
from dotenv import load_dotenv
import os
import datetime
from twilio.rest import Client
from send_sms import mess


load_dotenv()
city_name = os.environ['city_name']
api_key = os.environ['api_key']
lat = os.environ['lat']
lng = os.environ['lng']

# extracting current date_time

now = datetime.datetime.now()
current_hour = now.hour
print(f"the current hour is -------------> {current_hour}\n Hitting rain API")

parameter = {
    "lat" : lat, "lon": lng, "appid" : api_key,
    "exclude" : "current,minute,daily,minutely"
}
# print(f"the latitude ---------->{lat} \n\n longititude----------> {lng}")
# weather_api = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
# weather_api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}")

weather_api = "https://api.openweathermap.org/data/2.5/onecall"

data = requests.get(url=weather_api, params=parameter)

data = data.json()

# rain_count = 0

# for i in range(0,24):
#     test = data['hourly'][i]["weather"]
#     print(test)

test = data['hourly'][current_hour]["weather"]
condition = str(test[0]['id'])
print(condition)
if int(condition) < 700:
    print("its Raining")
    mess(body="its raining at this time please bring umbrella")


# data = weather_api.json()
# print(data)

#api_result_example
# {'coord': {'lon': 77.2491, 'lat': 28.6694}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}, 
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'base': 'stations',
#  'main': {'temp': 307.29, 'feels_like': 313.68, 'temp_min': 307.29, 'temp_max': 307.29, 'pressure': 999, 'humidity': 55}, 'visibility': 4000, 
#  'wind': {'speed': 2.57, 'deg': 120}, 'rain': {'1h': 2.2}, 'clouds': {'all': 75}, 'dt': 1659951668, 
# 'sys': {'type': 1, 'id': 9165, 'country': 'IN', 'sunrise': 1659917768, 'sunset': 1659965839}, 
# 'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}