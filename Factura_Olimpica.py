"""
Crear Una Factura En Python, Donde Se Listen Unos Productos, Cuantos Productos Quiere, Método De Pago, Neto, IVA, Total A Pagar
"""

opcion=1
acumulador=0
galletasm=10000
arepasdo=15000
yogurt=5000
capri=7000

while (opcion<=5):
    menu=int(input("Cuales Productos Desea Comprar: \n 1. Galletas Milo \n  2.Arepas Doña Pilar \n  3. Yogurt \n  4. Galletas Capri \n  5. No Quiero Seguir Comprando"))
    if menu==1:
        print("Usted Compro Unas Galletas Millo Que Cuestan: ",galletasm)
    