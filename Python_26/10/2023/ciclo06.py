"""

Realizar un programa capture una determinada cantidad de numeros y los muestre por pantalla, finaliza hasta
que el usuario digite 0
"""

numero=int(input("Ingrese un numero: "))
while(numero!=0):
    print("el numero ingresado es: ",numero)
    numero=int(input("Ingrese el numero 0 para terminar: "))
    if numero==0:
        break #finaliza la ejecucion del programa
print("Fin del programa") 