from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


INLINE_KEYBOARD_REQUEST_INFORMATION = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = 'Запросить информацию',
                callback_data='request_information'
            )
        ]
    ]
)