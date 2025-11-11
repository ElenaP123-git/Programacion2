edad =[]
altura= []
contador = 1
opcion = ""
árboles = []
diametro = []

while opcion != "E":
    print("A: Introduzca el número de árboles que va a introducir")
    print("B: Introducir diámetro, edad y altura árbol")
    print("C: Mostrar el resumen de los datos guardados")
    print("D: Resumen recuadro")
    print("E: Salir del programa")
    print("F: Tipo, árbol con mayor altura y diámetro")
    print("G: Tipo, diametro y altura")
    
    opcion = input(("Elige una opción (A-E): ")) .upper()
    
    if opcion == "A":
        a = int(input(("Introduce el número de árboles que quieras: ")))
        for i in range (a):
            aa = input(("Introduce el árbol: "))
            árboles.append(aa)
        print("Lista generada: ", árboles)

    elif opcion == "B":
        if len(árboles) == 0:
            print("Primero debes introducir los árboles (opción A).")
        else:
            for i in range(len(árboles)):
                print("TE PREGUNTA POR CADA ÁRBOL(",contador,") -",árboles[i])
                d = float(input("Introduce el diámetro: "))
                e = int(input("Introduce la edad: "))
                alt = float(input("Introduce la altura: "))
                contador +=1
                diametro.append(float(d))
                edad.append(int(e))
                altura.append(float(alt))


    elif opcion == "C":
        print("RESUMEN DATOS:")
        print("Hay", len(árboles), "árboles: ", árboles)
        print("Diámetros guardados (", len(diametro), "): ", diametro)
        print("Edades guaraddas (", len(edad), "): ", edad)
        print("Alturas guardadas (", len(altura), "): ", altura)
        
    elif opcion == "D":
        if len(altura) == 0:
            print("La lista de alturas está vacía.")
        else:
            mayor = altura[0]
            menor = altura[0]
            for x in altura:
                if x > mayor:
                    mayor = x
                elif x < menor:
                    menor = x

        # MEDIA EDAD
        if len(edad) == 0:
            print("No hay edades válidas para calcular la media.")
        else:
            total = 0
            for i in range(len(edad)):
                total += int(edad[i])  # Convertimos cada elemento a entero y los sumamos
            media_edad = total / len(edad)
            print("La edad media de los árboles es:", media_edad, "años")

        print("La altura máxima es: ", mayor)
        print("La altura mínima es: ", menor)
        print("Existen", len(árboles), "árboles en total de más de", menor, "m")

    elif opcion == "F":
        if len(altura) == 0:
            print("No hay alturas registradas.")
        else:
            mayor2 = altura[0] # recorro la lista
            posicion = 0 # ASÍ GUARDA LA ALTURA MAYOR    ojo piojo
            for i in range(len(altura)):
                if altura[i] > mayor2:
                    mayor2 = altura[i]
                    posicion = i

            print("Árbol con mayor altura:")
            print("Tipo:", árboles[posicion])
            print("Altura:", altura[posicion])
            print("Diámetro:", diametro[posicion])

    elif opcion == "G":
        if len(árboles) == 0:
            print("No hay árboles registrados.")
        else:
            print("Listado de árboles:")
            for i in range(len(árboles)):
                print("[", árboles[i], ",", diametro[i], ",", altura[i], "]") # WHAAAAAAAAAAT locura

print("Fuera del programa")