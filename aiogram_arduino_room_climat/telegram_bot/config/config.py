from aiogram import Bot
from dataclasses import dataclass
from environs import Env


@dataclass
class _TelegramBot:
    """
    Представляет параметры конфигурации для Telegram-бота.
    """
    API_KEY_TELEGRAM_BOT: str  # Ключ API Telegram бота
    COM_PORT: str  # COM-порт для последовательной связи


@dataclass
class _ConfigTelegramBot:
    """
    Представляет конфигурацию для Telegram-бота.
    """
    TELEGRAM_BOT: _TelegramBot  # Конфигурация Telegram-бота


def __load_config_bot(path: str | None) -> _ConfigTelegramBot:
    """
    Загружает параметры конфигурации для Telegram-бота из указанного файла окружения.

    Args:
        path (str | None): Путь к файлу окружения.

    Returns:
        ConfigTelegramBot: Параметры конфигурации для Telegram-бота.

    Raises:
        ValueError: Если возникает проблема с загрузкой или валидацией параметров конфигурации.
    """
    env = Env()
    env.read_env(path)

    API_KEY_TELEGRAM_BOT = env('API_KEY_TELEGRAM_BOT')
    if not API_KEY_TELEGRAM_BOT or len(API_KEY_TELEGRAM_BOT) != 46:
        raise ValueError(f'Не удалось загрузить API_KEY_TELEGRAM_BOT из {path}\nКлюч: {API_KEY_TELEGRAM_BOT}')

    COM_PORT = env('COM_PORT')
    if not COM_PORT or COM_PORT.startswith('COM') and COM_PORT[3:].isdigit():
        raise ValueError(f'Не удалось инициализировать COM_PORT из {path}\nПорт: {COM_PORT}')

    return _ConfigTelegramBot(
        TELEGRAM_BOT=_TelegramBot(
            API_KEY_TELEGRAM_BOT=API_KEY_TELEGRAM_BOT,
            COM_PORT=COM_PORT
        )
    )

config = __load_config_bot('.env')
bot = Bot(config.TELEGRAM_BOT.API_KEY_TELEGRAM_BOT, parse_mode='HTML')
