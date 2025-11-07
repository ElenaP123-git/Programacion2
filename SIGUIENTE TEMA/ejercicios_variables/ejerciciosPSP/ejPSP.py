nombres = []
puntuaciones = []
generos = []
puntuación = [] 

opcion = "" #para introducir datos mas adelante
while opcion != "S":
    print("Selecciona una de las siguientes opciones (R, E, S,P)")
    print("R. Registrar juegos")
    print("E. Mostrar estadísticas")
    print("S. Salir del programa")
    print("P. Mejor puntuación")
    print("D. Detalle de un juego")
    print("G. Filtrar por género")
    opcion = input("Opción: ")
    opcion = opcion.upper() #aquí es donde se introducen los nuevos datos de la variable vacía

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

    elif opcion == "P":
        mayor = puntuaciones[0] #recorrido desde el principio hasta el final
        for num in puntuaciones: #para 1,2,3,4... en recorrido de puntuaciones
            if num > mayor: #para buscar el mayor dato
                mayor=num #ya se detecta que número es mayor (se redefine la variable para que sea el mayor dato)
        posicion = puntuaciones.index(mayor)
        print(nombres[posicion], "Puntuación mas alta: ", puntuaciones[posicion],"Genero:",generos[posicion])
                
        #maximo = puntuaciones[0] #hace todo el recorrido desde el principio hasta el final para saber cual es el máximo
        #for i in range(len(puntuaciones)):
            #if i > maximo:
                #maximo = i #redefiniendo la variable por la que es mayor
        #posicion =puntuaciones.index(maximo) #cuidado porque el valor si no está,da error
        #print(nombre[posición],puntuaciones[posicion],generos[posicion])
    elif opcion == "D":
        nombre2 = input("Introduce un juego: ")
        if nombre2 in nombres:
            n = nombres.index(nombre2) #en la lista nombres, se indica la posición coincidente con el nombre introducido
            print(nombres[n],puntuaciones[n],generos [n]) #imprime la posición en la que está la opción coincidente de la lista
        else:
            print("No tenemos ese juego")

    elif opcion == "G":
        genero2 = input("Introduce el nombre de un género: ")
        listaplus = []
        for i in range(len(generos)):
            if generos[i] == genero2.lower():
                listaplus.append(i)
        if listaplus:
            for i in listaplus:
                print("Nombre:", nombres[i], "Género:", generos[i], "Puntuación:", puntuaciones[i])
        else:
            print("No hay juegos para ese género")

    else:
        print("Opción no válida. Intenta de nuevo.")
