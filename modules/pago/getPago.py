from os import system  # import of the standard function os.system()
from datetime import datetime
import time
from tabulate import tabulate
import requests

# Data
def getAllData():
    # json-server producto.json -b 5505
    peticion = requests.get("http://154.38.171.54:5006/pagos", timeout=10)
    data = peticion.json()
    return data

# Obtener el pedido por Id
def getPedidoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}", timeout=10)
    return [peticion.json()] if peticion.ok else []

# Devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago
# en 2008. Tenga en cuenta que debera eliminar aquellos codigos de cliente que aparezcan repeditos
def getAllClientPayYear():
    ClientPayYear = []
    for pay in getAllData():
        año = pay.get("fecha_pago")
        if año[0:4] == "2008":
            ClientPayYear.append({
                "Codigo": pay.get("codigo_cliente"),
                "Fecha de Pago": pay.get("fecha_pago")
            })

    # Eliminar valores repetidos usando un conjunto y luego convertirlo a lista
    unique_clients = list(
        {client['Codigo']: client for client in ClientPayYear}.values())

    return unique_clients

# Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante PayPal.
# Ordene el resultado de mayor a menor
def getAllPagosPaypal():
    pagosPaypal = []
    for pay in getAllData():
        if pay.get("forma_pago") == "PayPal":
            date_1 = "/".join(pay.get("fecha_pago").split("-")[::-1])
            paymentDate = datetime.strptime(date_1, "%d/%m/%Y")

            if paymentDate.year == 2008:
                pagosPaypal.append({
                    "codigo": pay.get("codigo_cliente"),
                    "Fecha de pago": pay.get("fecha_pago"),
                    "Forma de pago": pay.get("forma_pago"),
                    "Identidicador de transaccion": pay.get("id_transaccion"),
                    "total": pay.get("total"),
                })
    valores_ord = sorted(pagosPaypal, key=lambda x: x["total"], reverse=True)
    return valores_ord

# Devuelve un listado con todas las formas de pago que aparecen en la tabla pago.
# Tenga en cuenta que no deben aparecer formas de pago repetidas
def getAllFormasPago():
    formasPago = []
    for pay in getAllData():
        formasPago.append({
            "Formas de pago": pay.get("forma_pago")
        })

    # Eliminar valores repetidos usando un conjunto y luego convertirlo a lista
    unique_pay = list(
        {client['Formas de pago']: client for client in formasPago}.values())

    return unique_pay

# Menu
def menu():
    while True:
        system("clear")

        print(""" 

    ____                        __              __        ____                        
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \____ _____ _____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
          /_/                                                     /____/              
                                                                                                    
    """)
        print("""
    01. Obtener todos los clientes que realizaron pagos en 2008
    02. Obtener todos los pagos que se realizaron en el año 2008 mediante PayPal
    03. Obtener todas las formas de pago
    04. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllClientPayYear(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                print(tabulate(getAllPagosPaypal(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                print(tabulate(getAllFormasPago(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
