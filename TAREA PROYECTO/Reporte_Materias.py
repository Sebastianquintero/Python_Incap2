# Crear la lista de asignaturas
asignaturas = ["MATEMATICAS", "ESPAÑOL", "CIENCIAS", "SOCIALES"]

# Solicitar las notas al usuario
index = len(asignaturas) - 1
while index >= 0:
    asignatura = asignaturas[index]
    nota = float(input(f"Ingrese la nota para {asignatura}: "))
    
    # Eliminar la asignatura de la lista si la nota es mayor a 3.5
    if nota > 3.5:
        asignaturas.pop(index)
    
    index -= 1

# Imprimir la lista con las asignaturas perdidas
print("Asignaturas perdidas:", asignaturas)
