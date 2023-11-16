"""
suma de elementos de una lista
"""

suma=0 #acumulador
lista01=[10,7,3,7,2] #asignado elementos a una lista
n=len(lista01) #calcula la longitud de una lista
x=0 #c
while x<n:
    suma=suma+lista01[x] #adiciona a la variable suma el contenido de la lista en la posicion[n]
    x=x+1 #modificador para ir desplazando sobre la lista
print("Los elementos de la lista son: ",lista01,"\n")
print("El resultado de sumar los elementos de la lista es: ",suma,"\n")
print("La longitud de la lista es: ",n)