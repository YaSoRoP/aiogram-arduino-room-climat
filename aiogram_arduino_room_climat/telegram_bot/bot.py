from asyncio import run
from aiogram import Dispatcher
from config.config import bot


async def main() -> None:
    """
    Основная функция, запускающая бота.

    Создает диспетчер (Dispatcher), удаляет вебхук и начинает поллинг сообщений от пользователей.

    Returns:
        None
    """
    dp = Dispatcher()

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())