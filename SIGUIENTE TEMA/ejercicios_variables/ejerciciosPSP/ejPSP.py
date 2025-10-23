nombres = []
puntuaciones = []
generos = []

opcion = ""
while opcion != "S":
    print("Selecciona una de las siguientes opciones (R, E, S)")
    print("R. Registrar juegos")
    print("E. Mostrar estadísticas")
    print("S. Salir del programa")
    opcion = input("Opción: ")
    opcion = opcion.upper()

    if opcion == "R":
        print("Registrando...")
        cantidad = input("¿Cuántos juegos quieres registrar? ")
        if cantidad >= "0":
            cantidad = int(cantidad)
            contador = 0
            while contador < cantidad:
                print("Juego", contador + 1)
                nombre = input("Nombre del juego: ")
                puntuacion = input("Puntuación (1 a 10): ")
                if puntuacion >= "0":
                    puntuacion = int(puntuacion)
                    if puntuacion >= 1 and puntuacion <= 10:
                        genero = input("Género (Acción, RPG, Deportes, etc.): ")
                        nombres += [nombre]
                        puntuaciones += [puntuacion]
                        generos += [genero]
                        contador += 1
                    else:
                        print("La puntuación debe estar entre 1 y 10.")
                else:
                    print("Puntuación inválida.")
        else:
            print("Cantidad inválida.")
    elif opcion == "E":
        print("Estadísticas:")
        print("Tu colección de juegos PSP:")
        i = 0
        while i < len(nombres):
            print(str(i + 1) + ". " + nombres[i] + " | Puntuación: " + str(puntuaciones[i]) + " | Género: " + generos[i])
            i += 1
        print()
    elif opcion == "S":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intenta de nuevo.")
