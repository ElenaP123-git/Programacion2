impares=[]
salir = False
numVeces = 0
while not salir:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un segundo número: "))
    
    # Si num2 es múltiplo de num1, salimos
    if num2 % num1 == 0:
        print("Saliendo del Programa")
        salir = True
    else:
        for i in range(num2,num1,-2): # hasta que no termino este bucle, no paso al siguiente if
            if i % 2 != 0: 
                print(i)
                impares.append(i)
    print("En total existen", len(impares), "números impares en el rango")
    print("=========================================")
    if numVeces>2: # el siguiente if
        salir=True
        numVeces += 1
    else:
        numVeces+1
    impares=[]
print("FIN")    