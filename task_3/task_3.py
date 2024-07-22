'''
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, 
переданий як аргумент командного рядка, і виводити статистику за рівнями логування 
наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як 
другий аргумент командного рядка, щоб отримати всі записи цього рівня.
'''
import re
import sys
from pathlib import Path
from collections import Counter

if len(sys.argv) > 1:
    '''Принимаем информацию из консоли
    Для теста берем "python task_3/task_3.py task_3/log.txt ErrOR"
    Регист уровня не важен
    '''
    data = sys.argv
    file = Path(sys.argv[1])
    try:
        accent = '' if not data[2] else data[2]
    except IndexError:
        accent = ''
else:
    sys.exit(0)

if not file.exists():
    print(Fore.RED + f'\nФайл "{file}" не существует!\n')
    sys.exit(0)

if not file.is_file():
    print(Fore.RED + f'\n"{file}" Не является файлом лога!\n')
    sys.exit(0)

def main(file:str, accent:str='' ):
    '''
    Для теста берем "python task_3/task_3.py task_3/log.txt ErrOR"
    Регист уровня не важен
    '''
    log_lines = load_logs(file)
    if len(log_lines) < 1:
        return 'Файл лога пуст'

    # Получим список подсчитанных логов по уровню события
    counted_logs =  count_logs_by_level(log_lines)

    # Итоговый текст для вывод в консоль
    total_string = ''

    # Таблица с подсчетами уровней
    total_string += display_log_counts(counted_logs)

    # Если кто то указал уровень лога, нужно получить строки таких логов.
    if len(accent) > 0:
        
        # Сами строки
        filtered_logs = filter_logs_by_level(log_lines, accent)
        string_lines = ''
        
        # Конкатенируем данные.
        for line in filtered_logs:
            line_string = ''
            for key, val in line.items():
                line_string += val + ' '
            string_lines += line_string + '\n'

        # Готовый текст для консоли
        total_string += '\n' + string_lines

    return total_string 

def load_logs(file: str) -> list:
    ''' Находим обрабатываем файл'''
    lines = []
    try:
       
       # Открываем файл с гарантией закрытия
       with open(file, 'r', -1, 'UTF-8', 'strict') as f:
           
           # Создаем лист словарей.
           for line in f.readlines():
                lines.append(parse_log_line(line))          

    except BaseException as e:
        return f'Произошла ошибка {e}'
    return lines
    
def parse_log_line(line: str) -> dict:
    ''' Паттерн для разделения строки на нужные сегменты'''
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'
    m = re.match(pattern, line)
    return {'date':m[1], 'time':m[2], 'level':m[3], 'message':m[4]}

def filter_logs_by_level(logs: list, level: str) -> list:
    # Достанем строки с нужным уровнем лога
    return list(filter(lambda line: line['level'].lower() == level.lower(), logs))

def count_logs_by_level(logs: list) -> dict:
    # Берем из каждой строки только уровень и количество повторов
    levels = [line['level'] for line in logs]
    return Counter(levels)

def display_log_counts(counts: dict):
    # Таблица для вывод подсчитанных уровней логов
    table = ''
    head = f"\n{'Рівень логування':<17} | {'Кількість':<8}\n"
    divider = '-' * len(head) + '\n'
    table += head + divider

    # Выводим столько уровней, сколько нашли в логах
    for level, count in counts.items():
        table += f"{level:<17} | {count:<8}\n"
    return table

print(main(file, accent))