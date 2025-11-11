opcion = ""
árboles = []
diametro = []
edad =[]
altura= []
contador = 0

while opcion != "E":
    print("A: Introduzca el número de árboles que va a introducir")
    print("B: Introducir diámetro, edad y altura árbol")
    print("C: Mostrar el resumen de los datos guardados")
    print("D: Resumen recuadro")
    print("E: Salir del programa")
    opcion = input(("Elige una opción (A-E): ")) .upper()
    
    if opcion == "A":
        a = int(input(("Introduce el número de árboles que quieras: ")))
        for i in range (a):
            aa = input(("Introduce el árbol: "))
            árboles.append(aa)
            print("Lista generada: ", árboles)
    elif opcion == "B":
        d = input("Introduce el diámetro: ")
        e = ("Introduce la edad: ")
        alt = ("Introduce la altura: ")
        if d < alt:
            print("Brah, thats weird")
            d = input("Introduce el diámetro: ")
            e = ("Introduce la edad: ")
            alt = ("Introduce la altura: ")
        else:
            diametro.append(d)
            edad.append(e)
            altura.append(alt)
            print("Edad:", e, "años")
            print("Diámetro:", d, "cm")
            print("Altura: ", alt, "m")

    elif opcion == "C":
        print("RESUMEN DATOS:")
        print("Hay", len(árboles), "árboles: ", árboles)
        print("Diámetros guardados (", len(diametro), "): ", diametro)
        print("Edades guaraddas (", len(edad), "): ", edad)
        print("Alturas guardadas (", len(altura), "): ", altura)
        
    elif opcion == "D":
        print("La altura máxima es: ")
        print("La altura mínima es: ")
        print("La edad media para los de tipo B es")
        print("Existen",len(árboles), "árboles en total de más de",edad)
print("Fin del programa")


