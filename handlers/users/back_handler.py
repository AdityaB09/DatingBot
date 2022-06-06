import random
from contextlib import suppress

from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from keyboards.inline.main_menu_inline import start_keyboard
from loader import dp
from utils.db_api import db_commands


async def delete_message(message: types.Message):
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


@dp.callback_query_handler(text="back_with_delete")
async def open_menu(call: CallbackQuery):
    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    user_db = await db_commands.select_user(telegram_id=call.from_user.id)
    markup = await start_keyboard(status=user_db['status'])
    await delete_message(call.message)

    await call.message.answer(f"<b>{heart} QueDateBot </b> - платформа для поиска новых знакомств.\n\n"
                              f"<b>🤝 Сотрудничество: </b>\n"
                              f"Если у вас есть предложение о сотрудничестве, пишите сюда - "
                              f"@Support\n\n",
                              reply_markup=markup)