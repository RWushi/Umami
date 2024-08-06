from Config import bot, UserState
from Keyboards.Courier import menu_kb, location_kb

async def menu(chat_id):
    text = "Выберите действие:"
    kb = menu_kb
    await UserState.menu_courier.set()
    await bot.send_message(chat_id, text, reply_markup=kb)

async def location(chat_id):
    text = ("Чтобы начать трансляцию Вашей геолокации:\n"
            "1) Нажмите на значок скрепки в поле ввода сообщения.\n"
            "2) Нажмите \"Геопозиция\".\n"
            "3) Нажмите \"Транслировать геопозицию\".\n"
            "4) Разрешите Телеграму получать данные о Вашей локации (если спросит).\n"
            "5) Нажмите \"Пока не отключу\".\n"
            "6) В конце рабочего дня Вам нужно нажать на кнопку \"❌Закончить работу\".")
    kb = location_kb
    await UserState.location.set()
    await bot.send_message(chat_id, text, reply_markup=kb)
