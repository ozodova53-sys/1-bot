import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

# TOKEN
API_TOKEN = "7036832179:AAHAbG64u19BRGxVlqvTrLZmHJDcS-03bQ"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# VIDEOLAR RO'YXATI (Kod: Link)
# Bu yerga videolaringiz linkini qo'shasiz
videolar = {
    "1": https://t.me/c/3084186707/287
    "2": "https://t.me/vorkaut_andijon/3",
    "12": "https://t.me/vorkaut_andijon/12",
}

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nVideo kodini yuboring (Masalan: 12)")

@dp.message(F.text.isdigit())
async def send_video(message: types.Message):
    kod = message.text
    if kod in videolar:
        await message.answer_video(video=videolar[kod], caption=f"✅ {kod}-video!")
    else:
        await message.answer("⚠️ Bu kod bo'yicha video hali qo'shilmagan.")

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

