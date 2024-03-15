from os import system  # import of the standard function os.system()
import time
from tabulate import tabulate
import requests


def getAllData():
    # json-server producto.json -b 5502
    peticion = requests.get("http://172.16.100.141:5502", timeout=10)
    data = peticion.json()
    return data


def getAllCodigoCiudad():
    codigoCiudad = []

    for val in getAllData():
        codigoCiudad.append({
            "Codigo": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Otro


def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllData():
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "Ciudad": val.get("ciudad"),
                "Telefono": val.get("telefono"),
                "Oficinas": val.get("codigo_oficina"),
                "Pais": val.get("pais"),
            })
    return ciudadTelefono

# Menu


def menu():
    while True:
        system("clear")

        print(""" 

    ____                        __              __        ____  _____      _                 
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \/ __(_)____(_)___  ____ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
          /_/                                                                                
                                                                                                     
    """)
        print("""
    01. Obtener todos los codigos de oficina y su locacion
    02. Obtener datos de las oficinas de un pais especifico
    03. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllCodigoCiudad(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                paisOficina = input("Ingrese el Pais deseado: ")
                print(tabulate(getAllCiudadTelefono(paisOficina),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
