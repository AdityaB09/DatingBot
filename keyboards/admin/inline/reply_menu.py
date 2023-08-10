from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_cancel_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    cancel_button = InlineKeyboardButton("🙅🏻‍♂️ Отменить", callback_data="admin:cancel")
    markup.add(cancel_button)
    return markup


async def settings_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    admins = InlineKeyboardButton("👮‍♂️ Админ Состав", callback_data="admin:admins")
    change_contact = InlineKeyboardButton("📞 Сменить контакты", callback_data="admin:change_contacts")
    markup.add(admins, change_contact)

    return markup


async def logs_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    upload_users_txt = InlineKeyboardButton("🗒 Выгрузить юзеров | .txt", callback_data="owner:backup:users:txt")
    upload_logs = InlineKeyboardButton("🗒 Выгрузить конфиги и логи", callback_data="owner:backup:configs")
    markup.add(upload_users_txt)
    markup.add(upload_logs)
    return markup
