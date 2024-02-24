from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard import INLINE_KEYBOARD_REQUEST_INFORMATION
from services.arduino.arduino_python_interface import request_sensor_data
from datetime import datetime
from utils.logger import logger

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info(LEXICON_RU['log_info_cmd_start'].format(
        message.from_user.full_name, 
        message.from_user.id))
    
    await message.delete()
    await message.answer(
        text=LEXICON_RU['cmd_start'].format(message.from_user.full_name),
        reply_markup=INLINE_KEYBOARD_REQUEST_INFORMATION)
    

@router.callback_query(F.data.in_('request_information'))
async def send_information(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['callback_send_information'].format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            request_sensor_data()),
        reply_markup=INLINE_KEYBOARD_REQUEST_INFORMATION
    )
    await callback.answer()