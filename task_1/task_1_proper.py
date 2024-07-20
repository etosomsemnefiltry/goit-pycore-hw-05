'''
Завдання 1

Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного 
контексту, тобто з області, де вона була оголошена.

Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і 
повторного використання вже обчислених значень чисел Фібоначчі.

'''

def caching_fibonacci():
    cache = {} # Создаем словарь

    def fibonacci(n: int) -> int:

        # Обработка базовых случаев
        if n <= 1:
            return n
        
        # Если значение уже в кеше, вернем его
        if n in cache:
            return cache[n]

        # Если значения в кеше нет, рассчитаем
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Вернем результат расчета
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610