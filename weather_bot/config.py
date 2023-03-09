# enter your API tokens here
BOT_API_TOKEN = ""
WEATHER_API_KEY = ""

WEATHER_NOW_API_CALL = (
    "http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
)
WEEK_FORECAST_API_CALL = (
    "http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7&aqi=no"
)
