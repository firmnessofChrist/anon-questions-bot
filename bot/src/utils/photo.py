from aiogram.types import FSInputFile
import os

# Путь к изображению welcome
welcome = FSInputFile(os.path.join("src", "static", "welcome.jpg"))

# Добавляем остальные изображения
new_message = FSInputFile(os.path.join("src", "static", "new_message.jpg"))
sended = FSInputFile(os.path.join("src", "static", "sended.jpg"))
answer_sended = FSInputFile(os.path.join("src", "static", "answer_sended.jpg"))
send_message_photo = FSInputFile(os.path.join("src", "static", "send_message_photo.jpg"))
no_photo = FSInputFile(os.path.join("src", "static", "no_photo.jpg"))
