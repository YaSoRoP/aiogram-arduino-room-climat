import serial
from time import sleep
from utils.logger import logger
from aiogram_arduino_room_climat.telegram_bot.config.config import config


# Получаем конфигурационные параметры из файла конфигурации
COM_PORT = config.TELEGRAM_BOT.COM_PORT
BAUD = config.TELEGRAM_BOT.BAUD

def request_sensor_data() -> str:
    """
    Функция для запроса данных с датчика, подключенного к Arduino.

    Returns:
        str: Строка с данными датчика.
    """
    try:
        # Устанавливаем соединение с Arduino
        arduino = serial.Serial(
            port=COM_PORT, 
            baudrate=BAUD)
    except serial.SerialException as e:
        logger.error(f'Произошла ошибка при подключении к Arduino: {e}')
        return "Ошибка при подключении к Arduino"
    
    sleep(2)  # Ждем некоторое время перед чтением данных
    response = arduino.readline().decode().strip()
    arduino.close()  # Закрываем соединение с Arduino
    return response
