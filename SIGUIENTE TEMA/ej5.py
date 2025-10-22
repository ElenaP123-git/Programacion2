import random
lista1 = []
lista2 = []
lista3 = []

for i in range (1,21): #i = 1,2,3,4...20 (se imprimirán 20 números)
    num_aleatorio = random.randint (0,100) #el numero aleatorio será entre 0 y 100 (20 números)
    lista1.append(num_aleatorio) #en la lista1 se acumulan los 20 números aleatorios del 1 al 100
print(lista1)

for numeros in lista1: #para los números que hay en la lista1
    lista2.append(numeros**2) #en la lista2 aparecerán pero al cuadrado
print(lista2)

for numeros2 in lista1:
    lista3.append(numeros2**3) #podría haberlo puesto en el for de arriba XD
print(lista3)

for i in range(20):
    print(lista1[i]," ",lista2[i]," ",lista3[i])
