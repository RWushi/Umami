from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚴Курьеры")],
        [KeyboardButton(text="🧑‍💻Администраторы")]
    ],
    resize_keyboard=True
)

add_delete_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕Добавить")],
        [KeyboardButton(text="➖Удалить")],
        [KeyboardButton(text="↩️Вернуться в меню")]
    ],
    resize_keyboard=True
)

user_id_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️Вернуться назад")]
    ],
    resize_keyboard=True
)