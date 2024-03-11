from os import system #import of the standard function os.system()
from tabulate import tabulate
import time
import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []

    for val in of.oficina:
        codigoCiudad.append({
            "Codigo": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Otro
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
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
    01. Obtener todos los codigos de oficina y su locacion
    02. Obtener datos de las oficinas de un pais especifico
    03. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                paisOficina = int(input("Ingrese el Pais deseado: "))
                print(tabulate(getAllCiudadTelefono(paisOficina), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos