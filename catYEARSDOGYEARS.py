'''
Un programa que calcula la edad de un gato y un perro con respecto a la de los humanos
'''
def animal_ages(humanYears):
    # Inicializamos los años de gato y perro
    catYears = 0
    dogYears = 0

    # Si el humano tiene al menos un año
    if humanYears >= 1:
        # Primer año: 15 años tanto para el gato como para el perro
        catYears += 15
        dogYears += 15

    # Si el humano tiene al menos dos años
    if humanYears >= 2:
        # Segundo año: 9 años adicionales tanto para el gato como para el perro
        catYears += 9
        dogYears += 9

    # Si el humano tiene más de dos años
    if humanYears > 2:
        # Por cada año adicional: 4 años para el gato y 5 años para el perro
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    # Devolvemos los años humanos, años de gato y años de perro en una lista
    return {
        "humanYears": humanYears,
        "catYears": catYears,
        "dogYears": dogYears
    }

# Ejemplo de uso
print(animal_ages(3))  # Debería devolver [3, 28, 29]
print(animal_ages(10))
print(type(animal_ages(3)))