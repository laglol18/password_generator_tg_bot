import telebot
from telebot import types
import random
#Второй раз пишу бота с помощью telebot. Проще чем aiogram. Хотелось бы разобрать его подробнее на уроке ))
a = 0
b = 0
bot = telebot.TeleBot('6102021384:AAHFhkkVd1L75xASGCv-Cw1y1_j_gPsBPGQ')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Поздороваться')
btn2 = types.KeyboardButton('Сгенерировать пароль')
markup.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text="Привет!", reply_markup=markup)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, text="Привет\nНажми на кнопки, чтобы начать.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Поздороваться":
        bot.send_message(message.chat.id, text="Привееет!")

    elif message.text=="Сгенерировать пароль":
        msg = bot.send_message(message.chat.id,'Сколько паролей вам сгенерировать? (100 максимум)', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, pass_count)

    else:
        bot.send_message(message.chat.id,'Неизвестная функция. Нажмите /help чтобы посмотреть функционал')

@bot.message_handler(content_types=['text'])
def pass_count(message):
    global b
    try:
        b = int(message.text)
        if 0 < b <= 100:
            msg = bot.send_message(message.chat.id,'Какой длины вы хотите пароль? (30 максимум)')
            bot.register_next_step_handler(msg, pass_len)
        else:
            bot.send_message(message.chat.id,'Вы ввели некорректное число', reply_markup=markup)
    except:
        bot.send_message(message.chat.id,'Введите целое число не больше 100', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def pass_len(message):
    chars = '+-*!&$?=abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    global a
    try:
        a = int(message.text)
        if 0 < a <= 30:
            l = a
            c = b
            passwords = ''
            for i in range(c):
                password = ''
                for j in range(l):
                    password += random.choice(chars)
                passwords += password + '\n'
            bot.send_message(message.chat.id, passwords, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Вы ввели некорректное число', reply_markup=markup)
    except:
            bot.send_message(message.chat.id,'Введите целое число не больше 30', reply_markup=markup)


bot.polling(none_stop=True)
