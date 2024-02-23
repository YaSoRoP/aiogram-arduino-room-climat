from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon.lexicon_ru import LEXICON_RU


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(LEXICON_RU['cmd_start'].format(message.from_user.full_name))