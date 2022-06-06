import datetime
import pyowm
import telebot
from telebot import types
from pyowm.utils import timestamps
import Token
import time

bot = Token.bot
owm = Token.owm

@bot.message_handler(commands=['start'])
def hello(message):
	bot.send_message(message.chat.id, 'Привіт друже')

@bot.message_handler(content_types=['text'])

def prognoz(message):
	m2 = set(message.text)
	city = message.text[7:]
	if len(m2) == 1:
		if 'z' in m2:
			bot.send_message(message.chat.id, 'Вийди отсюда розбійник')
		elif 'v' in m2:
			bot.send_message(message.chat.id, 'Вийди отсюда розбійник')
	elif len(m2) == 2:
		if 'z' and 'v' in m2:
			bot.send_message(message.chat.id, 'Вийди отсюда розбійник')

	if "погода" in message.text:
		if len(message.text) > 6:
			try:
				mgr = owm.weather_manager()
				observation = mgr.weather_at_place(city)
				w = observation.weather
				temp = w.temperature('celsius')['temp']
				temp_max = w.temperature('celsius')['temp_max']
				temp_min = w.temperature('celsius')['temp_min']
				answre = f"""У {str.capitalize(city)} у даний момент {w.detailed_status}\nТемпература зараз {round(temp)}°С\nМакс.{round(temp_max)}°С\nМін.{round(temp_min)}°С"""
				bot.send_message(message.chat.id, answre)
				bot.register_next_step_handler(message, prognoz)
			except:
				bot.send_message(message.chat.id, 'Щось не так із містом \n'
												  'Як правильно:\n'
												  '(Погода місто)')
	elif "погода" in message.text:
		if len(message.text) > 6:
			try:
				mgr = owm.weather_manager()
				observation = mgr.weather_at_place(city)
				w = observation.weather
				temp = w.temperature('celsius')['temp']
				temp_max = w.temperature('celsius')['temp_max']
				temp_min = w.temperature('celsius')['temp_min']
				answre = f"""У {str.capitalize(city)} у даний момент {w.detailed_status}\nТемпература зараз {temp}°С\nМакс.{temp_max}°С\nМін.{temp_min}°С"""
				bot.send_message(message.chat.id, answre)
				bot.register_next_step_handler(message, prognoz)
			except:
				bot.send_message(message.chat.id, 'Щось не так із містом \n'
												  'Як правильно:\n'
												  '(Погода місто)')

bot.polling(none_stop=True)

