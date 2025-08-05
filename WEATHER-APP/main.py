import requests
import json
while True:
    try:
        city = input("Enter the city name: ")

        url = f"http://api.weatherapi.com/v1/current.json?key=0795de5375ac40f09b475657252007&q={city}&aqi=no"
        r = requests.get(url)
        weatherDict = json.loads(r.text)
        parse = weatherDict["current"]["temp_c"]
        print(parse)
    except Exception as e:
        print("No matching Location found")
        quit()
        