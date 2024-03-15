from os import system
import json
import time
from tabulate import tabulate
import requests


def postOficina():
    # json-server oficina.json -b 5502
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese el nombre de la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la region: ") or None,
        "codigo_postal": input("Ingrese el codigo postal: "),
        "telefono": input("Ingrese el numero telefonico: "),
        "linea_direccion1": input("Ingrese la direccion principal: "),
        "linea_direccion2": input("Ingrese la direccion secundaria: ") or None
    }
    peticion = requests.post("http://172.16.103.33:5502",
                             timeout=10, data=json.dumps(oficina).encode("UTF-8"))
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
       __      __                    __        ____  _____      _                 
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                  
""")
        print("""
    01. Guardar una oficina nueva
    02. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                postOficina()
                print("SE GUARDO CORRECTAMENTE")
                # print(tabulate(postOficina(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
