# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:23:22 2023

@author: Estudiante
"""
"""
Diseñe un programa que lea tres longitudes  y determine de que tipo de triángulo se trata entre: equilátero (si tiene tres lados iguales), isósceles (si tiene dos lados iguales) o escaleno (si tiene tres lados desiguales)
"""
ladoA=int(input("INGRESE EL LADO A DE TRIANGULO : "))
ladoB=int(input("INGRESE EL LADO B DE TRIANGULO : "))
ladoC=int(input("INGRESE EL LADO C DE TRIANGULO : "))
if ladoA==ladoB and ladoB==ladoC:
    print("ESTO ES UN TRIANGULO EQUILATERO \nTODOS LOS LADOS SON IGUALES")
elif ladoA==ladoB or ladoB==ladoC or ladoC==ladoA:
    print("ESTO ES UN TRIANGULO ISOCELES \nTIENE 2 LADOS IGUALES")
else:
    print("ESTO ES UN TRIANGULO ESCALENO \nTODOS LOS LADOS SON DIFERENTES")