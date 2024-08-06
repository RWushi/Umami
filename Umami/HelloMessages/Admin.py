from Config import bot, UserState
from Keyboards.Admin import menu_kb, add_delete_kb, user_id_kb


async def menu(chat_id):
    text = "Выберите действие:"
    kb = menu_kb
    await UserState.menu_admin.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def courier(chat_id):
    text = "Выберите действие:"
    kb = add_delete_kb
    await UserState.courier.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def admin(chat_id):
    text = "Выберите действие:"
    kb = add_delete_kb
    await UserState.admin.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def add_courier(chat_id):
    text = "Введите ID пользователя, которого хотите сделать курьером"
    kb = user_id_kb
    await UserState.add_courier.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def delete_courier(chat_id):
    text = "Введите ID курьера, которого хотите удалить"
    kb = user_id_kb
    await UserState.delete_courier.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def add_admin(chat_id):
    text = "Введите ID пользователя, которого хотите сделать администратором"
    kb = user_id_kb
    await UserState.add_admin.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

async def delete_admin(chat_id):
    text = "Введите ID администратора, которого хотите удалить"
    kb = user_id_kb
    await UserState.delete_admin.set()
    await bot.send_message(chat_id, text, reply_markup= kb)

