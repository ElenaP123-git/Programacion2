cadena = input("Escribe algo: ")

caracter1 = input("Escribe un caracter: ")
while not (len(caracter1) == 1):
    print("Error: Debes escribir solo un carácter.")
    caracter1 = input("Escribe un caracter: ")

caracter2 = input("Escribe un segundo caracter: ")
while not (len(caracter2) == 1):
    print("Error: Debes escribir solo un carácter.")
    caracter2 = input("Escribe un segundo caracter: ")

# Reemplazo si el primer carácter está en la cadena
if caracter1 in cadena:
    cadena = cadena.replace(caracter1, caracter2)
    print("Cadena modificada:", cadena)
else:
    print("El primer carácter no aparece en la cadena.")
