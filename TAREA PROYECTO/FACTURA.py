# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:46:39 2023

@author: jrian
"""


productos = {"MANZANA": 10950,"PERA": 5500,"MANDARINA": 2700,"PAPA": 1500,"AGUACATE": 3500}

# Función para calcular el valor de la compra con IVA
def calcular_valor_compra(producto, cantidad):
    if producto in productos:
        valor_kilo = productos[producto]
        valor_compra = cantidad * valor_kilo
        iva = valor_compra * 0.19  
        total = valor_compra + iva
        return total
    else:
        return "Producto no encontrado en el diccionario"


producto_ingresado = input("Ingrese el nombre del producto: ")
cantidad_ingresada = float(input("Ingrese la cantidad por kilos de producto a llevar: "))


resultado = calcular_valor_compra(producto_ingresado, cantidad_ingresada)
print("*********************************************")
print("PRODUCTO LLEVADO :",producto_ingresado)
print("CANTIDAD LLEVADA :  ",cantidad_ingresada)
print("El valor de la compra es: ",resultado," pesos,IVA incluido")

