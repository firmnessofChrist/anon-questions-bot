from aiogram import Bot, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from src.callbacks import AdminStats, AdminUpload, AdminMailing, AdminRefs, AdminAdv, AdminPanel, AdminChannels
from src.utils.db import MongoDbClient
from aiogram import F
import os
router = Router()

# Путь к файлу, где будут храниться сообщения
messages_file_path = os.path.join('data', 'received_messages.txt')

# Admin-panel keyboard
@router.callback_query(AdminPanel.filter())
async def admin_panel(callback_query: CallbackQuery, bot: Bot):
    # Answer the callback query with a message 'Back'
    await callback_query.answer('Back')

    # Check if the user ID matches the admin IDs
    if callback_query.from_user.id == 686138890 or callback_query.from_user.id == 1291860365:
        keyboard_admin = InlineKeyboardBuilder()

        # Add buttons to the keyboard for different admin actions
        keyboard_admin.row(
            InlineKeyboardButton(text='Statistics📊', callback_data=AdminStats().pack()),
            InlineKeyboardButton(text='Upload📝', callback_data=AdminUpload().pack())
        )
        keyboard_admin.row(
            InlineKeyboardButton(text='Mailing📩', callback_data=AdminMailing().pack()),
            InlineKeyboardButton(text='Channels🗣', callback_data=AdminChannels().pack())
        )
        # Добавляем кнопку "View Messages" в админскую панель
        keyboard_admin.row(
            InlineKeyboardButton(text='View Messages📩', callback_data='view_messages')
        )
        keyboard_admin.row(
            InlineKeyboardButton(text='Referrals🔗', callback_data=AdminRefs().pack()),
            InlineKeyboardButton(text='Advertisement Post📢', callback_data=AdminAdv().pack())
        )

        # Edit the message text to show the admin panel with the keyboard
        await bot.edit_message_text(chat_id=callback_query.from_user.id, text="Admin panel:",
                                    message_id=callback_query.message.message_id,
                                    reply_markup=keyboard_admin.as_markup())


# Хендлер для кнопки "View Messages"
@router.callback_query(F.data == "view_messages")
async def view_messages(callback_query: CallbackQuery, bot: Bot):
    try:
        if os.path.exists(messages_file_path):
            with open(messages_file_path, 'r', encoding='utf-8') as file:
                messages = file.read()
                if not messages.strip():
                    messages = "Сообщений пока нет."
        else:
            messages = "Файл с сообщениями не найден."

        await bot.send_message(callback_query.from_user.id, f"Все полученные сообщения:\n\n{messages}")
    except Exception as e:
        await bot.send_message(callback_query.from_user.id, f"⚠️ Ошибка при чтении сообщений: {e}")
    finally:
        await callback_query.answer()
