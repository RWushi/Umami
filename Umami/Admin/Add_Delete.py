from aiogram.types import Message
from Config import dp, UserState, DB
from HelloMessages.Admin import admin, courier


async def check_id(user_id):
    async with DB() as conn:
        result = await conn.fetchrow('SELECT 1 FROM user_settings WHERE ID = $1', user_id)
    return result is not None


async def add_courier(user_id):
    async with DB() as conn:
        async with conn.transaction():
            await conn.execute('''
                UPDATE user_settings 
                SET role = 'courier'
                WHERE ID = $1
            ''', user_id)
            await conn.execute('DELETE FROM client WHERE ID = $1', user_id)
            await conn.execute('''
                INSERT INTO courier (ID) 
                VALUES ($1)
            ''', user_id)


async def delete_courier(user_id):
    async with DB() as conn:
        await conn.execute('DELETE FROM user_settings WHERE ID = $1', user_id)


async def add_admin(user_id):
    async with DB() as conn:
        async with conn.transaction():
            await conn.execute('''
                UPDATE user_settings 
                SET role = 'admin'
                WHERE ID = $1
            ''', user_id)
            await conn.execute('DELETE FROM client WHERE ID = $1', user_id)
            await conn.execute('DELETE FROM courier WHERE ID = $1', user_id)


async def delete_admin(user_id):
    async with DB() as conn:
        await conn.execute('DELETE FROM user_settings WHERE ID = $1', user_id)


@dp.message_handler(state=UserState.add_courier)
async def add_courier_handler(message: Message):
    chat_id = message.chat.id

    if message.text.isdigit():
        user_id = int(message.text)
        user_exists = await check_id(user_id)
        if user_exists:
            await add_courier(user_id)
            await message.answer(f"Пользователь с ID {user_id} добавлен, как курьер, чтобы применилась новая роль, ему нужно перезапустить бота")
        else:
            await message.answer(f"Пользователя с ID {user_id} в этом боте не существует")

    elif message.text == "↩️Вернуться назад":
        await courier(chat_id)

    else:
        await message.answer("Введите числовой ID")


@dp.message_handler(state=UserState.delete_courier)
async def delete_courier_handler(message: Message):
    chat_id = message.chat.id

    if message.text.isdigit():
        user_id = int(message.text)
        user_exists = await check_id(user_id)
        if user_exists:
            await delete_courier(user_id)
            await message.answer(f"Пользователь с ID {user_id} больше не является курьером")
        else:
            await message.answer(f"Пользователя с ID {user_id} в этом боте не существует")

    elif message.text == "↩️Вернуться назад":
        await courier(chat_id)

    else:
        await message.answer("Введите числовой ID")


@dp.message_handler(state=UserState.add_admin)
async def add_admin_handler(message: Message):
    chat_id = message.chat.id

    if message.text.isdigit():
        user_id = int(message.text)
        user_exists = await check_id(user_id)
        if user_exists:
            await add_admin(user_id)
            await message.answer(f"Пользователь с ID {user_id} добавлен, как администратор, чтобы применилась новая роль, ему нужно перезапустить бота")
        else:
            await message.answer(f"Пользователя с ID {user_id} в этом боте не существует")

    elif message.text == "↩️Вернуться назад":
        await admin(chat_id)

    else:
        await message.answer("Введите числовой ID")


@dp.message_handler(state=UserState.delete_admin)
async def delete_admin_handler(message: Message):
    chat_id = message.chat.id

    if message.text.isdigit():
        user_id = int(message.text)
        user_exists = await check_id(user_id)
        if user_exists:
            await delete_admin(user_id)
            await message.answer(f"Пользователь с ID {user_id} больше не является администратором")
        else:
            await message.answer(f"Пользователя с ID {user_id} в этом боте не существует")

    elif message.text == "↩️Вернуться назад":
        await admin(chat_id)

    else:
        await message.answer("Введите числовой ID")