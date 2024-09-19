import math


def convert_to_16_9(x, y):
    # Calcula el nuevo ancho manteniendo la altura (y) y ajustando a la proporción 16:9
    new_x = math.ceil(y * 16 / 9)

    # Devuelve las nuevas dimensiones en una tupla (ancho, altura)
    return new_x, y


# Ejemplo de uso
original_x, original_y = 374, 280
new_x, new_y = convert_to_16_9(original_x, original_y)
print(f"Original resolution: {original_x}x{original_y}")
print(f"New resolution (16:9): {new_x}x{new_y}")
