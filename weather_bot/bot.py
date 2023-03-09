import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from city import get_city
from config import BOT_API_TOKEN
import inline_keyboard
from messages import (
    start_message,
    city_error_message,
    weather_now_message,
    week_forecast_message,
)
from weather_api import get_weather, week_forecast

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class Form(StatesGroup):
    city = State()


@dp.message_handler(commands=["start"], content_types=types.ContentType.TEXT)
async def start_handler(message: types.Message):
    user_id = message.from_user.id

    user_full_name = message.from_user.full_name
    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")

    await message.answer(
        text=start_message().format(user_full_name=user_full_name),
        reply_markup=inline_keyboard.START,
    )


@dp.callback_query_handler(text="set_city")
async def get_city_handler(callback_query: types.CallbackQuery):
    await Form.city.set()
    await bot.send_message(callback_query.from_user.id, text="What's your city?")
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.message_handler(state=Form.city)
async def city_process_handler(message: types.Message, state: FSMContext):
    city = message.text

    if get_city(city) is None:
        await message.reply(text=city_error_message())
    else:
        types.user.User.city = city
        await state.finish()
        await message.answer(
            text="City has been set", reply_markup=inline_keyboard.SET_CITY
        )


@dp.callback_query_handler(text="weather_now")
async def weather_now_query_handler(callback_query: types.CallbackQuery):
    weather = get_weather()
    await bot.send_message(
        callback_query.from_user.id,
        text=weather_now_message(weather),
        reply_markup=inline_keyboard.RIGHT_NOW,
    )
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text="week_forecast")
async def week_forecast_query_handler(callback_query: types.CallbackQuery):
    forecast = week_forecast()
    await bot.send_message(
        callback_query.from_user.id,
        text="\n\n".join(week_forecast_message(day) for day in forecast),
        reply_markup=inline_keyboard.WEEK_FORECAST,
    )
    await bot.answer_callback_query(callback_query_id=callback_query.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
