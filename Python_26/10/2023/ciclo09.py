"""
Realizar un programa ue solicite por teclado 10 notas de alumnos y nos informe cuantos tienen notas mayores o iguales
a 3.5 y cuantos menores
"""

import math
mayor=0 #Acumuladores
menor=0 #Acumuladores
nota=1 #condicion inicial
while(nota<=10): #condicion final
    num=float(input("Ingrese el valor de la nota..."))
    if nota>=3.5:
        mayor=mayor+1
    else:
        menor=menor+1

    nota=nota+1
print("La cantidad de notas ingresadas mayores a 3.5 son: ",mayor,"\n La cantidad de notas ingresadas menores a 3.5 son: ",menor)
print("****** Ultima Linea *******")