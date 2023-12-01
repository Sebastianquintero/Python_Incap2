# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:27:08 2023

@author: Estudiante
"""

"""
Programa que captura el nombre y documento de identidad de 3 usuarios, donde el documento es la clave, el sistema solicita al usuario que ingrese el documento para buscarlo en la 
base, si no esta emite el mensaje
"""

def cargar():
    usuario={}
    for x in range(3):
        nombre=input("Ingrese su nombre")
        documento=int(input("Ingrese el documento de identidad sin puntos ni comas ..."))
        usuario[documento]=nombre
    return usuario

def imprimir(usuario):
    print("Los datos ingresados son: ....")
    for documento in usuario:
        print(documento,usuario[documento])
        
def buscar(usuario):
    documen_buscar=int(input("Ingrese el documentoa buscar sin puntos ni comas ..."))
    if documen_buscar in usuario:
        print("El documento buscado: ",documen_buscar," Corresponde a: ",usuario[documen_buscar])
    else:
        print("El documento buscado: ",documen_buscar," No se encuentra en la base de datos")
        

datos=cargar()
imprimir(datos)
buscar(datos)