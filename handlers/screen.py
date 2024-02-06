from start_bot import dp, logger
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, BufferedInputFile
from aiogram.enums import ChatAction
import pyautogui
from start_bot import bot
import io



@dp.message(Command("screen"))
async def make_screen(message: Message):
	try:
		try:
			await bot.send_message(message.chat.id, "Спроба зробити скріншот")
			screen = pyautogui.screenshot()
			with io.BytesIO() as buffer:
				screen.save(buffer, format="PNG")
				buffer.seek(0)
				await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
				await bot.send_photo(message.chat.id, BufferedInputFile(buffer.getvalue(), filename="screenshot.png"))
		except Exception as e:
			try:
				await bot.send_message(message.chat.id, "Помилка")
				await bot.send_message(message.chat.id, str(e))
			except Exception as e:
				logger.error(f"Error in make_screen>Error Notification: {str(e)}")

	except Exception as e:
		try:
			logger.critical(f"GLOBAL ERROR im make_screen function: {str(e)}")
		except:
			pass