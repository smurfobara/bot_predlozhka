from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import logging
from config import admin

import keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()
    contact = State()

class Sending(StatesGroup):
    first = State()
    message = State()
    messageText = None

class transfer(StatesGroup):
    first = State()
    second = State()
    third = State()


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext):
    await message.answer('Привет!👋 Отправляй сообщение, и его анонимно получит админ\nМожно присылать видео и фото, а также просто текст.', reply_markup=types.reply_keyboard_remove.ReplyKeyboardRemove())
    await state.set_state(transfer.second)

@router.message(F.photo, transfer.second)
async def get_photo(message: Message, state: FSMContext):
    photoID = message.photo[-1].file_id
    photoCaption = message.caption
    await message.bot.send_photo(admin, photoID, caption=photoCaption)
    await message.answer('Готово! Сообщение фото с описанием отправлено админу\n Если захотите прислать еще, нажмите кнопку ниже👇👇')
    await state.clear()

@router.message(F.video, transfer.second)
async def get_video(message: Message, state: FSMContext):
    videoID = message.video.file_id 
    videoCaption = message.caption
    await message.bot.send_video(admin, videoID, caption=videoCaption)
    await message.answer('Готово! Сообщение видео с описанием отправлено админу\n Если захотите прислать еще, нажмите кнопку ниже👇👇')
    await state.clear()

@router.message(F.text, transfer.second)
async def get_text(message: Message, state: FSMContext):
    await message.bot.send_message(admin, message.text)
    await message.answer('Готово! Сообщение отправлено админу\n Если захотите прислать еще, нажмите кнопку ниже👇👇', reply_markup=kb.send_again)
    await state.clear()




""" @router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')

@router.message(F.text == 'Корзина')
async def basket(message: Message):
    await message.answer('И вам добрый день!')

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    #await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Номер?', reply_markup=kb.phone)

@router.message(F.contact, Reg.number)
async def contact_get(message: Message, state: FSMContext):
    await state.update_data(number = message.contact.phone_number)
    await message.answer('Твой номер успешно получен!', reply_markup=types.reply_keyboard_remove.ReplyKeyboardRemove())
    contact = f'Number: {message.contact.phone_number}\nName: {message.contact.first_name}\nSurname: {message.contact.last_name}\nUserId: {message.contact.user_id}'
    await message.bot.send_message(5893427261, str(contact))
    print(message.contact)
    await state.clear()

@router.message(Command('test'))
async def send_message_channel(message: Message, state: FSMContext):
    await state.set_state(Sending.first)
    await message.answer('Введите нужное сообщение')

@router.message(Sending.first)
async def send_message_channel_second(message: Message, state: FSMContext):
    #await state.update_data(messageText = message.text)
    Sending.messageText = message.text
    await message.bot.send_message(2102441712, Sending.messageText)
    await state.clear() """

