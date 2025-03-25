
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

nastroyka_rus=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Изменить Имя'),
            KeyboardButton(text='Изменить номер')
        ],
        [
            KeyboardButton(text='Изменить категории'),



        ],
        [
KeyboardButton(text='🏠 На главную')
        ]


    ],
    resize_keyboard=True
)