import random
impares = []
pares = []

numeros = [random.randint(0,100) for i in range (20)] 

for num in numeros: # "para cada numero num dentro de la lista numeros"
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
lista = pares + impares

print("Números generados:", numeros)
print("Nueva lista: ", lista)
