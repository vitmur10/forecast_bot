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
	m = str(message.text)
	city = m[7:]
	if 'погода' in m:
		if len(m) > 6:
			try:
				mgr = owm.weather_manager()
				observation = mgr.weather_at_place(city)
				w = observation.weather
				temp = w.temperature('celsius')['temp']
				temp_max = w.temperature('celsius')['temp_max']
				temp_min = w.temperature('celsius')['temp_min']
				answre = 'У ' + city + ' у даний момент ' + w.detailed_status + '\n'
				answre += 'Температура зараз ' + str(temp) + '°С\n' \
				'' + 'Макс. ' + str(temp_max) + '°С\n' \
				'Мін. ' + str(temp_min) + '°С' + '\n'
				bot.send_message(message.chat.id, answre)
				bot.register_next_step_handler(message, prognoz)
			except:
				bot.send_message(message.chat.id, 'Щось не так із містом \n'
												  'Як правильно:\n'
												  '(Погода місто)')
	elif 'Погода' in m:
		if len(m) > 6:
			try:
				mgr = owm.weather_manager()
				observation = mgr.weather_at_place(city)
				w = observation.weather
				temp = w.temperature('celsius')['temp']
				temp_max = w.temperature('celsius')['temp_max']
				temp_min = w.temperature('celsius')['temp_min']
				answre = 'У ' + city + ' у даний момент ' + w.detailed_status + '\n'
				answre += 'Температура зараз ' + str(temp) + '°С\n' \
				'' + 'Макс. ' + str(temp_max) + '°С\n' \
				'Мін. ' + str(temp_min) + '°С' + '\n'
				bot.send_message(message.chat.id, answre)
				bot.register_next_step_handler(message, prognoz)
			except:
				bot.send_message(message.chat.id, 'Щось не так із містом \n'
												  'Як правильно:\n'
												  '(Погода місто)')

bot.polling(none_stop=True)
