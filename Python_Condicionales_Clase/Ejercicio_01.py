# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:29:34 2023

@author: Estudiante
"""

"""
Carga del sueldo, pero si el sueldo que ingresamos supera $3.000.000   se mostrará por pantalla el mensaje 
"Esta persona debe abonar impuestos" e indicar el valor a pagar por el impuesto, en caso que la persona cobre 3.000.000 o menos aparece advertencia por pantalla 
"No debe pagar impuesto". La tarifa del impuesto es del 35% sobre el sueldo.
"""
nombre=input("Ingrese Su nombre")
sueldo=float(input("Ingrese Su sueldo"))

if sueldo>3000000:
    print("****************************************")
    print("Sr.",nombre,"debe abonar impuestos y este valor es:",sueldo*0.35)
else:
    print("-------***********************")
    print("Sr",nombre,"Felicidades No DEBE PAGAR IMPUESTO")
