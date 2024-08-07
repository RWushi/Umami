from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from States import PostgresStateStorage
import asyncpg


DATABASE_CONFIG = {
    'host': '',
    'database': '',
    'user': '',
    'password': '',
    'port': '5432'
}

storage = PostgresStateStorage(**DATABASE_CONFIG)


async def create_connection():
    return await asyncpg.connect(**DATABASE_CONFIG)


class DB:
    async def __aenter__(self):
        self.conn = await create_connection()
        return self.conn

    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def add_new_user(user_id):
    async with DB() as conn:
        async with conn.transaction():
            await conn.execute('''
                INSERT INTO user_settings (ID, role) VALUES ($1, 'client') 
                ON CONFLICT (ID) DO NOTHING
            ''', user_id)
            await conn.execute('''
                INSERT INTO client (ID) VALUES ($1) 
                ON CONFLICT (ID) DO NOTHING
            ''', user_id)


class UserState(StatesGroup):
    menu_admin = State()
    menu_courier = State()
    menu_client = State()
    courier = State()
    admin = State()
    add_courier = State()
    delete_courier = State()
    add_admin = State()
    delete_admin = State()
    location = State()
    address = State()
    confirmation = State()
    payment = State()


payment_token = ''

bot = Bot(token='')
dp = Dispatcher(bot, storage=storage)
