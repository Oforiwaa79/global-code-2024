# import pyowm

# owm = pyowm.OWM('e54f5105f74d4c5f4bf3dbeba4a1f7b5')
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('London,uk')
# w = observation.weather

# print(w.wind())
# print(w.humidity)


from pprint import pprint
import requests
api_key = "e54f5105f74d4c5f4bf3dbeba4a1f7b5"
location = input("Enter your current location: ")

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}')
 
if r.status_code == 200:
    #pprint(r.json())

    print(f"Hi! Your coordinate is latitude:{r.json()['coord']['lat']} and longitude:{r.json()['coord']['lon'],}")
    print(f"Feels like: {r.json()['main']['feels_like']} \nGround level: {r.json()['main']['grnd_level']}")

else:
    print("Invalid input")




