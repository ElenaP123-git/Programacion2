contador = 0
lista = []

while contador < 15: #contador
    num = int(input("Introduce un número: "))
    contador += 1
    lista.append(num)
print("Lista original:", lista) 

n = int(input("¿Cuántas veces quieres rotar la lista hacia la derecha? "))

if n < len(lista): # "si n es menor que los números introducidos en la lista"
    for i in range(n): # n es el numero de veces que este bucle da vueltas, si num = [1,2,3,4,5] y n = 3 ==> [3,4,5,1,2]
#                      mientras i es la cantidad de num que hay (5) --> (0,1,2,3,4)
#                      lo que hace que los números cambien de posición es el pop y el insert
        ultimo_elemento = lista.pop() #sustituir el último elemento por el primero
        lista.insert(0, ultimo_elemento)
    print("Lista rotada:", lista)
else:
    print("El número debe ser menor que", len(lista))
