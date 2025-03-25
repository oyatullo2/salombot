
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

men_buyurtmachiman_rus=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Мои заказы'),
            KeyboardButton(text='📥 Создать заказ')
        ],
        [
            KeyboardButton(text='✅ Предложения фрилансеров')
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