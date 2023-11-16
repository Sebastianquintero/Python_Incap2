"""
Programa que solicita nombre, curso y 3 notas, calcula la definitiva y clasifica de acuerdo a su resultado
definitiva <3.0 Reprobado, Definitiva >=3.0 Aprovado 
"""
definitiva=0
datos=[] #lista
nombre=input("Ingrese su nombre:  ")
datos.append(nombre)
curso=input("Ingrese su curso actual: ")
datos.append(curso)
nota1=float(input("Ingrese La Primera Nota ..."))
datos.append(nota1)
nota2=float(input("Ingrese La Segunda Nota ..."))
datos.append(nota2)
nota3=float(input("Ingrese La Tercera Nota ..."))
datos.append(nota3)
print("Los datos del estudiante ingresados son: ",datos,"\n")
for x in range(2,5):
    definitiva=definitiva+datos[x] #almacenando en la variable promedio las notas ingresadas
definitiva=round((definitiva/3),1)
datos.append(definitiva)
print("La definitiva de las notas es: ",round(definitiva,1),"\n") #redondeo la definitiva con 1 decimal
if definitiva<3.0:
    estado="REPROVADO"
    datos.append(estado)
else:
    estado="APROVADO"
    datos.append(estado)
print("Los datos ingresados son: ",datos,"\n")
print("********************** \n")
print("REPORTE ESTUDIANTE \n")
print("Nombre: ",datos[0],"\n")
print("Curso: ",datos[1],"\n")
print("NOTA 1: ",datos[2],"\n")
print("NOTA 2: ",datos[3],"\n")
print("NOTA 3: ",datos[4],"\n")
print("definitiva: ",datos[5],"\n")
print("Estado actual: " ,datos[6],"\n")
print("*********************************")
print(datos)
