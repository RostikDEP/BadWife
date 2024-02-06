import os
from dotenv import load_dotenv
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode

load_dotenv()
TOKEN = os.getenv("TEST_TOKEN")

dp = Dispatcher()


async def main():
	bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
	await dp.start_polling(bot)


if __name__ == '__main__':
	from handlers import *
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	asyncio.run(main())