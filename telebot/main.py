import asyncio
from aiogram import Bot, Dispatcher
from os import getenv
from modules import routers


BOT = Bot(token=getenv('TELEBOT_TOKEN'))
DP = Dispatcher()

# Добавляем в корневой роутер кастомные
DP.include_routers(*routers)


async def main():
    await DP.start_polling(BOT)


if __name__ == "__main__":
    asyncio.run(main())
