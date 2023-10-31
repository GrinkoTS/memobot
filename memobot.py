import telebot
import random
from telebot import types
import os
import glob

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button1 = types.KeyboardButton('Хочу мем!')
    keyboard.add(button1)
    # Отправка сообщения с клавиатурой
    bot.reply_to(message, 'Привет! Я Мемобот и я умею веселить народ) Нажми кнопку "Хочу мем!"', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Хочу мем!':
        # Действия при нажатии на "Хочу мем!"
        image_folder_path = 'mems'
        image_files = glob.glob(os.path.join(image_folder_path, '*.jpg'))
        random_image = random.choice(image_files)
        with open(random_image, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

    else:
        # Действия при получении другого сообщения
        bot.reply_to(message, 'Ты не нажал кнопку! Но мем я все равно пришлю ;)')
        image_folder_path = 'mems'
        image_files = glob.glob(os.path.join(image_folder_path, '*.jpg'))
        random_image = random.choice(image_files)
        with open(random_image, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

bot.polling()