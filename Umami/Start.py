from aiogram.types import Message
from aiogram.utils import executor
from Config import dp, DB, add_new_user
from HelloMessages.Admin import menu as admin
from HelloMessages.Courier import menu as courier
from HelloMessages.Client import menu as client


@dp.message_handler(commands=['start', 'my_id'], state="*")
async def role_check(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await add_new_user(user_id)

    if message.text == '/start':

        async with DB() as conn:
            role = await conn.fetchval('SELECT role FROM user_settings WHERE ID = $1', user_id)

        if role == 'admin':
            await admin(chat_id)
        elif role == 'courier':
            await courier(chat_id)
        elif role == 'client':
            await client(chat_id)

    elif message.text == '/my_id':
        await message.answer(f"Ваш ID: `{user_id}`", parse_mode="Markdown")


import Admin.Menu, Courier.Menu, Client.Menu

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)