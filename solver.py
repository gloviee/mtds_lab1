import math


def calculate(a: float, b: float, c: float) -> list:
    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return sorted([x1, x2]) if x1 != x2 else [x1]