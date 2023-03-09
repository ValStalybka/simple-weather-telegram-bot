from datetime import datetime

from aiogram.types.user import User

from weather_api import Forecast, Weather


def start_message():
    return (
        "Hi {user_full_name}!\n"
        "I can tell you the weather, but I need to know your city"
    )


def city_error_message():
    return "City not found!\nPlease, check the spelling and retype."


def weather_now_message(weather: Weather):
    return (
        f"Current weather in {User.city}:\n"
        f"Temp: {weather.temp} C\n"
        f"Condition: {weather.condition}"
    )


def week_forecast_message(cast: Forecast):
    date = datetime.strptime(cast.date, "%Y-%m-%d")
    return (
        f"{date.strftime('%a, %B %d')}:\n"
        f"Temp: {cast.max_temp} C / {cast.min_temp} C\n"
        f"Condition: {cast.condition}"
    )
