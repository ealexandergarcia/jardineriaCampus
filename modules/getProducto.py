from os import system #import of the standard function os.system()
import time
from tabulate import tabulate
import requests
import modules.postProductp as psProducto
import modules.getGamas as gG

def getAllData():
    # json-server producto.json -b 5503
    peticion = requests.get("http://172.16.100.141:5503",timeout=10)
    data = peticion.json()
    return data

# Devuelve un listado con todos los productos que pertenecen a la gama "ornamentales" y que
# tienen mas de 100 unidades en stock. El listado debe estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio
def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
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
    03. Guardar info
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                gamaProd = input("Ingrese la gama que desea filtar: ")
                stockProd = int(input("Ingrese el stock que desea filtrar: "))
                print(tabulate(getAllStocksPriceGama(gamaProd,stockProd), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                producto = {
                    "codigo_producto": input("Ingrese el codigo del producto: "),
                    "nombre": input("Ingrese el nombre del producto: "),
                    "gama": input(f"Seleccione la gama:\n"+"\t\n".join([f"{i}. {val}" for i, val in enumerate(gG.getAllNombre())])+"\t\n" ),
                    "dimensiones": input("Ingrese las dimensiones del producto: "),
                    "proveedor": input("Ingrese el proveedor del producto: "),
                    "descripcion": input("Ingrese la descripcion del producto: "),
                    "cantidad_en_stock": int(input("Ingrese la cantidad de stock: ")),
                    "precio_venta": float(input("Ingrese el precio de venta: ")),
                    "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
                    }
                # print(producto)
                psProducto.postProducto(producto)
                print("producto Guardado")
                input("\nPresiona Enter para volver al menú...")
            case 3:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos
