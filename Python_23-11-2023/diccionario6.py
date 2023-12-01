# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:35:22 2023

@author: Estudiante
"""
"""
cargar referencia, nombre, cantidad, precio. Se va a realizar consultas del producto por referencia y generar alertas en caso que la cantidad sea igual a 0
"""


def cargar():
    producto={} #definiendo un diccionario
    x=int(input("Ingrese la cantidad de productos a capturar")) #indica la cantidad de productos
    z=1
    while z<=x:
        referencia=input("Ingrese la referencia del producto: ")
        nombre=input("Ingrese el nombre del producto: ")
        cantidad=int(input("Ingrese las unidades del producto: "))
        precio=int(input("Ingrese el valor unitario del producto: "))
        producto[referencia]=(nombre,cantidad,precio)
        z=z+1
    return producto


def imprimir(a):
    print("**********************************************************")
    print("  ***   LISTA DE PRODUCTOS  ********")
    print("**********************************************************")
    for referencia in a:
        print("Referencia  del producto: ",referencia)
        print("Nombre del producto: ",a[referencia][0]) #recorre el diccionario e imprime la posicion 0 que 
        print("stock actual: ",a[referencia][1])
        print("Valor Unitario: ",a[referencia][2])
        print("--------------------------------------------------------")
        
        
def consulta(a):
    print("**********************************************************")
    print("/****** CONSULTA DE PRODUCTOS *****")
    print("--------******************************************************")
    referencia=input("Ingrese la referencia del producto a consultar ......?")
    if referencia in a:
        print("Referencia: ",referencia)
        print("Nombre del producto: ",a[referencia][0])
        print("Stock Actual :",a[referencia][1])
        print("Valor Unitario: ",a[referencia][2])
    else:
        print("La referencia ingresada no se encuentra almacenada")
        
def alerta(a):
    print("-*****************************************************************")
    print("******************** Productos  sin stock ****************************")
    print("***********************************************************************")
    for referencia in a:
        if a[referencia][1]==0:
            print("Alerta -- Productos sin stock")
            print("Referencia: ",referencia)
            print("Nombre del producto: ",a[referencia][0])
            print("***************************************************************")
            

    

#principal
datos=cargar() #funcion que devuelva parametros que se almacenan en la variable datos
imprimir(datos) #funcion que recibe parametro
consulta(datos)
alerta(datos)