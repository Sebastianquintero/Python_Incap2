# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:06 2023

@author: Estudiante
"""

# Diccionario que carga valores -> Nombre_Pais, Capital, Numero de habitantes

def cargar():
    paises={} #diccionario vacio
    for x in range(3):
        nombre=input("Ingrese El nombre pais... ")
        capital=input("Ingrese la capital del pais.. ")
        habitantes=int(input("Ingrese la cantidad de habitantes...  "))
        paises[nombre]=(capital,habitantes)
    return paises

def imprimir(paises):
    print("La informacion ingresada es: ",paises)
    for nombre in paises:
        print("El pais ingresado es: ",nombre)
        print("La capital del pais es: ",paises[nombre][0])
        print("La cantidad de habitantes es: ",paises[nombre][1])
        print("********************************")
    
    
    
    
    
    
    
    
    
    
    
#Programa Principal
paises=cargar()#funcion llamada cargar que devuelva valores que serian almacenados en paises
imprimir(paises) #Funcion imprimir que recibe la variable paises