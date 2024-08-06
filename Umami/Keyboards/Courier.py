from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞Поддержка")],
        [KeyboardButton(text="📍Начать работу")],
        [KeyboardButton(text="❌Закончить работу")]
    ],
    resize_keyboard=True
)

location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️Вернуться в меню")]
    ],
    resize_keyboard=True
)

support = InlineKeyboardButton("📞Поддержка", url="https://t.me/qwertp0i")
support_kb = InlineKeyboardMarkup().add(support)