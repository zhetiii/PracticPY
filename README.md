# Модульная система «Экспресс Курьер»

## Инструкция по запуску
1. Установка окружения: `pip install -r requirements.txt`
2. Запуск графического интерфейса: `python app_gui.py`
3. Консольные команды:
   - Просмотр статистики: `python app_cli.py report --period month`
   - Выгрузка данных: `python app_cli.py export --file data.json`
4. Проверка тестов: `python -m pytest`
