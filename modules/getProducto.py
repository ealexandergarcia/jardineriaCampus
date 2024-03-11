from os import system #import of the standard function os.system()
from tabulate import tabulate
import time
import storage.producto as pr
# Devuelve un listado con todos los productos que pertenecen a la gama "ornamentales" y que
# tienen mas de 100 unidades en stock. El listado debe estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio

# def getAllProductosOrnamentales():
#     ProductosOrnamentales = []
#     for prodctos in prod.producto:
#         ProductosOrnamentales.append({
#                     "gama": prodctos.get("gama")
#                 })
#     unique_products = list({prodcto['gama']:prodcto for prodcto in ProductosOrnamentales}.values())
#     return unique_products

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= 100):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key= price)

    return condiciones

# Menu
def menu():
    while True:
        system("clear")
        
        print(""" 
    _______                                            __                         
    |       \                                          |  \                        
    | $$$$$$$\  ______    ______    ______    ______  _| $$_     ______    _______ 
    | $$__| $$ /      \  /      \  /      \  /      \|   $$ \   /      \  /       $
    | $$    $$|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$$
    | $$$$$$$\| $$    $$| $$  | $$| $$  | $$| $$   \$$ | $$ __ | $$    $$ \$$    \ 
    | $$  | $$| $$$$$$$$| $$__/ $$| $$__/ $$| $$       | $$|  \| $$$$$$$$ _\$$$$$$$
    | $$  | $$ \$$     \| $$    $$ \$$    $$| $$        \$$  $$ \$$     \|       $$
    \$$   \$$  \$$$$$$$| $$$$$$$   \$$$$$$  \$$         \$$$$   \$$$$$$$ \$$$$$$$ 
                        | $$                                                       
                        | $$                                                       
                        \$$                                                                                                       
    """)
        print ("""
    01. Obtener todos los productos que pertenecen a la gama "ornamentales" y que tienen mas de 100 unidades en stock
    02. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print("PROXIMAMENTE...")
                input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos
