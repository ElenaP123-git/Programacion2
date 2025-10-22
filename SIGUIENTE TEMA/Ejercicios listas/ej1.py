lista_animales = ["Gato", "Zorro", "Perro","Dragón","Mariposa"]
animal = input("Dime un animal para buscar: ")


if animal in lista_animales: # "Si animal está en la lista de animales..."
    print("Lo tengo")
    print("Es el número de lista: ", lista_animales.index(animal))
else:
    print("no lo tengo")
print(lista_animales[:]) #para imprimir toda la lista
print(lista_animales[1:3]) #para imprimir a partir del número de lista que se escoja hasta donde quiera
