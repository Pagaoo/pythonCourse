contador = 1  # Isso é um contador
acumulador = 1  # Acumula algo, nesse caso contador + acumulador

while contador <= 10:
    print(contador)

    acumulador = acumulador + contador
    contador += 1
else:
    print(acumulador)
