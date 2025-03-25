
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

men_frilanserman_rus=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Мои заказы'),
            KeyboardButton(text='📥 Взять заказ')
        ],
        [
            KeyboardButton(text='🔎 Найти заказ'),
            KeyboardButton(text='✅ Мои предложения')


        ],
        [
KeyboardButton(text='⚙️ Настройки')
        ],
        [
            KeyboardButton(text='⬅️ назад')
        ]

    ],
    resize_keyboard=True
)