from aiogram.types import Message
from Config import dp, UserState, DB
from HelloMessages.Courier import menu


async def save_message_id(user_id, message_id):
    async with DB() as conn:
        await conn.execute('''UPDATE courier 
                              SET message_id = $2 
                              WHERE ID = $1''', user_id, message_id)


async def save_location(user_id, latitude, longitude):
    async with DB() as conn:
        await conn.execute('''UPDATE courier 
                              SET latitude = $2, longitude = $3 
                              WHERE ID = $1''', user_id, latitude, longitude)


@dp.message_handler(state=UserState.location)
async def location_button_handler(message: Message):
    chat_id = message.chat.id

    if message.text == "↩️Вернуться в меню":
        await menu(chat_id)


@dp.message_handler(content_types=['location'], state=UserState.location)
async def location_handler(message: Message):
    if message.location.live_period:
        message_id = message.message_id
        user_id = message.from_user.id
        latitude = message.location.latitude
        longitude = message.location.longitude

        await save_location(user_id, latitude, longitude)
        await save_message_id(user_id, message_id)

        await message.answer("Ваша гео-трансляция активирована")
    else:
        await message.answer("Вы отправили статичную геолокацию, отображающую только Ваше текущее положение. Вам нужно отправить Live локацию согласно инструкциям")


@dp.edited_message_handler(content_types=['location'], state=UserState.location)
async def current_location_handler(message: Message):
    if message.location.live_period:
        user_id = message.from_user.id
        latitude = message.location.latitude
        longitude = message.location.longitude

        await save_location(user_id, latitude, longitude)