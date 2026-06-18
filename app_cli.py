import argparse
import db_manager
import data_processor

def run_cli():
    db_manager.setup_database()
    cmd_parser = argparse.ArgumentParser(description="Консольный модуль управления Экспресс Курьер")
    cmd_parser.add_argument('mode', choices=['report', 'export', 'import'], help="Режим работы")
    cmd_parser.add_argument('--period', help="Временной отрезок")
    cmd_parser.add_argument('--file', help="Целевой файл данных")

    arguments = cmd_parser.parse_args()

    if arguments.mode == 'report':
        print(">> СВОДНАЯ СТАТИСТИКА ПО СТАТУСАМ <<")
        for state, qty in db_manager.calculate_status_stats():
            print(f"Категория: [{state}] -> Текущее количество: {qty} ед.")
            
    elif arguments.mode == 'export':
        if not arguments.file:
            print("Ошибка: не указан путь к файлу через параметр --file")
            return
            
        if arguments.file.endswith('.json'):
            data_processor.save_to_json(arguments.file)
            print("Выгрузка структуры JSON завершена успешно.")
        elif arguments.file.endswith('.xml'):
            data_processor.save_to_xml(arguments.file)
            print("Выгрузка структуры XML завершена успешно.")
        else:
            print("Ошибка: неподдерживаемый тип документа.")

if __name__ == '__main__':
    run_cli()
