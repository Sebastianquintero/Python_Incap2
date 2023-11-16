"""
Uso de metodos en lista
"""
listax=[1,2,3,4,5]
listay=[9,8,7]
listaz=['Carlos','Pedro','Luis']
print("Lista original: ",listax)
listax.append(6)
print("Lista con adicionales: ",listax)
listax.extend(listay)
print("Las listas unidas son: ",listax)
listax.append(3)
print("Lista con nueva adicion del 3 es: ",listax)
listax.insert(5,0)
print("Componentes de la lista con insercion en la posicion 5: ",listax)
listax.reverse()
print("Lista Al Reves es: ",listax)
listax.sort()
print("Lista ordenada de menor a mayor: ",listax)
print("Componentes de la lista Z son: ",listaz)
listaz.remove('Pedro')
print("Componentes de la lista Z ",listaz)
print("Cantidad de veces que aparece el 3....",listax.count(3))
print("Lista Z vacia....",listaz.clear())

