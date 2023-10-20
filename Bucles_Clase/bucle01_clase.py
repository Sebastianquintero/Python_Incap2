# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:16:52 2023

@author: Estudiante
"""

"""
Programa que visualiza los numeros pares iniciando en 2 y terminando en 10
"""

print("Uso de FOR")
for i in range(2,12,2):
    print(i)
    
print("///////////////////////////////////////////////////////")

print("Uso de WHILE")
i=2
while i<=10:
    print(i)
    i=i+2
    
    
"""
Programa que visualiza los numeros desde el 20 hasta el 25 de uno en uno
"""

print("Uso de FOR")
for i in range(20,26,1):
    print(i)
    
print("///////////////////////////////////////////////////////")

print("Uso de WHILE")
i=20
while i<=25:
    print(i)
    i=i+1
    
    
"""
Programa que capture 3 numeros, los sume y muestre el resultado por pantalla
"""


    
print("///////////////////////////////////////////////////////")

print("Uso de WHILE")
i=20
while i<=25:
    print(i)
    i=i+1
    
respuesta=0 #Acumulador
for i in range(3):
    numero=int(input("Ingrese un numero entero: "))
    respuesta=respuesta+numero
print("El resultado de sumar los numeros es: ",respuesta)

print("///////////////////    WHILE  ////////////////////////////////////")


respuesta=0
i=1
while(i<=3):
    numero=int(input("Ingrese un numero entero"))
    respuesta=respuesta+numero
    i=i+1 #Ultima sentencia del while
print("El resultadp de sumar los numeros es: ",respuesta)

    
"""
Programa que nombre, curso, 3 notas y clasifique al estudiante: reprobado<2.5, recuperar entre 2.5 y 3.0 Y APROVADO >3.0
"""
definitiva=0
nombre=input("Ingrese Nombre Completo: " )
curso=input("Ingrese curso actual: " )
for i in range(3):
    nota=float(input("Ingrese Notas ...."))
    definitiva=definitiva+nota
definitiva=definitiva/3
print("REPORTE DE NOTAS -------")
print("su nombre completo es: ",nombre)
print("su curso actual es: ",curso)
print("Su definitiva es: ",definitiva)
if definitiva <2.5:
    print("Estado: REPROBADO")
elif definitiva >=2.5 and definitiva <3.0:
    print("Estado: RECUPERAR")
elif definitiva >3.0:
    print("Estado: APROBADO")

    
    
    
"""
programa que capture 5 numeros y determine cuantos son pares (residuo=0) y cuantos impares (residuo=1)
"""
par=0
impar=0
for i in range(5):
    num=int(input("ingrese un numero entero"))
    if num%2==0:
        par=par+1
    else:
        impar=impar+1
print("La cantidaa de pares es: ",par)
print("La cantidad de impares es: ",impar)



print("--------- USO WHILE ---------------")

par=0
impar=0
i=1
while(i<=5):
    num=int(input("Ingrese los numeros ......."))
    if num%2==0:
        par=par+1
    else:
        impar=impar+1
        
print("La cantidad de numeros pares es: ",par)
print("La cantidad de numeros impares es: ",impar)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    