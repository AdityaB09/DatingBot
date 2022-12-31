import asyncio
import random

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import BadRequest

from data.config import load_config
from filters import IsPrivate
from functions.app_scheduler import send_message_week
from handlers.users.back_handler import delete_message
from keyboards.inline.language_inline import language_keyboard

from keyboards.inline.main_menu_inline import start_keyboard
from loader import dp, scheduler, _
from utils.db_api import db_commands


@dp.message_handler(IsPrivate(), CommandStart())
async def register_user(message: types.Message):
    try:
        if message.from_user.username is not None:
            await db_commands.add_user(name=message.from_user.full_name,
                                       telegram_id=message.from_user.id,
                                       username=message.from_user.username)
            await db_commands.add_meetings_user(telegram_id=message.from_user.id,
                                                username=message.from_user.username)
        else:
            await db_commands.add_user(name=message.from_user.full_name,
                                       telegram_id=message.from_user.id,
                                       username="None")
            await db_commands.add_meetings_user(telegram_id=message.from_user.id,
                                                username="None")

    except:
        pass
    support = await db_commands.select_user(telegram_id=load_config().tg_bot.support_ids[0])
    user_db = await db_commands.select_user(telegram_id=message.from_user.id)
    markup = await start_keyboard(status=user_db["status"])
    fullname = message.from_user.full_name

    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    await message.answer(_("Приветствую вас, {fullname}!!\n\n"
                           "{heart} <b> QueDateBot </b> - платформа для поиска новых знакомств.\n\n"
                           "🪧 Новости о проекте вы можете прочитать в нашем канале - "
                           "https://t.me/QueDateGroup \n\n"
                           "<b>🤝 Сотрудничество: </b>\n"
                           "Если у вас есть предложение о сотрудничестве, пишите агенту поддержки - "
                           "@{supports}\n\n").format(fullname=fullname, heart=heart,
                                                     supports=support['username']),
                         reply_markup=markup)


@dp.callback_query_handler(text="start_menu")
async def start_menu(call: CallbackQuery):
    user_db = await db_commands.select_user(telegram_id=call.from_user.id)
    support = await db_commands.select_user(telegram_id=load_config().tg_bot.support_ids[0])
    markup = await start_keyboard(user_db["status"])
    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    await call.message.edit_text(_("Приветствую вас, {fullname}!!\n\n"
                                   "{heart} <b> QueDateBot </b> - платформа для поиска новых знакомств.\n\n"
                                   "🪧 Новости о проекте вы можете прочитать в нашем канале - "
                                   "https://t.me/QueDateGroup \n\n"
                                   "<b>🤝 Сотрудничество: </b>\n"
                                   "Если у вас есть предложение о сотрудничестве, пишите агенту поддержки - "
                                   "@{supports}\n\n").format(fullname=call.from_user.full_name, heart=heart,
                                                             supports=support['username']),
                                 reply_markup=markup)
    scheduler.add_job(send_message_week, trigger="interval", weeks=3, jitter=120, args={call.message})


@dp.callback_query_handler(text="language")
async def choice_language(call: CallbackQuery):
    try:
        await call.message.edit_text(_("Выберите язык"), reply_markup=await language_keyboard())
    except BadRequest:
        await delete_message(call.message)
        await call.message.answer(_("Выберите язык"), reply_markup=await language_keyboard())


@dp.callback_query_handler(text="Russian")
@dp.callback_query_handler(text="Deutsch")
@dp.callback_query_handler(text="English")
@dp.callback_query_handler(text="Indonesian")
async def change_language(call: CallbackQuery):
    if call.data == "Russian":
        await db_commands.update_user_data(telegram_id=call.from_user.id, language="ru")
    elif call.data == "Deutsch":
        await db_commands.update_user_data(telegram_id=call.from_user.id, language="de")
    elif call.data == "English":
        await db_commands.update_user_data(telegram_id=call.from_user.id, language="en")
    elif call.data == "Indonesian":
        await db_commands.update_user_data(telegram_id=call.from_user.id, language="in")
    await call.answer(_("Язык был успешно изменен. Введите команду /start"), show_alert=True)
    await asyncio.sleep(5)
    await call.message.delete()
