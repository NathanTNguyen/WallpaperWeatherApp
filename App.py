import requests
import ctypes
import os
import time

city = "City of Parramatta"
api_key = "2839b6012af49108dab56c41744c92e6"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

while True:

    response = requests.get(url)
    data = response.json()

    # Get the current temperature in degrees Celsius
    temperature = data["main"]["temp"] - 273.15
    weather = data["weather"][0]["main"]

    print(f"The current temperature in {city} is {temperature:.1f}°C")
    print(f"The current conditions are: {weather}")

    # Set the wallpaper based on the current conditions
    if weather == "Thunderstorm":
        wallpaper = "thunderstorm.jpg"
    elif weather == "Drizzle":
        wallpaper = "drizzle.jpg"
    elif weather == "Rain":
        wallpaper = "rain.jpg"
    elif weather == "Snow":
        wallpaper = "snow.jpg"
    elif weather == "Mist":
        wallpaper = "mist.jpg"
    elif weather == "Smoke":
        wallpaper = "smoke.jpg"
    elif weather == "Haze":
        wallpaper = "haze.jpg"
    elif weather == "Dust":
        wallpaper = "dust.jpg"
    elif weather == "Fog":
        wallpaper = "fog.jpg"
    elif weather == "Sand":
        wallpaper = "sand.jpg"
    elif weather == "Ash":
        wallpaper = "ash.jpg"
    elif weather == "Squall":
        wallpaper = "squall.jpg"
    elif weather == "Tornado":
        wallpaper = "tornado.jpg"
    elif weather == "Clear":
        wallpaper = "clear.jpg"
    elif weather == "Clouds":
        wallpaper = "clouds.jpg"
    else:
        wallpaper = "default.jpg"

    #set wallpaper
    absolute_path = os.path.dirname(__file__)
    relative_path = wallpaper
    full_path = os.path.join(absolute_path, relative_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path , 0)

    time.sleep(300)