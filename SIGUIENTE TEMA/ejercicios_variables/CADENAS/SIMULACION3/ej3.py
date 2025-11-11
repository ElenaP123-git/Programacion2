letra = input("Introduce una letra: ")
lista = []
stop = True

while stop:
    list = input("Introduce palabtras, introduce STOP si quieres parar: ") .upper()
    if list == "STOP":
        stop = False
    else:
        lista.append(list)
print("Fin programa")