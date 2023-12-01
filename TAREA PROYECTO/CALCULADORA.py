# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:59:08 2023

@author: jrian
"""
import math


n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    ¿qué quieres hacer?
    
    1) Sumar 
    2) Restar 
    3) Multiplicar 
    4) Dividir 
    5) Residuo
    6) Potencia
    7) Raiz
    8) Salir
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma es igual a",n1+n2)
        print("*************************************")
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta es igual a",n1-n2)  
        print("*************************************")
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto es igual a",n1*n2)
        print("*************************************")
    elif opcion == 4:
        print(" ")
        print("RESULTADO: De la division es",n1/n2)
        print("*************************************")
    elif opcion == 5:
        print(" ")
        print("RESULTADO: Del residuo es",n1%n2) 
        print("*************************************")
    elif opcion == 6:
        print(" ")
        print("RESULTADO: De la potencia es",math.pow(n1,n2))
        print("*************************************")
    elif opcion == 7:
        print(" ")
        print("RESULTADO: De la raiz es",math.sqrt(n1))
        print("*************************************")
    elif opcion ==8:
        
        print("*************************************")
        break
    else:
        print("Opción incorrecta")
        print("*************************************")
        