seguir = True
impares = []

while seguir:
    primero = int(input("Introduce el primer número: "))
    segundo = int(input("Introduce el segundo número: "))

    if primero == 0 and segundo == 0:
        print("FIN")
        seguir = False
    else:
        while primero >= segundo:
            print("El primer número debe ser menor que el segundo.")
            primero = int(input("Introduce el primer número: "))
            segundo = int(input("Introduce el segundo número: "))

        print("Impares que existen entre [", str(primero), " - ", str(segundo), "]:")

        # tuve que buscar ayuda aquí
        
        i = primero
        impares = []
        while i <= segundo:
            if i % 2 != 0:
                impares.append(i) # imprime números impares1
            i = i + 1

        print(impares)

        # CORRECCIÓN, USAR LISTA