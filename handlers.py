import logging
from aiogram import types
from aiogram.utils import executor
from bot import dp
from keys import insurance_types
from aiogram.dispatcher.filters import Text
from keyboards import second_keyboard


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        input_field_placeholder="Выберите тип страхования:"
    )

    buttons = [
        types.KeyboardButton(text="Полис E-Осаго"),
        types.KeyboardButton(text="Cтрахование домов и квартир"),
        types.KeyboardButton(text="Страхование путешественников")
        ]
    keyboard.add(*buttons)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_name=}')

    if message.chat.type == 'private':
        await message.answer(f'Привет, {user_name}! Это бот страховой компании "Узбекинвест"', reply_markup=keyboard)


@dp.message_handler(Text(equals=insurance_types))
async def send_faq(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=second_keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите один вариант"
    )
    await message.answer('Тест Вопрос #1', reply_markup=keyboard)


@dp.message_handler(Text(equals="Вернуться назад"))
async def start(message: types.Message):
    buttons = [
        types.KeyboardButton(text="Полис E-Осаго"),
        types.KeyboardButton(text="Cтрахование домов и квартир"),
        types.KeyboardButton(text="Страхование путешественников")
    ]
    keyboard.add(*buttons)
    await message.answer(text='Назад.', reply_markup=keyboard)


@dp.message_handler(Text(equals="Связаться с контактным центром"))
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Да", url="tg://resolve?domain=marininwonderland")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Даете согласие на обработку персональных данных?", reply_markup=keyboard)




if __name__ == '__main__':
    executor.start_polling(dp)
