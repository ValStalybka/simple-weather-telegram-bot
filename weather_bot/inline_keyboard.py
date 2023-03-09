from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BTN_RIGHT_NOW = InlineKeyboardButton("Weather now", callback_data="weather_now")
BTN_WEEK_FORECAST = InlineKeyboardButton("Week forecast", callback_data="week_forecast")
BTN_SET_CITY = InlineKeyboardButton("Set my city", callback_data="set_city")

START = InlineKeyboardMarkup().add(BTN_SET_CITY)
SET_CITY = InlineKeyboardMarkup().add(BTN_RIGHT_NOW, BTN_WEEK_FORECAST)
RIGHT_NOW = InlineKeyboardMarkup().add(BTN_WEEK_FORECAST)
WEEK_FORECAST = InlineKeyboardMarkup().add(BTN_RIGHT_NOW)
