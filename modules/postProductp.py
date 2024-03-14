from os import system
import json
import time
from tabulate import tabulate
import requests
import modules.getGamas as gG


def postProducto():
    # json-server producto.json -b 5503
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input(f"Seleccione la gama:\n"+"\t\n".join([f"{i}. {val}" for i, val in enumerate(gG.getAllNombre())])+"\t\n"))],
        "dimensiones": input("Ingrese las dimensiones del producto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese la descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrese la cantidad de stock: ")),
        "precio_venta": float(input("Ingrese el precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
    peticion = requests.post("http://172.16.103.33:5503",
                             timeout=10, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def menu():
    while True:
        system("clear")

        print("""
    ___       __          _       _      __                                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                                   
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                                   
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                                       
/_/  |_\__,_/_/_/_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/             __           __            
  ____/ /___ _/ /_____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                          /_/                                                                                                                                            
    """)
        print("""
    01. Guardar un producto nuevo
    02. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postProducto(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            # case 2:
            #     # print(psProducto.postProducto())
            #     print(tabulate(psProducto.postProducto(), headers="keys", tablefmt="grid"))
            #     input("\nPresiona Enter para volver al menú...")
            #     input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
