#EJERCICIO 6 COMO LE GUSTA A SORAYA

lista = []
contador = 0
while contador < 10:
    num = int(input("Introduce un número: ")) #otra forma de hacer el contador for i in range (0,10)
    contador += 1                             #                                     numero = int(input("Dame un número: "))
    lista.append (num)                        #                                     lista.append(numero)
print("La lista es: ", lista)

mayor = lista[0] #se inicializan las variables mayor y menor con el primer número de la lista
menor = lista[0]

for numeros in lista: # se recorre cada número n de la lista
    if numeros > mayor: #si n es mayor que el actual mayor, se actualiza
        mayor=numeros 
    elif numeros < menor: #si n es menor que el actual número, se actualiza
        menor= numeros

print(lista)
print("El número mayor es: ", mayor)
print("El número menor es: ", menor)

