def third_angle(angle1, angle2):
    # Sumar los dos ángulos y restar de 180 para obtener el tercero
    return 180 - (angle1 + angle2)

# Ejemplos de uso
print(third_angle(60, 60))  # Debería devolver 60
print(third_angle(45, 90))  # Debería devolver 45
