dias_semana = ["Lunes", "Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
print(dias_semana[6])

import random
lista_num = []
for lista in range(0,5):
    aleatorio = random.randint(0,8)
    lista_num.append(aleatorio) #para introducir los datos aleatorios en la tabla
print(lista_num)
#OJITO

multiplos_3 = [i * 3 for i in range(1,21)] #para imprimir los 20 primeros múltiplos de 3
print(multiplos_3)

dias = ["martes","miercoles","jueves"] #para añadir a la lista anterior "martes, miercoles y jueves"
for dia in dias:
    multiplos_3.append(dia)
print(multiplos_3)

multiplos_3_diez = multiplos_3 [:10] #para imprimir 10 números que sean múltiplos de 3
print(multiplos_3_diez)