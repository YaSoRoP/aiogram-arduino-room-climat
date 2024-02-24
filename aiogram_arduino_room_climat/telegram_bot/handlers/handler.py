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
    """
    Обрабатывает команду /start.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    logger.info(LEXICON_RU['log_info_cmd_start'].format(
        message.from_user.full_name, 
        message.from_user.id))
    
    await message.delete()  # Удаляем команду /start из чата
    # Отправляем приветственное сообщение с инлайн-клавиатурой
    await message.answer(
        text=LEXICON_RU['cmd_start'].format(message.from_user.full_name),
        reply_markup=INLINE_KEYBOARD_REQUEST_INFORMATION)
    

@router.callback_query(F.data.in_('request_information'))
async def send_information(callback: CallbackQuery):
    """
    Обрабатывает запрос на получение информации.

    Args:
        callback (CallbackQuery): Объект callback-запроса.

    Returns:
        None
    """
    logger.info(LEXICON_RU['log_info_callback_send_information'].format(
        callback.message.from_user.full_name, 
        callback.message.from_user.id))
    # Редактируем текст сообщения с текущей датой-временем и данными с датчика
    await callback.message.edit_text(
        text=LEXICON_RU['callback_send_information'].format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Текущая дата-время
            request_sensor_data()),  # Данные с датчика
        reply_markup=INLINE_KEYBOARD_REQUEST_INFORMATION
    )
    await callback.answer()  # Отвечаем на callback-запрос