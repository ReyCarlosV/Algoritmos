def mango(quantity, price):
    # Número de mangos por los que se paga
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Costo total
    total_cost = paid_mangoes * price

    return total_cost


# Ejemplos de uso
print(mango(2, 3))  # Debería devolver 6
print(mango(3, 3))  # Debería devolver 6
print(mango(5, 3))  # Debería devolver 12
print(mango(9, 5))  # Debería devolver 30