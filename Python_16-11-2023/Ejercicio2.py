# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:58:49 2023

@author: Estudiante
"""

#Operaciones con diccionarios #
serpientes={'cobra':'elapidos','pelota':'piton','trimeresurus':'vibora'}
print("Los componenetes del diccionario serpientes son: ",serpientes)
print("El valor de la clave cobra es: ",serpientes['cobra'])
print("La longitud del diccionario serpiente es: ",len(serpientes))
print("Las claves del diccionario serpiente son: ",serpientes.keys())
print("Los valores del diccionario serpiente son: ",serpientes.values())
print("Los elementos o items del diccionario serpiente son: ",serpientes.items())
print("Agregar un elemento al diccionario serpiente :",serpientes.update({'cascabel':'crotalina'}))
print("Diccionario serpiente con nuevos elementos :",serpientes)
print("Eliminar el elemento cobra del diccionario serpiente: ",serpientes.pop('cobra'))
print("Eliminar el ultimo elemento del diccionario serpiente: ",serpientes.popitem())
print("Estado del diccionario serpiente ....",serpientes)