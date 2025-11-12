opcion = ""
while opcion != "E":
    print("T) Pulse T para generar un nuevo tablero")
    print("J) Pulse J para jugar")
    print("Pulse E para salir del juego")
    print("Elige una opción")
    opcion = input(("Introduce una opción: "))
    if opcion == "T":
        print("Generando tablero...")
    elif opcion == "J":
        print("Jugando")

print("Saliendo...")
print("Fuera del programa")