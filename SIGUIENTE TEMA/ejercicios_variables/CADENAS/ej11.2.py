numero = input("Introduce un número entero: ")

valido = False
while valido == False:
    valido = True
    for letra in numero:
        if letra not in "0123456789":
            print("Por favor, introduce solo números.")
            numero = input("Introduce un número entero: ")
            valido = False

resultado = ""
contador = 0
i = len(numero) - 1

while i >= 0:
    resultado = numero[i] + resultado
    contador += 1
    if contador % 3 == 0 and i != 0:
        resultado = "." + resultado
    i -= 1

print("Número con separaciones de miles:", resultado)
