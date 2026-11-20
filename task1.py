
def caching_fibonacci():
    # Створюємо словник для кешування чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Базові випадки рекурсії
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевіряємо, чи є результат у кеші
        if n in cache:
            return cache[n]

        # Обчислюємо число Фібоначчі та зберігаємо його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


# Перевірка роботи функції
fib = caching_fibonacci()

print(f"Число Фібоначчі для 0: {fib(0)}")
print(f"Число Фібоначчі для 1: {fib(1)}")
print(f"Число Фібоначчі для 10: {fib(10)}")
print(f"Число Фібоначчі для 15: {fib(15)}")
print(f"Число Фібоначчі для 148: {fib(148)}")