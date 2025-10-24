contador = 0
lista = []
while contador < 10:
    num = int(input("Introduce un número: "))
    contador += 1
    lista.append(num)
print("La lista es: ", lista)

maximo = max(lista) # A SORAYA NO LE GUSTA
minimo = min(lista)

for numeros in lista:
    if numeros == maximo:
        print(numeros, "--> máximo")
    elif numeros == minimo:
        print(numeros, "--> mínimo")
    else:
        print(numeros)

