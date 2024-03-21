from os import system  # import of the standard function os.system()
import time
import re
from tabulate import tabulate
import requests
import modules.producto.postProductp as psProducto

imgerror = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠒⠒⠲⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠠⢚⣂⡀⠈⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⡴⠆⠀⠀⠀⠀⠀⢎⠐⢟⡇⠀⠈⢣⣠⠞⠉⠉⠑⢄⠀⠀⣰⠋⡯⠗⣚⣉⣓⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢠⢞⠉⡆⠀⠀⠀⠀⠀⠓⠋⠀⠀⠀⠀⢿⠀⠀⠀⠀⠈⢧⠀⢹⣠⠕⠘⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⠮⠔⠁⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠈⣇⠀⢳⠀⠀⠘⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠉⠓⠦⣧⠀⠀⠀⠀⢦⠤⠤⠖⠋⠇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠸⡄⠈⡇⠀⠀⢹⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠈⣆⠀⠀⠀⢱⠀⡇⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠸⡄⠀⠀⠀⠳⠃⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⢠⢏⠉⢳⡀⠀⠀⢹⠀⠀⠀⠀⢠⠀⠀⠀⠑⠤⣄⣀⡀⠀⠀⠀⠀⠀⣀⡤⠚⠀⠀⠀⠀⠀⢸⢢⡀⠀⠀⠀⠀⠀⢰⠁⠀
⠀⠀⣀⣤⡞⠓⠉⠁⠀⢳⠀⠀⢸⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⠙⠦⣤⣀⣀⡤⠃⠀⠀
⠀⣰⠗⠒⣚⠀⢀⡤⠚⠉⢳⠀⠈⡇⠀⠀⠀⢸⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⠵⡾⠋⠉⠉⡏⠀⠀⠀⠈⠣⣀⣳⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⡰⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠲⠤⠤⠤⠴⠚⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""



def getAllData():
    # json-server producto.json -b 5506
    peticion = requests.get("http://154.38.171.54:5008/productos", timeout=10)
    data = peticion.json()
    return data

# Método para obtener un cliente por su ID
def getProductCodigo(id_cliente):
    url = f"http://154.38.171.54:5008/productos/{id_cliente}"
    
    try:
        response = requests.get(url)
        # si la solicitud no fue exitosa (por ejemplo, 404 o 500), raise_for_status() genera una excepción HTTPError. 
        # Esto detendra la ejecucion del programa y mostrara un mensaje de error que indica la causa del fallo.
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        
        cliente = response.json()
        return cliente
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el cliente: {e}")
        return None

def getProductCodigo2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?codigo_producto={codigo.upper()}", timeout=10)
    data = peticion.json()
    if(len(data) == 0):
        data = None
    # else:
    #     return[]
    return data


# Devuelve un listado con todos los productos que pertenecen a la gama "ornamentales" y que
# tienen mas de 100 unidades en stock. El listado debe estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio


def getAllStocksPriceGama(gama, stock):

    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock={stock}&_sort=-precio_venta")
    condiciones = peticion.json()
    for i, val in enumerate(condiciones):
        condiciones[i] = {
            "Codigo": val.get("codigo_producto"),
            "venta": val.get("precio_venta"),
            "nombre": val.get("nombre"),
            "Gama": val.get("gama"),
            "dimensiones": val.get("dimensiones"),
            "proveedor": val.get("proveedor"),
            "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else val.get("descripcion"),
            "Stock": val.get("cantidadEnStock"),
            "base": val.get("precio_proveedor"),
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
        print("""
    01. Obtener todos los productos que pertenecen a la gama seleccionada y que tenga mas de 100 unidades en stock (ejm: Ornamentales, 100)
    02. Atras
    """)
        opcion = input("\n Ingrese su opcion: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion= int(opcion)

            match opcion:
                case 1:
                    gamaProd = input("Ingrese la gama que desea filtar: ")
                    stockProd = int(input("Ingrese el stock que desea filtrar: "))
                    print(tabulate(getAllStocksPriceGama(
                        gamaProd, stockProd), headers="keys", tablefmt="grid"))
                    input("\nPresiona Enter para volver al menú...")
                case 2:
                    break
                case _:
                    print("Opcion invalida")
                    time.sleep(2)  # espera en segundos
        else:
            system("clear")
            print(imgerror)
            print("""
      ____             _   __           _              __  ___     __
     / __ \____  _____(_)_/_/ ____     (_)___ _   ____/_/_/ (_)___/ /___ _
    / / / / __ \/ ___/ / __ \/ __ \   / / __ \ | / / __ `/ / / __  / __ `/
   / /_/ / /_/ / /__/ / /_/ / / / /  / / / / / |/ / /_/ / / / /_/ / /_/ /
   \____/ .___/\___/_/\____/_/ /_/  /_/_/ /_/|___/\__,_/_/_/\__,_/\__,_/
        /_/
""")
            time.sleep(2)  # espera en segundos