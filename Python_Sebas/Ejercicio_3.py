# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:00:01 2023

@author: Estudiante
"""

"""
programa que solicite el peso estatura y la edad de una persona;
determinando su imc =(peso/altura**2)

"""

peso=float(input("Ingrese el peso actual ..."))
estatura=float(input("Ingrese su estatura actual ..."))
imc=round((peso/estatura**2),2)
print("El indice de masa corporal -imc- es: ",imc)
