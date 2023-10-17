# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:48:34 2023

@author: Estudiante
"""

"""
Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.
Además por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el monto de la compra, 
el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto. 

"""

print("Venta de Rosas --------------------------------------------")
compra=int(input("cuantas Docenas Desea Comprar: "))
vd=12000
vp=(compra*vd)
valorinicial=3
if compra>3:
    descuento=(compra*vd)*0.15
    print("--------------------------------------------")
    print("El valor de su compra es de: ",compra*vd,"Su descuento es de: ",descuento,"\n valor a pagar: ",vp-descuento)
    print("Por compras mayores a tres docenas te regalo una unidad",compra-valorinicial)
elif compra<=3:
    descuento=(compra*vd)*0.10
    print("")
    print("El valor de su compra es de: ",compra*vd,"Su descuento es de: ",descuento,"\n valor a pagar: ",vp-descuento)
else:
    print("Valor ingresado no valido")