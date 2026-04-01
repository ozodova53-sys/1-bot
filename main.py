import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

# Sizning tokeningiz ulandi
API_TOKEN = "7036832179:AAHAbG64u19bRGtVlqzWTrL2mHJDcS-O3bQ"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nBotingiz muvaffaqiyatli ishga tushdi. 🚀")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Men ishlayapman! Tez orada yangi funksiyalar qo'shamiz.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
