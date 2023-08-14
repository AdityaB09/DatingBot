from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

manipulation_callback = CallbackData(
    "user_callback",
    "action",
    "value"
)


async def user_manipulation() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    find_user = InlineKeyboardButton("🔍 Найти пользователя", callback_data="db:search_user")
    markup.add(find_user)
    return markup


async def search_user_keyboard(user_id: int, is_banned: bool) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)

    if is_banned:
        button = InlineKeyboardButton(
            "🟢 Разблокировать",
            callback_data=manipulation_callback.new(
                action="unban",
                value=f"{user_id}")
        )
    else:
        button = InlineKeyboardButton(
            "🚫 Заблокировать",
            callback_data=manipulation_callback.new(
                action="ban",
                value=f"{user_id}")
        )
    markup.add(button)
    return markup
