from aiogram.types import Message
from Config import dp, DB, UserState
from HelloMessages.Client import request_location, menu


@dp.message_handler(state=UserState.confirmation)
async def confirmation_handler(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text == "✅Подтвердить заказ":
        await request_location(chat_id)

    elif message.text == "❌Отменить заказ":
        await menu(chat_id)


import Client.Address