# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:23:22 2023

@author: Estudiante
"""
"""
Diseñe un programa que lea tres longitudes  y determine de que tipo de triángulo se trata entre: equilátero 
(si tiene tres lados iguales), isósceles (si tiene dos lados iguales) o escaleno (si tiene tres lados desiguales)
"""
lado1=int(input("Ingrese El Lado 1: "))
lado2=int(input("Ingrese El Lado 2: "))
lado3=int(input("Ingrese El Lado 3: "))

if lado1==lado2 and lado2==lado3:
    print("Es Un Triangilo Equilátero",lado1,lado2,lado3)
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")