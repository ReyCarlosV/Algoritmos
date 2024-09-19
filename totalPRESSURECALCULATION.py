def total_pressure(M1, M2, m1, m2, V, T):
    # Constante del gas ideal
    R = 0.082

    # Convertir la temperatura a Kelvin
    T_kelvin = T + 273.15

    # Calcular la fracción molar de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la fórmula
    P_total = (n1 + n2) * R * T_kelvin / V

    return P_total


# Ejemplos de uso
print(total_pressure(28, 32, 10, 20, 10, 25))  # Ejemplo con valores ficticios