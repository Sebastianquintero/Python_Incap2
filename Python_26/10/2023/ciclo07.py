"""
Ejercicio 2
realizar un programa que calcule el area de 5 circulos, si area= 2*pi*radio*radio
"""
import math

circulo=1
while(circulo<=5):
    radio=float(input("Ingrese el valor del radio"))
    area=2*math.pi*math.pow(radio,2)
    print("El area del circulo cuyo radio es: ",radio,"da como resultado: ",round(area,2))
    circulo+=1 #circulo=circulo+1 -- modificador debe ir de ultimas dentro del while
print("******** Ultima Linea ********")

#Ciclo con for
