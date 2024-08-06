from aiogram.types import LabeledPrice, PreCheckoutQuery, Message
from aiogram.types.message import ContentType
from Config import bot, dp, payment_token, UserState
from Courier.Confirmation import confirmation
from HelloMessages.Client import menu


async def payment(chat_id, drink):
    await UserState.payment.set()
    title = drink
    await bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description="Покупка напитка",
        payload=chat_id,
        provider_token=payment_token,
        currency='RUB',
        prices=[LabeledPrice(label=drink, amount=10000)]
    )


@dp.pre_checkout_query_handler(lambda query: True, state=UserState.payment)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state=UserState.payment)
async def process_successful_payment(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await message.answer("Спасибо за покупку! Ваш заказ уже передается курьеру и администратору. Сохраните чек, для того, чтобы его показать курьеру")
    await menu(chat_id)
    await confirmation(user_id)