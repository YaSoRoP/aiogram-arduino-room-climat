from asyncio import run
from aiogram import Dispatcher
from handlers.handler import router
from config.config import bot


async def main() -> None:
    """
    Основная функция, запускающая бота.

    Создает диспетчер (Dispatcher), 
    включает маршрутизатор (router), 
    удаляет вебхук и начинает поллинг сообщений от пользователей.

    Returns:
        None
    """
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())