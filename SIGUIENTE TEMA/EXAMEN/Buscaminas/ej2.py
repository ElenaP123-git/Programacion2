import random
opcion = ""
while opcion != "E":
    print("T) Pulse T para generar un nuevo tablero")
    print("J) Pulse J para jugar")
    print("E) Pulse E para salir del juego")
    print("Elige una opción")
    opcion = input(("Introduce una opción: ")) . upper()
    if opcion == "T":
        print("Generando tablero...")
        tablero = []
        tableroSigno=[]
        aleatorio = [random.randint(0,1) for i in range (8)] # me va a dar 8 números del 0-1
        tablero.append(aleatorio)
        for i in tablero:
            if i == "0":
                tableroSigno.append(" ")
            elif i == "1":
                tableroSigno.append("X")
        print("¡Tablero generado! Se han escondido 3 minas. Tablero: ", tableroSigno)

    elif opcion == "J":
        print("Jugando")
        
print("Saliendo...")
print("Fuera del programa")