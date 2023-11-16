"""
Captura de 5 numeros y calcule el promedio, muestre el resultado por pantalla
"""
numeros=[] #declarando una variable tipo lista
promedio=0
x=0
while x<5:
    n=int(input("Ingrese un numero : ....."))
    numeros.append(n) #Agregar un elemento a la lista
    promedio=promedio+numeros[x] #acumulado o adicionando numero para luego calcular el promedio
    x=x+1 #modificador
print("Los elementos de la lista son:  .....",numeros,"\n")
promedio=promedio/5 #Calcula el problema de los numeros 
print("El promedio de los numeros ingresados en la Lista son: ",promedio,"\n")