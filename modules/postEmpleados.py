from os import system
import json
import time
from tabulate import tabulate
import requests
import modules.getEmpleados as gE

def postCliente():
    # json-server cliente.json -b 5505
    last = gE.getAllData()[-1]
    ultimo_elemento = last["codigo_empleado"]
    empleado = {
        "codigo_cliente": ultimo_elemento + 1,
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese primer apellido: "),
        "apellido2": input("Ingrese el segundo apellido: "),
        "email": input("Ingrese la direccion de correo electronico: "),
        "codigo_oficina": input("Ingrese el codigo de la oficina: " )or None,
        "codigo_jefe": int(input("Ingrese el codigo del jefe: ")),
        "puesto": input("Ingrese el puesto del empleado: "),
    }
    peticion = requests.post("http://172.16.103.33:5505",
                             timeout=10, data=json.dumps(empleado).encode("UTF-8"))
    res = peticion.json()
    return [res]


def menu():
    while True:
        system("clear")

        print("""
    ___       __          _       _      __                         __      __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/__    \__,_/\__,_/\__/\____/____/  
  ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____                       
 / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/                       
/ /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )                        
\__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/                         
                           /_/                                                                                                                                                                                                
    """)
        print("""
    01. Guardar un producto nuevo
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