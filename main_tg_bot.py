import requests
import datetime
from config import token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    
    code_to_smile = {
        "Clear" : "Ясно \U00002600",
        "Clouds" : "Облачно \U00002601",
        "Rain" : "Дождь \U00002614",
        "Drizzle" : "Дождь \U00002614",
        "Snow" : "Снег \U00002744",
        "Thunderstorm" : "Молния \U000026C8",
        "Mist" : "Туман \U0001F32B",
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric'
            )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_discription = data["weather"][0]["main"]
        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = "Посмотри в окно"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n"
              f"Влажность: {humidity}\nДавление: {pressure} мм.рт.ст\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Хорошего дня!"
              )
    
    except :
        await message.reply("\U00002620 Проверьте данные ввода \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)