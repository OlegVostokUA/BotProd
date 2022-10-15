from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# button_moder = KeyboardButton('/moder')
button_load = KeyboardButton('/УПЗ_Залишки')
button_list = KeyboardButton('/Подані_залишки')
button_orders = KeyboardButton('/Прод_заявки')
button_delete_orders = KeyboardButton('/Видалити_заявку')
button_parse = KeyboardButton('/Сформувати_файл')
button_clear = KeyboardButton('/Очистити_БД')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
    .insert(button_list).add(button_orders).insert(button_delete_orders).add(button_clear)\
    .insert(button_parse)
