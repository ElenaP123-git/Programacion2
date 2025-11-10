seguir = True

while seguir:
    primero = int(input("Introduce el primer número: "))
    segundo = int(input("Introduce el segundo número: "))

    if primero == 0 and segundo == 0:
        seguir = False # sale del while
    else:
        while primero >= segundo:
            print("El primer número debe ser menor que el segundo.")
            primero = int(input("Introduce el primer número: "))
            segundo = int(input("Introduce el segundo número: "))

        print("Impares que existen entre [" + str(primero) + " - " + str(segundo) + "]:")

        # help
        contador = 0
        i = primero
        while i <= segundo:
            if i % 2 != 0:
                print(i)
                contador = contador + 1
            i = i + 1

        print("En total existen", contador, "números impares en el rango.")
