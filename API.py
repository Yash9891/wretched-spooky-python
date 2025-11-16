#packages-----------------------------------
import requests

#download webpage
response=requests.get("https://api.github.com")
print(response.status_code)


import random
number=random.randint(1,10)
choice=random.choice(["apple","mango","kaju"])

print(f"{choice} {number}")

import datetime
today=datetime.date.today()
print(today)

import os
current_dir=os.getcwd()
print(current_dir)


#API----------------------------------------------
import requests
def get_weather(latitude, longitude):
        url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current_weather=true"
          )

        # Make the request
        response = requests.get(url)
        data = response.json()

        return  data["current_weather"]["temperature"]


print("Temperature:",get_weather(51.50,2.35)," celcius")




