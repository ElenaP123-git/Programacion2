#EJERCICIO 6 COMO LE GUSTA A SORAYA

lista = []
contador = 0
while contador < 10:
    num = int(input("Introduce un número: ")) #otra forma de hacer el contador for i in range (0,10)
    contador += 1                             #                                     numero = int(input("Dame un número: "))
    lista.append (num)                        #                                     lista.append(numero)
print("La lista es: ", lista)

mayor = lista[0] # todo se lee a partir del primer dato de la lista (los números de abajo)
menor = lista[0]

for numeros in lista: # por cada numero introducido en la lista
    if numeros > mayor: #si algún número es mayor que los otros
        mayor=numeros  # ese número es el mayor
    elif numeros < menor: #si algún número es menor que los otros
        menor= numeros # ese número es el menor
        
print("El número mayor es: ", mayor)  
print("El número menor es: ", menor) 