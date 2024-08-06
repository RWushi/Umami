from aiogram.types import Message
from Config import dp, UserState, DB
from HelloMessages.Client import menu
from Courier.ClosestCourier import get_couriers, filter_couriers
from .Payment import payment


async def get_drink(user_id):
    async with DB() as conn:
        drink = await conn.fetchval('SELECT drink FROM client WHERE ID = $1', user_id)
    return drink


@dp.message_handler(state=UserState.address)
async def back_to_menu_handler(message: Message):
    chat_id = message.chat.id

    if message.text == "↩️Вернуться в меню":
        await menu(chat_id)


@dp.message_handler(content_types=['location'], state=UserState.address)
async def address_handler(message: Message):
    if message.location:
        user_id = message.from_user.id
        latitude = message.location.latitude
        longitude = message.location.longitude

        async with DB() as conn:
            await conn.execute('''INSERT INTO client (ID, latitude, longitude) 
                                  VALUES ($1, $2, $3) 
                                  ON CONFLICT (ID) 
                                  DO UPDATE SET latitude = $2, longitude = $3''', user_id, latitude, longitude)

        await message.answer("Ваш адрес сохранен")

        address = (latitude, longitude)
        couriers = await get_couriers()
        if couriers:
            filtered_couriers = await filter_couriers(couriers, address)
            if filtered_couriers:
                chat_id = message.chat.id
                drink = await get_drink(user_id)
                await payment(chat_id, drink)
            else:
                await message.answer("В радиусе 1.5 км нет подходящих курьеров, повторите попытку позже")
        else:
            await message.answer("Сейчас нет работающих курьеров, повторите попытку в рабочее время")

    else:
        await message.answer("Разрешите боту доступ к Вашему местоположению")


import Courier.Confirmation