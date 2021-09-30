import random

from handlers.users.view import select_all_users_list, create_questionnaire
from keyboards.inline.BN_report import report_inline_kb
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.Reports import Report
from data.config import ADMINS

from loader import dp, bot


@dp.callback_query_handler(text="report")
async def report_user(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(
        "Укажите причину жалобы\n"
        "\n"
        "1. 🔞 Материал для взрослых.\n"
        "2. 💊 Пропаганда наркотиков.\n"
        "3. 💰 Продажа товаров и услуг.\n"
        "4. 🦨 Другое.\n"
        "\n"
        "5. Вернуться назад.", reply_markup=report_inline_kb)
    await Report.R1.set()


@dp.callback_query_handler(text="content", state=Report.R1)
@dp.callback_query_handler(text="drugs", state=Report.R1)
@dp.callback_query_handler(text="scam", state=Report.R1)
@dp.callback_query_handler(text="another", state=Report.R1)
async def report_user(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    display_name = call.from_user.full_name

    await call.answer(
        f"Репорт на пользователя успешно отправлен.\n"
        "Администрация предпримет все необходимые меры"
    )

    for admin_id in ADMINS:
        await bot.send_message(
            admin_id,
            f"Кинут репорт на пользователя "
        )
    async with state.proxy() as data:
        data["report_us"] = display_name


@dp.callback_query_handler(text="cancel_report", state=Report.R1)
async def cancel_report(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    user_list = await select_all_users_list()
    random_user = random.choice(user_list)
    await create_questionnaire(random_user=random_user, chat_id=call.from_user.id)
    await state.reset_state()
