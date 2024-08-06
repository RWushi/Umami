from aiogram.types import Message
from Config import bot, dp, DB, UserState
from Keyboards.Courier import support_kb
from HelloMessages.Courier import location


async def work_day_end(user_id):
    async with DB() as conn:
        await conn.execute('''UPDATE courier 
                              SET latitude = NULL, longitude = NULL 
                              WHERE ID = $1''', user_id)


async def get_message_id(user_id):
    async with DB() as conn:
        message_id = await conn.fetchval('SELECT message_id FROM courier WHERE ID = $1', user_id)
    return message_id if message_id else None


@dp.message_handler(state=UserState.menu_courier)
async def menu_handler(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.text == "📞Поддержка":
        await message.answer("При необходимости в помощи обратитесь к человеку", reply_markup=support_kb)

    if message.text == "📍Начать работу":
        await location(chat_id)

    if message.text == "❌Закончить работу":
        message_id = await get_message_id(user_id)
        if message_id:
            await bot.delete_message(chat_id, message_id=message_id)
            await work_day_end(user_id)
            await message.answer("Ваш рабочий день завершен, локация сброшена")
        else:
            await message.answer("Вы не делились своим расположением с ботом, чтобы сделать это, нужно нажать на кнопку \"📍Начать работу\"")


import Courier.Location