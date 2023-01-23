from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def calculate_square_root(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> None:
    """Вычисляет квадратный корень из введенного числа."""
    if your_number <= 0:
        return None
    else:
        result = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f' Это будет: {result}')
        return None


calc(25.5)
