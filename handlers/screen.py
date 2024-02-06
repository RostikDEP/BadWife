from start_bot import dp
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold


@dp.message(CommandStart())
async def command_start(message: Message):
	await message.answer(f"{hbold}")
