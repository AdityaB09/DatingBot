from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def second_menu_keyboard():
    markup = InlineKeyboardMarkup()
    my_profile = InlineKeyboardButton(text="👤 Моя анекта", callback_data="my_profile")
    edit_profile = InlineKeyboardButton(text="⬆️ Изменить анкету", callback_data="change_profile")
    back_to_menu = InlineKeyboardButton(text="⏪️ Вернуться в меню", callback_data="start_menu")
    verification = InlineKeyboardButton(text="✅ Верификация", callback_data="verification")
    filters = InlineKeyboardButton(text="⚙️ Фильтры", callback_data="filters")
    balance = InlineKeyboardButton(text="💎 Премиум", callback_data="premium")
    markup.row(my_profile, verification)
    markup.add(balance)
    markup.row(edit_profile, filters)
    markup.add(back_to_menu)
    return markup
