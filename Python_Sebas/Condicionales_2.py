# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:18:00 2023

@author: Estudiante
"""

"""
Programa que capture dos numeros y determine cual es el mayor y cual es el menor
"""

num=int(input("Ingrese un numero: "))
num1=int(input("Ingrese el segundo numero: "))
if num>num1:
    print("El Primer numero :",num,"es mayor que el segundo numero ",num1)
elif num1>num:
    print("El Segundo Numero: ",num1,"es mayor que el primer numero: ",num)
elif num==num1:
    print("Los Numeros ingresados son iguales")
    
    
    