from urllib.request import urlopen
from dataclasses import dataclass
import json

from aiogram.types.user import User

from config import WEATHER_API_KEY, WEEK_FORECAST_API_CALL, WEATHER_NOW_API_CALL


@dataclass(slots=True, frozen=True)
class Weather:
    temp: str
    condition: str


@dataclass(slots=True, frozen=True)
class Forecast:
    date: str
    max_temp: str
    min_temp: str
    condition: str


def get_weather() -> Weather:
    url = WEATHER_NOW_API_CALL.format(api_key=WEATHER_API_KEY, city=User.city)
    response = urlopen(url)
    data = json.load(response)["current"]
    temp = data["temp_c"]
    condition = data["condition"]["text"]
    return Weather(temp=temp, condition=condition)


def week_forecast():
    url = WEEK_FORECAST_API_CALL.format(api_key=WEATHER_API_KEY, city=User.city)
    response = urlopen(url)
    data = json.load(response)["forecast"]["forecastday"]
    forecast = []

    for day in data:
        date = day["date"]
        max_temp, min_temp = day["day"]["maxtemp_c"], day["day"]["mintemp_c"]
        condition = day["day"]["condition"]["text"]
        forecast.append(
            Forecast(
                date=date, max_temp=max_temp, min_temp=min_temp, condition=condition
            )
        )
    return forecast
