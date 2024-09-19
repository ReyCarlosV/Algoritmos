def nba_extrap(ppg, mpg):
    # Si los minutos jugados son 0, retornar 0
    if mpg == 0:
        return 0

    # Extrapolar los puntos por 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondear a la décima más cercana
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Debería devolver 28.8
print(nba_extrap(10, 10))  # Debería devolver 48
print(nba_extrap(5, 17))  # Debería devolver 14.1
print(nba_extrap(0, 0))  # Debería devolver 0
