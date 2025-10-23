lista = []
contador = 0
while contador < 12:
    temperatura = float(input("Introduce la temperatura media de cada mes: "))
    contador += 1
    lista.append(temperatura)
print("La temperatura media de todos los meses es: ", lista)

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre","octubre", "noviembre", "diciembre"]
for i in (meses): #para enero, febrero... en lista meses
    print("La temperatura media en", meses[i], "fue", "*" * int(lista[i]), "(", lista[i], "ºC)")
