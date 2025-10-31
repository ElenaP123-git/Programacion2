# trozoDeNumero
num = input("Introduce un número: ")
inicio = int(input("Introduce el inicio: "))
fin = int(input("Introduce el final: "))
print(num[inicio -1:fin]) # "en la lista num, se imprime desde el inicio hasta el fin que se introduce"
# [inicio:fin]--> 1234567, 2, 5 --> 345
# [inicio:fin+1]--> 1234567,2,5 --> 3456
# [inicio-1:fin]--> 1234567,2,5 --> 2345 :)
# [inicio:fin-1] --> 123456,2,5 --> 34 :)