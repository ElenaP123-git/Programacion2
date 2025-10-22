dias_semana = ["Lunes", "Martes", "Jueves"]
#                 0        1          2
print(dias_semana[1]) 
print(dias_semana[-1])
dias_semana.insert(2,"Miércoles") #para introducir datos donde quiera
dias_semana.append("Viernes") #para introducir datos al final de la tabla
print(dias_semana)

dias_finde = ["Sábado", "Domingo"]
dias_semana = dias_semana + dias_finde #fusionamos ambas listas
print(dias_semana)

dias_semana.pop(6) #para borrar por posición
dias_semana.remove ("Martes") #para borrar por valor
print(dias_semana)

print(len(dias_semana)) #para indicar el número de elementos que hay en la lista

for dias in dias_semana: #para imprimir cada dato de la lista
    print(dias)
for dias in range (len(dias_semana)): #lo mismo que arriba
    print(dias_semana[dias])
for i in reversed(dias_semana): #para imprimir al revés la lista
    print(i)

print(dias_semana.index("Lunes")) #para saber la posición en la que está el dato en la lista

print(dias_semana[1]) #para imprimir el dia de la semana que indicas

for x in "banana":
    print(x) # te dice todos los caracteres letra por letra

txt = "The best things in life are free!"
print("free" in txt) #true

print("expensive" not in txt) #true