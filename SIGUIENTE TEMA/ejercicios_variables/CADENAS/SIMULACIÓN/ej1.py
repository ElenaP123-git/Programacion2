clientes = []

opcion = ""
while opcion != "G":
    print("==========================================================")
    print("Amazon Guzmanes - Menú de opciones")
    print("A) Añadir cliente")
    print("V) Validar emails almacenados")
    print("C) Contar clientes de un dominio")
    print("M) Mostrar los % de clientes premium y normales")
    print("G) Salir")
    print("==========================================================")
    opcion = input("Selecciona una opción: ").upper()

    if opcion == "A":
        tipo = ""
        while tipo != "S" and tipo != "N":
            tipo = input("¿Es cliente premium? (S/N): ").upper()
        correo = input("Introduce el correo electrónico del cliente: ")
        clientes.append([correo, tipo])
        print("Cliente añadido correctamente.")

    elif opcion == "V":
        print("Validando emails...")
        for cliente in clientes:
            correo = cliente[0]
            if "@" in correo and "." in correo:
                print(correo + " → Válido")
            else:
                print(correo + " → Inválido")

    elif opcion == "C":
        dominio = input("Introduce el dominio a buscar (ej. gmail.com): ")
        contador = 0
        for cliente in clientes:
            correo = cliente[0]
            if correo.endswith("@" + dominio):
                contador = contador + 1
        print("Clientes con dominio '" + dominio + "': " + str(contador))

    elif opcion == "M":
        total = len(clientes)
        if total == 0:
            print("No hay clientes registrados.")
        else:
            premium = 0
            for cliente in clientes:
                if cliente[1] == "S":
                    premium = premium + 1
            normales = total - premium
            porcentaje_premium = premium * 100 / total
            porcentaje_normales = normales * 100 / total
            print("Premium: " + str(round(porcentaje_premium, 2)) + "%")
            print("Normales: " + str(round(porcentaje_normales, 2)) + "%")
    else:
        print("Opción no válida. Intenta de nuevo.")
if opcion == "G":
    print("Saliendo del programa. ¡Hasta pronto!")