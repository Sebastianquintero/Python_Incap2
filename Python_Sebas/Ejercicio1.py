# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:18:12 2023

@author: Estudiante
"""
#programa que capture nombre, curso y tres notas que calcule la definitiva
print("Datos generales \n")
nombre=input("Ingrese su nombre: ")
curso=input("Ingrese el curso en el que esta inscrito: ")
n1=float(input("Ingrese su primera nota: "))
n2=float(input("Ingrese su segunda nota: "))
n3=float(input("Ingrese su tercera nota: "))
definitiva=(n1+n2+n3)/3
print("****REPORTE GENERAL **** \n")
print("Su nombre completo es:",nombre,"\n")
print("El curso inscrito es : ",curso)
print("Las notas ingresadas fueron: ",n1,"-",n2,"-",n3)
print("La definitiva del estudiante ",nombre,"es : ",definitiva)
