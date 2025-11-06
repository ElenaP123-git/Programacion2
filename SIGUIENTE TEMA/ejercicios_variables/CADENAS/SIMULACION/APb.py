# Bucle principal
# Control de bucle
seguir = True

while seguir:
    primero = int(input("Introduce el primer número: "))
    segundo = int(input("Introduce el segundo número: "))

    if primero == 0 and segundo == 0:
        seguir = False
    else:
        while primero >= segundo:
            print("El primer número debe ser menor que el segundo.")
            primero = int(input("Introduce el primer número: "))
            segundo = int(input("Introduce el segundo número: "))

        tipo_intervalo = input("¿El intervalo es abierto (A) o cerrado (C)? ").upper()
        while tipo_intervalo != "A" and tipo_intervalo != "C":
            tipo_intervalo = input("Valor inválido. Introduzca A (abierto) o C (cerrado): ").upper()

        print("Impares que existen entre [", str(primero), " - ", str(segundo), "]:")

        contador = 0
        if tipo_intervalo == "A":
            inicio = primero + 1
            fin = segundo - 1
        else:
            inicio = primero
            fin = segundo

        i = inicio
        while i <= fin:
            if i % 2 != 0:
                print(i, end=", ")
                contador = contador + 1
            i = i + 1

        print("En total existen", contador, "números impares en el rango.")
