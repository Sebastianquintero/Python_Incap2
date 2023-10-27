"""
Realizar un programa que calcule permita al ususario seleccionar entre calcular la raiz cuadrada, potencia(cubo)
division y residuo de un numero ingresado
"""
import math
num=int(input("Ingrese un numero a operar"))
opcion=1
while(opcion<=4):
    menu=int(input("Seleccione la operacion a realizar : /n 1.Raiz cuadrada /n 2.Cubo /n 3.Division /n 4.Residuo"))
    if menu==1:
        respuesta=math.sqrt(num)
        print("La raiz cuadrada del numero ingresado ..",num,"da como resultado",round(respuesta,2))
    elif menu==2:
        respuesta=math.pow(num,3)
        print("El cubo del numero ingresado: ",num,"da como resultado : ",respuesta)
    elif menu==3:
        divisor=int(input("Ingrese el divisor : "))
        respuesta=num/divisor
        print("El resultado de dividir el numero ingresado :",num,"entre el divisor :",divisor,"da como resultado :",respuesta)
    elif menu==4:
        divisor=int(input("Ingrese el divisor : "))
        respuesta=num%divisor
        print("El residuo de dividir, el numero ingresado : ",num,"entre el divisor :",divisor,"da como resultado :",round(respuesta,2))
    else:
        print("Numero ingresado no es valido... ingrese solo numeros del 1 al 4")
    opcion=opcion+1