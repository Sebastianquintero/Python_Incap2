# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 22:37:39 2023

@author: jrian
"""

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print("Su simbolo es:",monedas[moneda.title()])
else:
    print("La divisa no está.")
    print("Intente de nuevo")