import serial.tools.list_ports


def com_get_info() -> None:
    """
    Функция для вывода полной информации о COM портах и их параметрах в консоль.

    Returns:
        None
    """
    com_ports_info = []
    
    # Получаем список доступных COM портов
    com_ports = serial.tools.list_ports.comports()
    
    # Собираем информацию о каждом COM порте
    for port in com_ports:
        com_ports_info.append(f"Порт: {port.device}, Описание: {port.description}, HWID: {port.hwid}")
    
    # Выводим информацию в консоль
    print('\n'.join(com_ports_info))