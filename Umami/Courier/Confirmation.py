from Config import bot, DB
from .ClosestCourier import get_couriers, filter_couriers, choose_courier
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_drink(user_id):
    async with DB() as conn:
        drink = await conn.fetchval('SELECT drink FROM client WHERE ID = $1', user_id)
    return drink


async def get_address(user_id):
    async with DB() as conn:
        latitude = await conn.fetchval('SELECT latitude FROM client WHERE ID = $1', user_id)
        longitude = await conn.fetchval('SELECT longitude FROM client WHERE ID = $1', user_id)
    return latitude, longitude


async def save_courier_id(user_id, courier_chat_id):
    async with DB() as conn:
        await conn.execute('''UPDATE client 
                              SET courier_id = $2
                              WHERE ID = $1''', user_id, courier_chat_id)


async def confirmation(user_id):
    address = await get_address(user_id)
    couriers = await get_couriers()
    filtered_couriers = await filter_couriers(couriers, address)
    drink = await get_drink(user_id)

    courier_chat_id = await choose_courier(filtered_couriers, address)
    await save_courier_id(user_id, courier_chat_id)

    main_text = f"Вы оказались ближайшим курьером к пользователю, который только совершил заказ: {drink}"

    user = await bot.get_chat(user_id)
    username = user.username
    if username:
        client = InlineKeyboardButton("Клиент🧑", url=f"https://t.me/{username}")
        client_kb = InlineKeyboardMarkup().add(client)
        await bot.send_message(courier_chat_id, main_text, reply_markup=client_kb)
    else:
        additional_text = "У этого пользователя нет юзернейма"
        text = f"{main_text}\n{additional_text}"
        await bot.send_message(courier_chat_id, text)

    latitude, longitude = address
    await bot.send_location(courier_chat_id, latitude, longitude)

    client_chat_id = user_id

    await bot.send_message(client_chat_id, "Курьер принял Ваш заказ, ожидайте")
    await message_for_admin(drink, username)


async def message_for_admin(drink, username):
    main_text = f"Курьер принял заказ: {drink}"

    if username:
        client = InlineKeyboardButton("Клиент🧑", url=f"https://t.me/{username}")
        client_kb = InlineKeyboardMarkup().add(client)
        await bot.send_message(5111567138, main_text, reply_markup=client_kb)
    else:
        additional_text = "У этого пользователя нет юзернейма"
        text = f"{main_text}\n{additional_text}"
        await bot.send_message(5111567138, text)#5419806659 RWushi
