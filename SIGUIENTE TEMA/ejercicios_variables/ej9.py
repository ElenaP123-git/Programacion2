contador = 0
lista = []

while contador < 15:
    num = int(input("Introduce un número: "))
    contador +=1
    lista.append(num)
print("Lista oroginal:", lista)

ultimo_elemento = lista.pop() # elimina el último elemento de la lista
lista.insert(0, ultimo_elemento) # añade el último elemento a la posición 0 (la primera)
print("Lista Rotada:", lista)