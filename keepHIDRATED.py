'''
Cuantos litros de agua debe tomar un ciclista por cada hora recorrida
'''
import math

def litres(time):
    # Multiplica el tiempo por 0.5 y redondea hacia abajo
    return math.floor(time * 0.5)

# Ejemplos de uso
print(litres(3))    # Debería devolver 1
print(litres(6.7))  # Debería devolver 3
print(litres(11.8)) # Debería devolver 5
