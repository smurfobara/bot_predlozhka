from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'), InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

send_again = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='VK', url='https://vk.com/smurfobara')]])

cars = ['Mercedes', 'Tesla', 'BMW']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://t.me/smurfobara'))
    return keyboard.adjust(2).as_markup()


phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправьте свой номер', request_contact=True)]
])
