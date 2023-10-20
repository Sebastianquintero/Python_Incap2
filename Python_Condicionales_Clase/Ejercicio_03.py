# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:16:44 2023

@author: Estudiante
"""

"""
Una compañía dedicada al alquiler de automoviles cobra un monto fijo de $300.000 para los primeros 300 km de recorrido.
Para más de 300 km y hasta 1000 km, cobra un monto adicional de $ 15.000 por cada kilómetro en exceso sobre 300.
Para más de 1000 km cobra un monto adicional de $ 10.000 por cada kilómetro en exceso sobre 1000.
Los precios ya incluyen el 20% del impuesto general a las ventas, IVA.
Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo y el monto incluído del impuesto
"""

fijo=300000
km=int(input("Ingrese los kilometros recorridos"))
if km<=300:
    valorpagar=fijo
    iva=(valorpagar)/1.20
    print("Los kilometros recorridos son: ",km," km ")
    print("El valor del impuesto IVA es: ",iva)
    print("El valor a pagar por el clientes es: ",valorpagar)
elif km>=301 and km<=1000:
    adicional=km-300
    vadicional=adicional*15000
    valorpagar=fijo+vadicional
    iva=(valorpagar)/1.20
    print("Los kilometros recorridos son: ",km," km ")
    print("El valor del impuesto IVA es: ",iva)
    print("El valor a pagar por el clientes es: ",valorpagar)
elif km>=1001:
    adicional01=km-1000
    vadicional01=adicional01*10000 #adicional a los 1000
    adicional02=(km-adicional01)-300 #(2000-1000)-300
    vadicional02=adicional02*15000
    valorpagar=vadicional01+vadicional02+fijo
    iva=(valorpagar)/1.20
    print("Los kilometros recorridos son: ",km," km ")
    print("El valor del impuesto IVA es: ",iva)
    print("El valor a pagar por el clientes es: ",valorpagar)
else:
    print("Los Valores ingresados son incorrectos :3")
