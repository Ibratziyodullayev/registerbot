from aiogram import types


async def start_menu_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.KeyboardButton("📝royhattan o'tish"),
        types.KeyboardButton("👤Admin bilan bog'lanish"),
    )
    return btn



async def info_yes_or_no_btn():
    btn = types.InlineKeyboardMarkup() #inlay keybort textga qarab ozi moslashadi
    btn.add(
        types.InlineKeyboardButton("✅", callback_data='yes'),
        types.InlineKeyboardButton("❌", callback_data='no'),
    )
    return btn