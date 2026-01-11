# this dashboard will call from OpenWeatherMap (OWM)
import requests

baseURL_lat_lon = "https://api.openweathermap.org/data/2.5/forecast?lat=57.14369&lon=-2.09814&appid=036478abe20af19a7e11a444ce1d5eff&units=metric"
# url needed if specify location with latitude and longitude coordinates
baseURL_city_name = "https://api.openweathermap.org/data/2.5/forecast?q=Aberdeen,gb&mode=json&appid=036478abe20af19a7e11a444ce1d5eff&units=metric"
# url needed if specify location with city name and country code
# error when using city_name url was because of "mode=xml" instead of "mode=json"

def retrieve_weather_info():
    # sends request to api, with a url, and recieves the data returned
    baseURL_lat_lon
    OWMresponse = requests.get(baseURL_city_name) # uses the requests.get module from requests to fetch a response

    if OWMresponse.status_code == 200: # status code 200 means ok
        weatherData = OWMresponse.json() # read info in json format
        return weatherData
    else:
        print(f"Failed to retrieve OWMresponse data: {OWMresponse.status_code}") # any other code is undesirable and will be shown here

weather_info = retrieve_weather_info()

if weather_info:
    print(f"{weather_info["list.weather.main"]}") # not recognised


    
    


