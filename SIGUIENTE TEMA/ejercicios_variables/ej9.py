contador = 0
lista = []

while contador < 15:
    num = int(input("Introduce un número: "))
    contador +=1
    lista.append(num)
print("Lista oroginal:", lista)

ultimo_elemento = lista.pop() 
lista.insert(0, ultimo_elemento)
print("Lista Rotada:", lista)