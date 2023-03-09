from urllib.error import HTTPError
from urllib.request import urlopen

from config import WEATHER_NOW_API_CALL, WEATHER_API_KEY


def get_city(city):
    city = city.strip()

    try:
        urlopen(WEATHER_NOW_API_CALL.format(api_key=WEATHER_API_KEY, city=city))

    except HTTPError:
        return None
    return city.lower().capitalize()
