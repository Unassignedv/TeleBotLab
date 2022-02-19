import telebot
from telebot import types
from datetime import datetime
from random import randrange

token = "52551*****:**********"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/info", "Время", "Привет", "Число")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, """
/help - заново вывести этот список \n
/hello - hello, world \n
/ubuntu - Определение ubuntu\n
/info - информация о создателе \n
/start - открыть клавиатуру \n
хочу (просто сообщение) - ссылка на вуз \n
время (просто сообщение) - получит текущее время \n
Число (просто сообщение) - при котором бот будет отсылать случайное число в диапазоне от 0 до 100 \n
Любой текст (просто сообщение) - вывод ошибку \n""")


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Информация: БИН2106 Гуролев В.П.')


@bot.message_handler(commands=['ubuntu'])
def ubuntu(message):
    bot.send_message(message.chat.id, 'Ubuntu — дистрибутив GNU/Linux, основанный на Debian GNU/Linux. Основным разработчиком и спонсором является компания Canonical. В настоящее время проект активно развивается и поддерживается свободным сообществом.')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello, world!')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "время":
        bot.send_message(message.chat.id, str(datetime.now()))
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет")
    elif message.text.lower() == "число":
        bot.send_message(message.chat.id, str(randrange(1, 100)))
    else:
        bot.send_message(message.chat.id, "Текст не распознан")


bot.polling(none_stop=True, interval=0)
