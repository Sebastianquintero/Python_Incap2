# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:53:29 2023

@author: Estudiante
"""

"""
 
"""
#Operaciones con diccionarios
diccionario1={'piloto1':'Juan Pablo Montoya','piloto2':'Fernando Alonso','piloto3':'Michael shumaher'}
print("Los valores del diccionario son: ",diccionario1) #imprime los elementos del diccionario
#get() Devuelve el valor de una clave indicada
print("El Valor de la primera clave es: ",diccionario1.get('piloto1'))
#update -- actualiza si lo encuentra o agrega sino existe
diccionario1.update({'piloto4':'Lewis Hamilton'})
diccionario1.update({'piloto2':'Sebastian Vettel'})
print("El diccionario con los adicionales y modificaciones es: ",diccionario1)#imprime el diccionario con las actualizaciones
#pop() Devuelve el valor que corresponde y luego lo elimina
print("El elemento a borrar es: ",diccionario1.pop('piloto3'))
print("El diccionario sin el elemento borrado es: ",diccionario1)
#Buscar un valor dentro del diccionario --> devuelve verdadero si lo encuentra - falso si no lo encuentra
print("El valor de juan Pablo Montoya en el diccionario ?",'Juan pablo Montoya' in diccionario1.values())#True
print("El valor de Felipe Massa en el diccionario ?",'Felipe Massa' in diccionario1.values())#False
#Buscar una clave dentro del diccionario --> devuelve verdadero si lo encuentra - falso si no lo encuentra
print("La clave piloto1 esta en el diccionario?",'piloto1' in diccionario1)
print("La clave piloto 1 esta en el diccionario?",'piloto1' in diccionario1)
