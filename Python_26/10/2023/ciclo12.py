"""
Programa que solicita el ingreso de N alturas de personas por teclado. Mostrar la altura promedio de las personas
"""

alt=float(input("De Cuantas personas desea promedian la estatura: "))
alturas=0
x=1
suma=0
while(x<=alt):
    alturas=float(input("Ingrese la altura en metros: "))
    suma=suma+alturas
    x+=1

promedio=suma/alt

print("El promedio de las alturas ingresadas es: ",promedio,"metros")