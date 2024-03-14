from os import system
import json
import time
from tabulate import tabulate
import requests
import modules.getClients as gC


def postCliente():
    # json-server cliente.json -b 5501
    last = gC.getAllData()[-1]
    ultimo_elemento = last["codigo_cliente"]
    cliente = {
        "codigo_cliente": ultimo_elemento + 1,
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contacto: "),
        "telefono": input("Ingrese el numero telefonico del cliente: "),
        "fax": input("Ingrese el numero de fax del cliente: "),
        "linea_direccion1": input("Ingrese la direccion del cliente: "),
        "linea_direccion2": input("Ingrese la direccion secundaria del cliente (opcional): " )or None,
        "ciudad": input("Ingrese la ciudad del cliente: " )or None,
        "region": input("Ingrese la region del cliente: " )or None,
        "pais": input("Ingrese el pais del cliente: "),
        "codigo_postal": input("Ingrese el codigo postal del cliente: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representanre de ventas: ")),
        "limite_credito": int(input("Ingrese su limite de credito: ")),
    }
    peticion = requests.post("http://172.25.202.224:5501",
                             timeout=10, data=json.dumps(cliente).encode("UTF-8"))
    res = peticion.json()
    return [res]


def menu():
    while True:
        system("clear")

        print("""
    ___       __          _       _      __                                      
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                     
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                         
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/                          
       __      __                    __        _________            __           
  ____/ /___ _/ /_____  _____   ____/ /__     / ____/ (_)__  ____  / /____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /   / / / _ \/ __ \/ __/ _ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /___/ / /  __/ / / / /_/  __(__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/   \____/_/_/\___/_/ /_/\__/\___/____/  
""")
        print("""
    01. Guardar un cliente nuevo
    02. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postCliente(), headers="keys", tablefmt="grid"))
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
