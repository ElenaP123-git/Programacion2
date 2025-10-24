lista = []
contador = 0
while contador < 12:
    temperatura = float(input("Introduce la temperatura media de cada mes: "))
    contador += 1
    lista.append(temperatura)
print("La temperatura media de todos los meses es: ", lista)

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre","octubre", "noviembre", "diciembre"]
for i in range (len(meses)): #genera numeros del 0 al 11
    print("La temperatura media en", meses[i], "fue", "*" * int(lista[i]), "(", lista[i], "ºC)")
#                     accede a elementos de le lista meses,     accede a elementos de lista correspondientes
# se pone int en la lista para poder multiplicar 