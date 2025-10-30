# voltea.py
num = input("Introduce un número: ")
invertido = "" #cadena vacía

for i in range(len(num) - 1, -1, -1): #ej: 1234 --> 4 (len(num)) --> 3 (len(num)-1)-->(len(num)-1,-1) forma de decirle al bucle que pare justo después de llegar al índice 0 --> (len(num)-1,-1,-1) va hacia atrás (paso)
    #                                  i = 3,2,1,0
    invertido = invertido + num[i] # En cada vuelta del bucle, toma el carácter en la posición i y lo añade al final de invertido
    #                                se contruye el bucle al revés
print("Número invertido: ", invertido)
