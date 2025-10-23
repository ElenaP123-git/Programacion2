#EJERCICIO 6 COMO LE GUSTA A SORAYA
lista = []
contador = 0
while contador < 10:
    num = int(input("Introduce un número: "))
    contador += 1
    lista.append (num)
print("La lista es: ", lista)

mayor = lista[0]
menor = lista[0]

for n in lista:
    if n > mayor:
        mayor=n
    elif n < menor:
        menor= n

print(lista)
print("El número mayor es: ", mayor)
print("El número menor es: ", menor)