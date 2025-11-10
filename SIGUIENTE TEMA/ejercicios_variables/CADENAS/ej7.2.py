cadena = input("Escribe nombre y apellidos: ")
cadena2 = cadena.split(" ")
a = "a"
b = "b"
c = "c"
for i in cadena2:
    if a == "a":
        a = i[0]
        x = a.upper()
    elif b == "b":
        b = i[0]
        y = b.upper()
    elif c == "c":
        c = i[0]
        z = c.upper()
print("Tus iniciales son: ", x,y,z)
