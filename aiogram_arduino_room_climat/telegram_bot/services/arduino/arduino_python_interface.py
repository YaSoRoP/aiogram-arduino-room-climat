import serial
from aiogram_arduino_room_climat.telegram_bot.config.config import config


COM_PORT: str = config.TELEGRAM_BOT.COM_PORT
BAUD: int = config.TELEGRAM_BOT.BAUD


def request_sensor_data() -> str:
    # Открываем соединение с Arduino
    arduino_connection = serial.Serial(
        port=COM_PORT,
        baudrate=BAUD,
        timeout=1
    )
    
    # Отправляем команду на Arduino
    arduino_connection.write(b'request_information\n')
    
    # Считываем ответ от Arduino
    response: str = arduino_connection.readline().decode().strip()
    
    # Закрываем соединение
    arduino_connection.close()
    
    return response