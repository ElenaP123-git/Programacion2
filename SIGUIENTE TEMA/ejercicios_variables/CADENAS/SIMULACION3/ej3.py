letra = input("Introduce una letra: ")
lista = []
stop = True # ojito, que sin esto no furula

while stop:
    list = input("Introduce palabtras, introduce STOP si quieres parar: ") .upper()
    if list == "STOP":
        stop = False
    else:
        lista.append(list)

print("La letra introducida es: ", letra)
print("La lista de palabras es: ", lista, "y el número de palabras es: ", len(lista))


