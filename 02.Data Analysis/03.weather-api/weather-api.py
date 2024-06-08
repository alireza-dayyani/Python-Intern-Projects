import requests
import pandas as pd

api_key = "0cf33743827961629b12588939d3ebdc"
city_name = input("Enter a city name in Iran: ")
geocoding = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},'',IR&appid={api_key}")

df = pd.DataFrame(geocoding.json())

lat = str(df.at[0, "lat"])
lon = str(df.at[0, "lon"])

city_result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
city_result = city_result.json()
print(city_result["weather"])