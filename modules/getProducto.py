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
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= 100):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key= price, reverse=True)
    for i,val in enumerate(condiciones):
        condiciones[i] = {
            "Codigo" : val.get("codigo_producto"),
            "venta" : val.get("precio_venta"),
            "nombre" : val.get("nombre"),
            "Gama" : val.get("gama"),
            "dimensiones" : val.get("dimensiones"),
            "proveedor" : val.get("proveedor"),
            "descripcion" : f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else val.get("descripcion"),
            "Stock" : val.get("cantidad_en_stock"),
            "base" : val.get("precio_proveedor"),
        }
    return condiciones

# Menu
def menu():
    while True:
        system("clear")
        
        print(""" 

    ____                        __              __        ____                 __           __            
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                                                             
                                                                                                     
    """)
        print ("""
    01. Obtener todos los productos que pertenecen a la gama seleccionada y que tenga mas de 100 unidades en stock (ejm: Ornamentales, 100)
    02. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                gamaProd = input("Ingrese la gama que desea filtar: ")
                stockProd = int(input("Ingrese el stock que desea filtrar: "))
                print(tabulate(getAllStocksPriceGama(gamaProd,stockProd), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos
