from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Робочі_години')
button2 = KeyboardButton('/Заявка_прод')
button3 = KeyboardButton('/Наявність_прод')
button4 = KeyboardButton('/Залишки')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button1).insert(button2).add(button3).insert(button4)
