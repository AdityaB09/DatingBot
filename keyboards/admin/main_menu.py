from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def admin_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    customers = KeyboardButton("🫂 Пользователи")
    settings = KeyboardButton("⚙️ Настройки")
    payments = KeyboardButton("💳 Платежки")
    advert = KeyboardButton("📊 Реклама")
    logs = KeyboardButton("🗒 Логи")
    monitoring = KeyboardButton(text="👀 Мониторинг")
    set_up_technical_works = KeyboardButton(text="🛑 Тех.Работа")
    markup.add(monitoring)
    markup.add(customers, payments)
    markup.add(settings)
    markup.add(logs, advert)
    markup.add(set_up_technical_works)
    return markup
