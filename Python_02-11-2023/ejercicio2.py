# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:32:46 2023

@author: Estudiante
"""

"""
Programa que solicita una clave que tenga una longitud entre 10y 20 caracteres, asi es asi,captura nombre,curso y edad de un estudiante, visualizar nombre en
Mayuscula Fija, Curso en Mayuscula Inicial, indicar cuantos caracteres tiene el nombre ingresado y clasificarlo de acuerdo a su edad: Adolecente 12-17 años
Joven 18-25 años, Adulto 26-60 Años, Adulto Mayor >60.En otro caso emite un mensaje de error
"""

clave=input("Ingrese una clave entre 10y 20 caracteres: ")
if len(clave)>=10 and len(clave)<=20:
    nombre=input("Ingrese Su Nombre Completo... \n ")
    curso=input("Ingrese El Curso ACTUAL... \n")
    edad=int(input("Ingrese su edad ACTUAL... \n"))
    if edad>=12 and edad<=17:
        estado="Adolecente"
    elif edad>=18 and edad<=25:
        estado="Joven"
    elif edad>=26 and edad<=60:
        estado="Adulto"
    elif edad>60:
        estado="Adulto Mayor"
    elif edad<12:
        estado="NO ES APTO"
        
    print("---------- REPORTE ESTADO --------")
    print("Su nombre completo es: ",nombre.upper(),"\n")
    print("Curso ACTUAL :",curso.title(),"\n")
    print("La cantidad de caracteres de su nombre es :",len(nombre),"\n")
    print("La clasificacion de acuerdo a su edad ",edad," es: ",estado.upper(),"\n")
    print("******************************** \n")
else:
    print("Error en la longitud de la contraseña")