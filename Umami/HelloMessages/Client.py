from Config import bot, UserState
from Keyboards.Client import menu_kb, confirmation_kb, location_kb


async def menu(chat_id):
    text = "Выберите действие:"
    kb = menu_kb
    await UserState.menu_client.set()
    await bot.send_message(chat_id, text, reply_markup=kb)


async def confirmation(chat_id, drink):
    text = f"Подтвердите или отмените заказ: {drink}"
    kb = confirmation_kb
    await UserState.confirmation.set()
    await bot.send_message(chat_id, text, reply_markup=kb)


async def request_location(chat_id):
    text = "Разрешите боту доступ к Вашему местоположению, для этого нажмите \"ОК\". (Возможно потребуется разрешить телеграму доступ к местоположению)"
    kb = location_kb
    await UserState.address.set()
    await bot.send_message(chat_id, text, reply_markup=kb)