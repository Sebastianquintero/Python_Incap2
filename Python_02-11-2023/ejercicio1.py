# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:37:59 2023

@author: Estudiante
"""
"""
frase: programacion
"""
mensaje=input("Ingrese una frase...")
print("cadena 1: ",mensaje,"\n")
mensaje2="en Lenguaje Python"
respuesta=mensaje+" "+mensaje2
print("La nueva cadena es: ",respuesta,"\n")
respuesta1=respuesta*4
print("La nueva cadena multiplicacion por 4 es: ",respuesta1)
respuesta+="Jornada Nocturna"
print("Cadena Adicional es: ",respuesta,"\n")
print("La Longitud o cantidad de caracteres de la cadena :",len(respuesta),"\n")
print("La cadena escrita  en Mayuscula fija es: ",respuesta.upper(),"\n")
print("La cadena escrita en Minuscula fija es: ",respuesta.lower(),"\n")
print("La cadena escrita en Mayuscula inicial es: ",respuesta.title(),"\n")
print("El primer caracter de la cadena es: ",respuesta[0],"\n")
print("La palabra Python en la cadena esta en la Posicion: ",respuesta.find("Python"))
respuesta2=respuesta.replace("Python", "C#")
print("La cadena reemplazada es :",respuesta2,"\n")
print("El lenguaje de programacion usadp es :",respuesta[25:31])
print("La cadena hasta la posicion 35 es: ",respuesta[:35])