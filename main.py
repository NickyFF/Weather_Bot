from config import token
import requests
import datetime

def get_weather(city, token):
    
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
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
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
        
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n"
              f"Влажность: {humidity}\nДавление: {pressure} мм.рт.ст\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Хорошего дня!"
              )
    
    except Exception as ex:
        print(ex)
        print("Проверьте данные ввода")

def main():
    city = input("Введите город: ")
    get_weather(city, token)

if __name__ == "__main__":
    main()