import requests

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
NAME_TO_COORD_URL = "http://api.openweathermap.org/geo/1.0/direct"
ZIP_TO_COORD_URL = "http://api.openweathermap.org/geo/1.0/zip"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"


class API:

    def __init__(self):
        self.api_input = ""
        self.search_with = "name"
        self.coords = []

        self.coord_params_direct = {
            "q": "",
            "appid": API_KEY
        }

        self.coord_params_zip = {
            "zip": "",
            "appid": API_KEY
        }

        self.weather_params = {
            "lat": "",
            "lon": "",
            "exclude": "minutely,hourly,daily,alerts",
            "units": "metric",
            "appid": API_KEY
        }

    def set_search_params(self, x):
        self.search_with = x

    def set_api_input(self, x):
        self.api_input = x
        if self.search_with == "name":
            self.coord_params_direct["q"] = x
        elif self.search_with == "zip":
            self.coord_params_zip["zip"] = x

    def update_params(self):
        self.weather_params["lat"] = self.coords[0]
        self.weather_params["lon"] = self.coords[1]

    def get_coords(self):
        if self.search_with == "name":
            response = requests.get(url=NAME_TO_COORD_URL, params=self.coord_params_direct)
            response.raise_for_status()
            self.coords = [response.json()[0]["lat"], response.json()[0]["lon"]]
        elif self.search_with == "zip":
            response = requests.get(url=ZIP_TO_COORD_URL, params=self.coord_params_zip)
            response.raise_for_status()
            self.coords = [response.json()["lat"], response.json()["lon"]]
        self.update_params()

    def get_weather_info(self):

        useful_info = {
            "name": self.api_input,
            "lat": self.coords[0],
            "lon": self.coords[1],
            "temperature": "",
            "pressure": "",
            "humidity": "",
            "dew point": "",
            "clouds": "",
            "wind speed": "",
            "description": "",
            "icon": None
        }

        response = requests.get(url=BASE_URL, params=self.weather_params)
        response.raise_for_status()
        info = response.json()
        useful_info["temperature"] = info["current"]["temp"]
        useful_info["pressure"] = info["current"]["pressure"]
        useful_info["humidity"] = info["current"]["humidity"]
        useful_info["dew point"] = info["current"]["dew_point"]
        useful_info["clouds"] = info["current"]["clouds"]
        useful_info["wind speed"] = info["current"]["wind_speed"]
        useful_info["description"] = (info["current"]["weather"][0]["main"] +
                                      ": " +
                                      info["current"]["weather"][0]["description"])

        icon_name = info["current"]["weather"][0]["icon"]
        print(icon_name)
        icon = requests.get(url="https://openweathermap.org/img/wn/" + icon_name + "@2x.png")

        useful_info["icon"] = icon

        return useful_info
