"""
Programa que Imprima los numeros del 1 al 5 sumandolos y promediandolos. Mostrar el resultado por pantalla
"""

suma= 0
numero=1
contador=0

#Se usa un bucle while para sumar los numeros del 1 al 5
while(numero <=5):
    print("Numero: ",numero)
    suma += numero
    contador +=1
    numero +=1
promedio = suma / contador
print("La suma de todos es: ",suma)
print("Y Su Promedio es :", promedio)