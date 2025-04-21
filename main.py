from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Привіт! Це Юля...")
    await asyncio.sleep(6)
    await message.answer("Я на сайті знайомств, де знайомлюсь з хлопцями...")
    await asyncio.sleep(7)
    await message.answer("Тут весело, але більшість просто мовчать")
    await asyncio.sleep(8)
    await message.answer("Може, хоч ти не такий? Я зараз тут — https://твій-смартлінк.com")

if name == '__main__':
    executor.start_polling(dp)
