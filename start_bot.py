import os
from dotenv import load_dotenv
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from loguru import logger
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TEST_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

logger.add(f"logs/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.log", format="{time} {level} {message}", rotation="10 MB", compression="zip")

async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	from handlers import *
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	asyncio.run(main())