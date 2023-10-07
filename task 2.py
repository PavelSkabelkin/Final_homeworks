def remember(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print(f"Кэширован результат для {args}")
        else:
            print(f"Использован кэшированный результат для {args}")
        return cache[key]

    return wrapper

@remember
def fibonacci(n):
    if n <= 0:
        return "Пожалуйста, введите положительное целое число."

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

try:
    n = int(input("Введите номер числа Фибоначчи: "))
    result = fibonacci(n)
    print(f"Число Фибоначчи с номером {n}: {result}")

except ValueError:
    print("Пожалуйста, введите целое число.")
