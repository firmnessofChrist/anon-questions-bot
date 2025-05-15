import logging
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile, CallbackQuery, InlineKeyboardButton, InputMediaPhoto, InputMediaAnimation, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.callbacks import AdminStats, AdminUpload, AdminMailing, AdminChannels, AdminRefs, AdminAdv

router = Router()

# Путь к файлу для хранения сообщений
messages_file_path = os.path.join('data', 'received_messages.txt')
os.makedirs('data', exist_ok=True)  # создаёт папку, если её нет

# Убедимся, что папка существует
os.makedirs(os.path.dirname(messages_file_path), exist_ok=True)

# ✅ Хендлер для вызова админ-панели по команде /admin
@router.message(Command('admin'))
async def admin_panel(message: Message):
    admin_ids = {686138890, 1119884448}
    if message.from_user.id not in admin_ids:
        await message.reply("⛔ У вас нет доступа к админ-панели.")
        return

    keyboard_admin = InlineKeyboardBuilder()

    # Добавляем кнопки в админскую панель
    keyboard_admin.row(
        InlineKeyboardButton(text='Statistics📊', callback_data=AdminStats().pack()),
        InlineKeyboardButton(text='Upload📝', callback_data=AdminUpload().pack())
    )
    keyboard_admin.row(
        InlineKeyboardButton(text='Mailing📩', callback_data=AdminMailing().pack()),
        InlineKeyboardButton(text='Channels🗣️', callback_data=AdminChannels().pack())
    )
    keyboard_admin.row(
        InlineKeyboardButton(text='View Messages📩', callback_data='view_messages')
    )
    keyboard_admin.row(
        InlineKeyboardButton(text='Referrals🔗', callback_data=AdminRefs().pack()),
        InlineKeyboardButton(text='Advertisement Post📢', callback_data=AdminAdv().pack())
    )

    await message.answer("🛠 Админ-панель:", reply_markup=keyboard_admin.as_markup())

# ✅ Хендлер для сохранения текстовых сообщений
@router.message(F.text)  # Только текст
async def save_message(message: Message):
    # Получаем текст сообщения
    text = message.text
    if not text:
        await message.reply("⚠️ Только текстовые сообщения сохраняются.")
        return

    # Добавляем новое сообщение в файл
    try:
        with open(messages_file_path, 'a', encoding='utf-8') as file:
            file.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] ID {message.from_user.id}: {text}\n")
        await message.reply("✅ Ваше сообщение сохранено.")
    except Exception as e:
        await message.reply(f"⚠️ Ошибка при сохранении сообщения: {e}")



