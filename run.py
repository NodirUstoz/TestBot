import asyncio

from aiogram import Bot, Dispatcher, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tugmalar import main as m
from tugmalar import settings as s
import tugmalar as t

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1-Handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Assalomu alaykum hurmatli foydalanuvchi Test Botimizga xush kelibsiz!", 
    reply_markup=s
)
    
# 2-Handler
@dp.message(Command('cars'))
async def cmd_cars(message: Message):
    await message.answer(f"Avtomobillardan birini tanlang: ",
    reply_markup=await t.inline_cars() 
)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")

# @AiogramUchunBot