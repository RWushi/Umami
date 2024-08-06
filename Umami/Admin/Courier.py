from aiogram.types import Message
from Config import dp, UserState
from HelloMessages.Admin import add_courier, delete_courier, menu


@dp.message_handler(state=UserState.courier)
async def courier_edit_handler(message: Message):
    chat_id = message.chat.id

    if message.text == "➕Добавить":
        await add_courier(chat_id)

    elif message.text == "➖Удалить":
        await delete_courier(chat_id)

    elif message.text == "↩️Вернуться в меню":
        await menu(chat_id)

import Admin.Add_Delete