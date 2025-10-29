contador = 0
lista = []

while contador < 15:
    num = int(input("Introduce un número: "))
    contador +=1
    lista.append(num)
print(lista)

lista.insert(0,14)
