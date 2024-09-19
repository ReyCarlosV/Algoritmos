'''
Calcula el minimo y maximo de la edad compatible contigo
'''
import math


def dating_range(age):
    if age > 14:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(dating_range(27))  # Debería devolver "20-40"
print(dating_range(5))  # Debería devolver "4-5"
print(dating_range(17))  # Debería devolver "15-20"
print(dating_range(20))