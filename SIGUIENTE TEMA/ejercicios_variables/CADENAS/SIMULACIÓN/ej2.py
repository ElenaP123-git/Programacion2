clientes = []

opcion = ""
while opcion !="G":
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
        incorrectos = []
        for cliente in clientes:
            correo = cliente[0]
            if "@" in correo:
                posicion_arroba = correo.index("@")
                parte_derecha = correo[posicion_arroba+1:]
                if "." in parte_derecha:
                    print(correo + " → Válido")
                else:
                    print(correo + " → Inválido")
                    incorrectos.append(correo)
            else:
                print(correo + " → Inválido")
                incorrectos.append(correo)
        print("Cantidad de emails incorrectos: " + str(len(incorrectos)))
        if len(incorrectos) > 0:
            print("Emails incorrectos:")
            for email in incorrectos:
                print(email)
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
    
