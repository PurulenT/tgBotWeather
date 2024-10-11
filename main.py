import telebot
import requests
import json

bot = telebot.TeleBot('7884716994:AAGAflU5l3zEIjX99mVS6dByzQS-5V0Tigc')
API = '38f499143880530d97c8c7379e786f06'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую! Напиши название твоего города и я дам тебе информацию по погоде.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp} C')
    else:
        bot.reply_to(message, "Город указан неверно!")

bot.polling(none_stop=True)