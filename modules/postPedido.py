from os import system
import json
import time
from tabulate import tabulate
import requests


def postPedido():
    # json-server pago.json -b 5504
    pedido = {
        "codigo_cliente": int(input("Ingrese el codigo del usuario: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese el identificar de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha de pago: "),
        "total": int(input("Ingrese total de la compra: "))
    }
    peticion = requests.post("http://172.25.202.224:5504",
                             timeout=10, data=json.dumps(pedido).encode("UTF-8"))
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
       __      __                    __        ____           ___     __          
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \___  ____/ (_)___/ /___  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/                                                                                       
""")
        print("""
    01. Guardar un nuevo pedido
    02. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postPedido(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
