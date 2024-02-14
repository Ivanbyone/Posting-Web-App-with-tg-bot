from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def start_button() -> ReplyKeyboardMarkup:

    start = [
        [
            KeyboardButton(text="Find post")
        ]
    ]

    start_keyboard = ReplyKeyboardMarkup(
        keyboard=start,
        resize_keyboard=True
    )

    return start_keyboard
