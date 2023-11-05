# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:47:39 2023

@author: Estudiante
"""

"""
Programa que capture dos numero y permite al usuario seleccionar entre sumarlos o multiplicarlos (por medio de funciones)
"""

def suma(a,b):
    #a -> n1   b ->n2
    respuesta=a+b
    print("El resultado de sumar los numeros: ",a," + ",b," = ",respuesta)
    
def multiplicar(a,b):
    respuesta=a*b
    print("El resultado de multiplicar los numeros: ",a," * ",b," = ",respuesta)



#programa principal

print("OPERACIONES BASICAS \n")
n1=int(input("Ingrese el primer numero...."))
n2=int(input("Ingrese el segundo numero ...."))
menu=int(input("Seleccionar la operacion a realizar \n 1.Suma \n 2.Multiplicacion"))
if menu==1:
    suma(n1,n2)
else:
    multiplicar(n1,n2)
