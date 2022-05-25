import asyncio

import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
import re

from loguru import logger

from keyboards.inline.change_data_profile_inline import gender_keyboard
from keyboards.inline.filters_inline import filters_keyboard

from loader import dp

from utils.db_api import db_commands
from utils.misc.create_questionnaire import get_data_filters


@dp.callback_query_handler(text="filters")
async def get_filters(call: CallbackQuery):
    user_data = await get_data_filters(call.from_user.id)
    await call.message.edit_text("Фильтр по подбору партнеров:\n\n"
                                 f"🚻 Необходимы пол партнера: {user_data[2]}\n"
                                 f"🔞 Возрастной диапазон: {user_data[0]}-{user_data[1]} лет",
                                 reply_markup=await filters_keyboard())


@dp.callback_query_handler(text="user_age_period")
async def desired_age(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Напишите минимальный возраст")
    await state.set_state("age_period")


@dp.message_handler(state="age_period")
async def desired_min_age_state(message: types.Message, state: FSMContext):
    messages = message.text
    int_message = re.findall('[0-9]+', messages)
    int_messages = "".join(int_message)
    await db_commands.update_user_data(telegram_id=message.from_user.id, need_partner_age_min=int_messages)
    await message.answer("Данные сохранены, теперь введите максимальный возраст")
    await state.reset_state()
    await state.set_state("max_age_period")


@dp.message_handler(state="max_age_period")
async def desired_max_age_state(message: types.Message, state: FSMContext):
    messages = message.text
    int_message = re.findall('[0-9]+', messages)
    int_messages = "".join(int_message)
    await db_commands.update_user_data(telegram_id=message.from_user.id, need_partner_age_max=int_messages)
    await message.answer("Данные сохранены, теперь введите максимальный возраст")
    await state.finish()
    user_data = await get_data_filters(message.from_user.id)
    await message.answer("Фильтр по подбору партнеров:\n\n"
                         f"🚻 Необходимы пол партнера: {user_data[2]}\n"
                         f"🔞 Возрастной диапазон: {user_data[0]}-{user_data[1]} лет",
                         reply_markup=await filters_keyboard())


@dp.callback_query_handler(text="user_max_range")
async def desired_max_range(call: CallbackQuery):
    markup = await gender_keyboard()
    await call.message.edit_text("Выберите, кого вы хотите найти:", reply_markup=markup)


@dp.callback_query_handler()
async def desired_gender(call: CallbackQuery):
    if call.data == 'male':
        try:
            await db_commands.update_user_data(telegram_id=call.from_user.id, need_partner_sex='Мужской')
        except asyncpg.exceptions.UniqueViolationError as err:
            logger.error(err)
    elif call.data == 'female':
        try:
            await db_commands.update_user_data(telegram_id=call.from_user.id, need_partner_sex='Женский')
        except asyncpg.exceptions.UniqueViolationError as err:
            logger.error(err)

    await call.message.edit_text("Данные сохранены")
    await asyncio.sleep(1)
    user_data = await get_data_filters(call.from_user.id)
    await call.message.edit_text("Фильтр по подбору партнеров:\n\n"
                                 f"🚻 Необходимы пол партнера: {user_data[2]}\n"
                                 f"🔞 Возрастной диапазон: {user_data[0]} - {user_data[1]} лет",
                                 reply_markup=await filters_keyboard())
