import sys
from typing import Callable
from colorama import init, Fore

init(autoreset=True)

cache = {}

def caching_fibonacci() -> Callable[[int], int]:
    
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    fib = caching_fibonacci()
    print(Fore.MAGENTA + f'\nВы можете ввести число. Для выхода, введите команду "quit"')
    while True:
        n = input(Fore.BLUE + '\nВведите желаемое число >>> ')
        if n == 'quit': 
            print(Fore.LIGHTGREEN_EX + '\nВсего доброго!\n')
            sys.exit(1)
        try:
            n = int(n)
            if n in cache:
                print(Fore.LIGHTYELLOW_EX + f'    --> Число {n} уже было в кеше: {cache[n]}')
                print(Fore.LIGHTGREEN_EX + f'\nЧисло Фибоначчи для {n}: {result}')
            else:
                result = fib(n)
                print(Fore.LIGHTGREEN_EX + f'\nЧисло Фибоначчи для {n}: {result}')
                print(Fore.CYAN + f'Новое значение {result} записано в кеш')
        except ValueError:
            print(Fore.RED + 'Вы ввели не число')

if __name__ == "__main__":
    main()
