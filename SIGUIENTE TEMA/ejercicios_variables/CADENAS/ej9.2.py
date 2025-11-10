cadena = input("Escribe algo: ")

caracter1 = input("Escribe un caracter: ")
while len(caracter1) != 1:
    caracter1 = input("Por favor, escribe solo un carácter: ")

caracter2 = input("Escribe un segundo caracter: ")
while len(caracter2) != 1:
    caracter2 = input("Por favor, escribe solo un carácter: ")

if caracter1 in cadena:
    cadena = cadena.replace(caracter1, caracter2)
    print(cadena)
else:
    print("El primer carácter no aparece en la cadena")
