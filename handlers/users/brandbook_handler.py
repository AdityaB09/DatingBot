from datetime import datetime

from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.back_inline import only_back_keyboard
from keyboards.inline.guide_inline import create_pagination_keyboard, guide_callback
from keyboards.inline.settings_menu import information_keyboard
from loader import dp, _
from utils.db_api import db_commands


@dp.callback_query_handler(text="information")
async def get_information(call: CallbackQuery):
    start_date = datetime(2021, 8, 10, 14, 0)
    now_date = datetime.now()
    delta = now_date - start_date
    count_users = await db_commands.count_users()
    txt = (f"Вы попали в раздел <b>Информации</b> бота, здесь вы можете посмотреть: статистику,"
           f"изменить язык, а также посмотреть наш брендбук.\n\n"
           f"🌐 Дней работаем: <b>{delta.days}</b>\n"
           f"👤 Всего пользователей: <b>{count_users}</b>\n")
    await call.message.edit_text(
        text=txt,
        reply_markup=await information_keyboard()
    )


async def send_photo_with_caption(
        call: CallbackQuery,
        photo: str,
        caption: str,
        step: int,
        total_steps: int,
) -> None:
    markup = await create_pagination_keyboard(step, total_steps)

    await call.message.delete()
    await call.message.answer_photo(types.InputFile(photo), reply_markup=markup, caption=caption)


@dp.callback_query_handler(text="guide")
async def get_guide(call: CallbackQuery) -> None:
    await send_photo_with_caption(
        call=call,
        photo=r"brandbook/first_page.png",
        caption=_("Руководство по боту: \n<b>Страница №1</b>"),
        step=1,
        total_steps=4
    )


@dp.callback_query_handler(guide_callback.filter(action="forward"))
async def get_forward(call: CallbackQuery, callback_data: dict) -> None:
    step = int(callback_data.get("value"))
    if step == 2:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/second_page.png",
            caption=_("Руководство по боту: \n<b>Страница №2</b>"),
            step=2,
            total_steps=4
        )
    elif step == 3:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/third_page.png",
            caption=_("Руководство по боту: \n<b>Страница №3</b>"),
            step=3,
            total_steps=4
        )
    elif step == 4:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/fourth_page.png",
            caption=_("Руководство по боту: \n<b>Страница №4</b>"),
            step=4,
            total_steps=4
        )


@dp.callback_query_handler(guide_callback.filter(action="backward"))
async def get_backward(call: CallbackQuery, callback_data: dict) -> None:
    step = int(callback_data.get("value"))

    if step == 1:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/first_page.png",
            caption=_("Руководство по боту: \n<b>Страница №1</b>"),
            step=1,
            total_steps=4
        )
    elif step == 2:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/second_page.png",
            caption=_("Руководство по боту: \n<b>Страница №2</b>"),
            step=2,
            total_steps=4
        )
    elif step == 3:
        await send_photo_with_caption(
            call=call,
            photo=r"brandbook/third_page.png",
            caption=_("Руководство по боту: \n<b>Страница №3</b>"),
            step=3,
            total_steps=4
        )


@dp.callback_query_handler(text="contacts")
async def contacts_menu(call: CallbackQuery):
    await call.message.edit_text(
        text=(
            "📧 Добро пожаловать в наш раздел контактной информации платформы:\n\n"
            "Наш сайт: В разработке"
        ),
        reply_markup=await only_back_keyboard(menu="information")
    )
