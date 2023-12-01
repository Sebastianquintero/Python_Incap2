# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:54:42 2023

@author: Estudiante
"""

"""
diccionario que capture 5 productos con sus precios, muestre los precios mayores a 50.000
"""

def cargar():
    producto={} #definiendo un diccionario
    for x in range(5):
        nombre=input("Ingrese nombre del producto ....")
        precio=int(input("ingrese el costo del producto: $ "))
        producto[nombre]=precio
    return producto
    

def imprimir(a):
    print("**********************************************************")
    print("  ***   LISTA DE PRODUCTOS  ********")
    print("**********************************************************")
    for referencia in a:
        print("Nombre del producto: ",referencia)
        print("Valor Unitario: $ ",a[referencia])
        print("--------------------------------------------------------")
        
def mayor(a):
    print("**********************************************************")
    print("  ***   PRODUCTOS MAYORES A 50.000 ********")
    print("**********************************************************")
    for p in a:
        if a[p]>50000:
            print(p)
            
            
            



#principal

datos=cargar()
imprimir(datos)
mayor(datos)