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
dias_semana.remove ("Martes") #para borrar por valor (sólo elimina el primer elemento de la lista con ese nombre)
print(dias_semana)
#NUEVA LISTA
animales = ["perro","zorro","dragón","perro"]
animales.remove ("perro")
print(animales)
#FIN NUEVA LISTA

print(len(dias_semana)) #para indicar el número de elementos que hay en la lista

for dias in dias_semana: #para imprimir cada dato de la lista
    print(dias)
for dias in range (len(dias_semana)): #lo mismo que arriba
    print(dias_semana[dias])
for i in reversed (dias_semana): #para imprimir al revés la lista  A SORAYA NO LE GUSTA 
    print(i)

print(dias_semana.index("Lunes")) #para saber la posición en la que está el dato en la lista
if "Lunes" in dias_semana: #para saber si tengo ese elemento en la lista
    print("lo tengo")
else:
    print("no lo tengo")

print(dias_semana[1]) #para imprimir el dia de la semana que indicas

for x in "banana":
    print(x) # te dice todos los caracteres letra por letra

txt = "The best things in life are free!"
print("free" in txt) #true
print("expensive" not in txt) #true

print(dias_semana[1:4]) #se imprime todo de la lista entre el 1 y el 4
print(dias_semana[0:len(dias_semana)]) #imprime lista completa
print(dias_semana[-len(dias_semana)])  #imprime solo lo primero de la lista porque lo elimina todo desde atrás
print(dias_semana[:-len(dias_semana)]) #imprime todo eliminado 
print(dias_semana[::-1]) #imprime la lista al revés A SORAYA NO LE GUSTA
print(dias_semana[:-1]) #imprime todos los elementos de la lista menos el último (resta los últimos elementos desde el principio) 
                        # por eso print(dias_semana[:-2]) elimina los últimos 2