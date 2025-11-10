contador = 0
lista = []

while contador < 15: #contador
    num = int(input("Introduce un número: "))
    contador += 1
    lista.append(num)
print("Lista original:", lista) 

n = int(input("¿Cuántas veces quieres rotar la lista hacia la derecha? "))

if n < len(lista): 
    for i in range(n): # para todos los números introducidos en n
        ultimo_elemento = lista.pop() # se quitarán los últimos números de la lista elegidos en n
        lista.insert(0, ultimo_elemento) # se insertan delante
    print("Lista rotada:", lista)
else:
    print("El número debe ser menor que", len(lista))
