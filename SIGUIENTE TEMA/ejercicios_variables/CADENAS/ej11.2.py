numero = input("Introduce un número entero: ")
resultado = ""
contador = 0

for i in range(len(numero) - 1, -1, -1):
    resultado = numero[i] + resultado
    contador += 1
    # Agregamos un punto cada 3 dígitos, excepto si es el primero
    if contador % 3 == 0 and i != 0:
        resultado = "." + resultado

print("Número con separadores de miles:", resultado)
