"""
Realizar un programa que lea 10 numero enteros y luego muestre cuantos valores ingresados
fueron multiplos de 3 y cuatos de 5
"""
multi3=0
multi5=0
prog=1
multi35=0
nm=0

while(prog<=10):
    numero=int(input("Ingrese un numero entero..."))
    if numero%3==0 and numero%5==0:
        print("El numero ingresado : ",numero,"es multiplo de 3 y de 5")
        multi35=multi35+1
    elif numero%3==0:
        print("El numero ingresado : ",numero,"es multiplo de 3")
        multi3=multi3+1
    elif numero%5==0:
        print("El numero ingresado : ",numero,"es multiplo de 5")
        multi5=multi5+1
    else:
        print("El numero ingresado : ",numero,"no es multiplo ni de 3 ni de 5")
        nm=nm+1
    prog=prog+1
print("El total de numeros multiplos de TRES y CINCO es: ",multi35)
print("El total de numeros multiplos de TRES es: ",multi3)
print("El total de numero multiplos de CINCO son: ",multi5)
print("El total de numeros que no son multiplos de TRES ni de CINCO son: ",nm)
print("******* Ultima Linea *****")