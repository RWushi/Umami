from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☕Заказать кофе")],
        [KeyboardButton(text="🍵Заказать чай")],
        [KeyboardButton(text="🚴Местоположение курьера")],
        [KeyboardButton(text="📞Поддержка")]
    ],
    resize_keyboard=True
)

confirmation_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅Подтвердить заказ")],

        [KeyboardButton(text="❌Отменить заказ")]
    ],
    resize_keyboard=True
)

location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏡Указать адрес", request_location=True)],
        [KeyboardButton(text="↩️Вернуться в меню")]
    ],
    resize_keyboard=True
)


support = InlineKeyboardButton("📞Поддержка", url="https://t.me/qwertp0i")
support_kb = InlineKeyboardMarkup().add(support)