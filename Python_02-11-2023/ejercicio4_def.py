# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:38:39 2023

@author: Estudiante
"""

"""
Programa que captura un numero y determina si es par o impar a traves de una funcion
"""

def par():
    num=int(input("Ingrese un numero entero..."))
    if num%2==0:
        print("El numero ingresado: ",num,"ES PAR")
    else:
        print("El numero ingresado",num,"ES IMPAR")


#Programa principal
print("Par o impar \n")
par() #llamado a la funcion
print("-****** Ultima linea programa principal******")