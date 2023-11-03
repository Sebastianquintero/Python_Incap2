# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:08:58 2023

@author: Estudiante
"""

"""
Programa que permite al usuario capturar los datos de un estudiante, la funcion debe calcular la definitiva devolviendo el resultado al programa principal el cual clasifica
la definitiva
"""

def definitiva():
    x=0
    for z in range(1,4):
        nota=float(input("Ingrese una nota..."))
        x=x+nota #almacena el valor de cada una de las notas
    x=x/3 #calcula la definitiva
    return x #retorna o devuelve al programa principal el resultado de definitiva






#programa principal

print("Ejemplo de funciones con parametros y retorno de valores \n")
print("********************** \n")
nombre=input("Ingrese un nombre...")
curso=input("Ingrese curso actual ...")
promedio=definitiva() #variable que retorna valores
if promedio<3.0:
    estado="Reprovado"
elif promedio>=3.0 and promedio<=4.0:
    estado="Aprovado"
elif promedio>4.0:
    estado="Excelente"
print("REPORTE ESTADO \n NOMBRE :",nombre.upper(),"\n CURSO :",curso.upper(),"\n Definitiva: ",promedio,"\n")
print("Estado: ",estado.title())
print("**********************************************************")