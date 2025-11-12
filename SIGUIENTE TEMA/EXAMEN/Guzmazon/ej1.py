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

for i in range(len(productos)):
    print("Lista productos:","[", productos[i], ",", precio[i],"]")
print("Importe máximo a gastar: ", dinero)
print("Productos: ", productos)
print("Precios: ",precio)
print("Coste total de cesta: ", total)





