import random

pares = []
impares = []

# Generar 20 números aleatorios entre 0 y 100
numeros = [random.randint(0, 100) for i in range(20)]
print("Lista original:", numeros)

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Combinar pares primero, luego impares
resultado = pares + impares
print("Lista con pares primero:", resultado)