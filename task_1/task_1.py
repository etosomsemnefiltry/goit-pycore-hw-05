'''
Завдання 1

Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного 
контексту, тобто з області, де вона була оголошена.

Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і 
повторного використання вже обчислених значень чисел Фібоначчі.

'''

'''
Более простой и соответствующий скучным условиям ДЗ вариант в файле task_1_proper.py
'''

import sys
from colorama import init, Fore

# Очистка раскраски строк для новых итераций
init(autoreset=True)

cache = {} # Словарь с кешем

def caching_fibonacci():
    # Замыкающая функция

    def fibonacci(n: int) -> int:
        
        # Обработка бозовый случаев
        if n <= 1:
            return n
        
        # Если значение есть в кеше, то вернем его
        if n in cache:
            return cache[n]
        
        # Если значения нет в кеше, то расчитаем с использованием рекурсии
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n] 

    return fibonacci 

def main():
    # Запуск интерактивной части

    # Инициируем и сохраним в переменной caching_fibonacci
    fib = caching_fibonacci()
    
    # Приветственное сообщение
    print(Fore.MAGENTA + f'\nВы можете ввести число. Для выхода, введите команду "quit"')

    # Запускаем бесконечный диалог с пользователем
    while True:
        n = input(Fore.BLUE + '\nВведите желаемое число >>> ')
        if n == 'quit': 
            print(Fore.LIGHTGREEN_EX + '\nВсего доброго!\n')
            sys.exit(1)
        
        # Пробуем, вдруг ввели не цифры, а что то другое
        try:
            n = int(n)

            if n in cache:
                # Если уже в кеше
                print(Fore.LIGHTYELLOW_EX + f'    --> Число {n} уже было в кеше: {cache[n]}')
            else:
                # Если нет в кеше
                # Защита от слишком больших чисел
                try: 
                    result = fib(n)
                    print(Fore.LIGHTGREEN_EX + f'\nЧисло Фибоначчи для {n}: {result}')
                    print(Fore.CYAN + f'Новое значение {result} записано в кеш')
                except RecursionError:
                    print(Fore.RED + 'Слишком большое число, введите меньше')

        except ValueError:
            print(Fore.RED + 'Вы ввели не число')

if __name__ == "__main__":
    main()