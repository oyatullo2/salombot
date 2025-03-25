
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

men_frilanserman=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Mening buyurtmalarim'),
            KeyboardButton(text='📥 Buyurtma olish')
        ],
        [
            KeyboardButton(text='🔎 Buyurtmani toping'),
            KeyboardButton(text='✅ Mening takliflarim')

        ],
        [
            KeyboardButton(text='⚙️ Sozlamalar')
        ],
        [
            KeyboardButton(text='⬅️ Orqaga')
        ]
    ],
    resize_keyboard=True
)