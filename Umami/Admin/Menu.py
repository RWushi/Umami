from aiogram.types import Message
from Config import dp, UserState
from HelloMessages.Admin import courier, admin


@dp.message_handler(state=UserState.menu_admin)
async def menu_handler(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.text == "🚴Курьеры":
        await courier(chat_id)

    elif message.text == "🧑‍💻Администраторы":
        await admin(chat_id)


import Admin.Courier, Admin.Admin