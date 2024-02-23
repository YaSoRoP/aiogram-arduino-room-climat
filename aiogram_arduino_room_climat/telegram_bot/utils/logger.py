import logging

# Инициализация логгера
logger = logging.getLogger(__name__)

# Конфигурация бота
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
)
    
# Создание объекта файла для вывода логов
file_handler = logging.FileHandler(filename='bot.log', encoding='utf-8')
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s"))

# Установка обработчика файла для корневого логгера
logging.getLogger().addHandler(file_handler)