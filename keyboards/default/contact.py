
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

contact=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kontakt yuborish',request_contact=True),

        ],
        [
            KeyboardButton(text='🏠 Bosh Menyuga'),
            KeyboardButton(text='⬅️ Orqaga')
        ],





    ],
    resize_keyboard=True
)