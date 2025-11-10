seguir = True
lista = []

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

        tipo_intervalo = input("¿El intervalo es abierto (A) o cerrado (C)? ").upper()
        while tipo_intervalo != "A" and tipo_intervalo != "C":
            tipo_intervalo = input("Valor inválido. Introduzca A (abierto) o C (cerrado): ").upper()

        print("Impares que existen entre [", str(primero), " - ", str(segundo), "]:")

        # help
        if tipo_intervalo == "A":
            inicio = primero + 1
            fin = segundo - 1
        else:
            inicio = primero
            fin = segundo

        lista = []
        i = inicio
        while i <= fin:
            if i % 2 != 0:
                lista.append(i)
            i = i + 1
        print(lista)
