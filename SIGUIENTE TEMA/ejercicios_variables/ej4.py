lista = []

contador = 0
while contador < 10:
    num = int(input("Introduce un número: "))
    contador = contador + 1
    lista.append(num)
print(lista)
print(lista[::-1]) #si pongo [:-1] lo imprime todo menos el último número introducido

 #for i in reversed(lista):  for numero in lista [::-1]:
 #  print(i)                    print(numero)
