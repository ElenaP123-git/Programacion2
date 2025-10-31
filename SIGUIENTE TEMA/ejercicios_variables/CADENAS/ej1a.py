#esCapicua (como le gusta a Soraya)
numero = input("Introduce un número: ")
invertido = ""

for i in range(len(numero) - 1, -1, -1):
    invertido = invertido + numero[i]
if numero == invertido:
    print("Es capicúa")
else:
    print("No es capicúa")

# ó

# num = input("Introduce un número: ")
#invertido = ""
#indice = len(num) - 1
#while indice >= 0:
#    invertido = invertido + num[indice]
#    indice = indice - 1
#print("Número invertido:", invertido)

# MUY DIFÍCIL :´//