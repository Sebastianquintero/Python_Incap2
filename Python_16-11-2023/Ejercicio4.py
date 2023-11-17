# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:36:57 2023

@author: Estudiante
"""

#Operaciones con diccionarios #
prueba={1:'manzana',2:'pera',3:'naranja'}
print("Elementos del diccionario",prueba)
print("El diccionario tiene: ",len(prueba),"elementos")
print("Este elemento esta en la posicion 1",prueba[1])
print("Las claves del diccionario prueba son: ",prueba.keys())
print("Los valores almacenados en el diccionario prueba son: ",prueba.values())
prueba[4]='banano'
print("Diccionario con el nuevo elemento: ",prueba)
print(prueba.items())
prueba[18]='mango'
print("Diccionario con nuevo elemento #2: ",prueba)
print("Busque la clave 2 y devuelva el elemento ",prueba.get(2))
print("Busque la clave 6 y devuelva el elemento ",prueba.get(6))
print("Eliminar el elemento mango: ",prueba.pop(18))
print("Diccionario actualizado sin elemento mango: ",prueba)

frutas=prueba.copy() #realiza una copia de prueba en un nuevo diccionario llamado frutas
print("Nuevo diccionario ...",frutas)
prueba.clear()
print("Diccionario prueba vacio ...",prueba)