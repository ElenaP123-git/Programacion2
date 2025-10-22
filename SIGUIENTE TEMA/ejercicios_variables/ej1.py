lista_animales = ["gato", "zorro", "perro","dragón","mariposa"]
animal = input("Dime un animal para buscar: ") . lower()


if animal in lista_animales: # "Si animal está en la lista de animales..."
    print("Sí tengo", animal)
    print("Es el número de lista: ", lista_animales.index(animal))
else:
    print("no tengo a", animal)

print(lista_animales[:]) #para imprimir toda la lista
print(lista_animales[1:3]) #para imprimir a partir del número de lista que se escoja hasta donde quiera