from aiogram.types import Message
from Config import bot, dp, UserState, DB
from Keyboards.Client import support_kb
from HelloMessages.Client import confirmation


async def add_drink(user_id, drink):
    async with DB() as conn:
        await conn.execute('UPDATE client SET drink = $2 WHERE ID = $1', user_id, drink)


async def check_courier_id(user_id):
    async with DB() as conn:
        result = await conn.fetchval('SELECT courier_id FROM client WHERE ID = $1', user_id)
    return result is not None


async def get_courier_id(user_id):
    async with DB() as conn:
        courier_id = await conn.fetchval('SELECT courier_id FROM client WHERE ID = $1', user_id)
    return courier_id


async def get_location(courier_id):
    async with DB() as conn:
        latitude = await conn.fetchval('SELECT latitude FROM courier WHERE ID = $1', courier_id)
        longitude = await conn.fetchval('SELECT longitude FROM courier WHERE ID = $1', courier_id)
    return latitude, longitude


@dp.message_handler(state=UserState.menu_client)
async def menu_handler(message: Message):
    chat_id = message.from_user.id
    user_id = message.from_user.id

    if message.text == "☕Заказать кофе":
        drink = "Кофе"
        await add_drink(user_id, drink)
        await confirmation(chat_id, drink)

    elif message.text == "🍵Заказать чай":
        drink = "Чай"
        await add_drink(user_id, drink)
        await confirmation(chat_id, drink)

    elif message.text == "🚴Местоположение курьера":
        courier_exists = await check_courier_id(user_id)
        if courier_exists:
            courier_id = await get_courier_id(user_id)
            latitude, longitude = await get_location(courier_id)
            await bot.send_location(chat_id, latitude, longitude)
        else:
            await message.answer("У Вас нет активных заказов, либо нет подходящих курьеров")

    elif message.text == "📞Поддержка":
        await message.answer("При необходимости в помощи обратитесь к человеку", reply_markup=support_kb)


import Client.Confirmation