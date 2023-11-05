# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:08:01 2023

@author: Estudiante
"""
"""
Programa que captura una cadena, mostrarla en minuscula e indicar cuantas vocales tiene la cadena
"""

frase=input("Ingrese una cadena ...")
frase=frase.lower()
print("La cadena Ingresada es: ",frase)
caracteres=len(frase)
print("La Cantidad de caracteres de la frase ingresada es: ",caracteres)
cantidad=0
x=0
while x<caracteres: 
    if frase [x]=="a" or frase[x]=="e" or frase[x]=="i" or frase[x]=="o" or frase[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("La Cantidad de vocales que contiene la frase es: ",cantidad)