dinero = float(input("Introduce el dinero máximo que te quieres gastar en la compra: "))
productos = []
precio =[]
p = True
total = 0
contador = 1

while total < dinero:
        print("PRODUCTO: ", contador)
        nomp = str(input("Introduce nombre del producto: "))
        prc = float(input("Introduce el precio del producto: "))
        precio.append(prc)
        productos.append(nomp)
        for i in range(len(precio)):
                    total += float(precio[i]) # suma todos los precios
        contador +=1

prod_sobra = productos[:-1]
print("La suma de los precios superó el importe máximo (", dinero, "€ )")
print("Lista dentro de presupuesto: ", prod_sobra)

print("Importe máximo a gastar: ", dinero)
print("Productos: ", productos)
print("Precios: ",precio)
print("Coste total de cesta: ", total)

src = True  # ej 2
opcion = ""
while src:
    print("S: Para calcular dinero sobrante")
    print("R: Eliminar un producto y su precio en la lista")
    print("C: Devolver lista cuyp precio es más alto que el importe")
    opcion = ("Introduce una opción: ")
    if opcion != "S" and opcion !="R" and opcion != "C":
           print("Inválido")
           src = False
    elif opcion == "S": # ej 3
        resta = dinero - total
        print("Resta entre importe que quería gastar y suma de los precios")
    
    elif opcion == "R":  # ej 4
        print("Los productos son: ", productos)
        for i in range(len(productos)):
            print("Lista productos introducidas:","[", productos[i], ",", precio[i],"]")
        pr = input(("Introduce el producto que quiere eliminar: "))
        if pr in productos:
            x = input("Seguro que lo quieres eliminar?? (S/N): ")
            if x == "S":
                productos.remove(pr)
        for i in range(len(productos)):
            print("Lista productos final:","[", productos[i], ",", precio[i],"]")

    elif opcion == "C":
          imp = ("Introduce importe: ")
          lista = []
          # no terminado