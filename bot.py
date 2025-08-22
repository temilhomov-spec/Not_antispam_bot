import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Удаляем все сообщения с ссылками
@dp.message_handler(lambda message: "http" in message.text.lower())
async def delete_ads(message: types.Message):
    await message.delete()

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("✅ Бот работает! Реклама будет удаляться автоматически.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
