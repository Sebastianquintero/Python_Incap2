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

costof=300000
masd3h1=int(input("Cuantos kilometros Recorrio? : "))
if masd3h1 <=300:
    print("El Monto a Pagar es de: ",costof)
elif masd3h1 >=301 or masd3h1 <=1000:
    kmadi=int(input("Cuantos Kilometros Adicionales Recorrio: " ))
    print("El Monto a Pagar es de : ",(costof),"+",15000*kmadi)
elif masd3h1 >1000:
    kmadi=int(input("Cuantos Kilometros Adicionales Recorrio: " ))
    print("El Monto a Pagar es de : ",(costof),"+",10000*kmadi)
else:
    print("El Valor Ingresado No Corresponde Al Pedido")

