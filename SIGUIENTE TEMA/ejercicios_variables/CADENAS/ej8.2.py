cadena = input("Introduce nombre y apellidos: ")
partes = cadena.split()
resultado = ""

for palabra in partes:
    if len(palabra) > 0:
        resultado += palabra[0].upper() + palabra[1:].lower() + " "

print(resultado.strip())

#OJO :,)