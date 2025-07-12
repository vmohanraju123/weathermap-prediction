import requests
API_KEY="86a3072dce3de48084ca807e4b3bd79c"
BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
def getweather():
    city=input("Enter city name:")
    url=BASE_URL+"appid="+API_KEY+"&q="+city+"&units=metric"
    response=requests.get(url)
    data=response.json()
    if data["cod"] != "404":
        main=data["main"]
        weather=data["weather"][0]
        print("\nweather in {}:".format(city))
        print("Temprature:",main["temp"],"°C")
        print("Humidity:",main["humidity"],"%")
        print("Condition:",weather["description"].capitalize())
    else:
        print("city not found")
getweather()