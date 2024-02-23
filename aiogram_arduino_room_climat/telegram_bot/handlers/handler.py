from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from utils.logger import logger

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info(LEXICON_RU['log_info_cmd_start'].format(
        message.from_user.full_name, 
        message.from_user.id))
    
    await message.answer(LEXICON_RU['cmd_start'].format(message.from_user.full_name))