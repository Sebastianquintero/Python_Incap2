"""
Lista que captura N numeros hasta que el usuario ingrese el 0, devolviendo el menor, mayor y longitud de cadena
"""

numeros=[] #lista
n=int(input("Ingrese un numero ..."))
numeros.append(n)
while(n!=0):
    n=int(input("Ingrese un numero ..."))
    numeros.append(n)
    if n==0:
        break
print("Los Valores ingresados son: ",numeros)
mayor=numeros[0]
menor=numeros[0]
fin=len(numeros)
for x in range(1,fin):
    if numeros[x]>mayor: #10>8
        mayor=numeros[x] #10
    elif numeros[x]<menor:
        menor=numeros[x]
print("La cantidad ingresada fue: ",fin)
print("El Mayor es: ",mayor)
print("El menor es: ",menor)