from aiogram.dispatcher.filters.state import State,StatesGroup

class buyurtma_yaratish_state(StatesGroup):
    ism=State()
    narx=State()
    tg_id=State()
    soxa=State()
    xaqida=State()