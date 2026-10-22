"""Простой консольный калькулятор."""


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание: из a вычитается b."""
    return a - b


def main():
    print("=== Калькулятор ===")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    print(f"Сумма: {add(a, b)}")
    print(f"Разность: {subtract(a, b)}")


if __name__ == "__main__":
    main()
