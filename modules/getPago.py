from os import system #import of the standard function os.system()
from tabulate import tabulate
from datetime import datetime
import time
import storage.pago as pag

# Devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago
# en 2008. Tenga en cuenta que debera eliminar aquellos codigos de cliente que aparezcan repeditos
def getAllClientPayYear():
    ClientPayYear = []
    for pay in pag.pago:
        año = pay.get("fecha_pago")
        if año[0:4] == "2008":
            ClientPayYear.append({
                "codigo_cliente": pay.get("codigo_cliente"),
                "fecha_pago": pay.get("fecha_pago")
            })

    # Eliminar valores repetidos usando un conjunto y luego convertirlo a lista
    unique_clients = list({client['codigo_cliente']:client for client in ClientPayYear}.values())

    return unique_clients


# Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante PayPal.
# Ordene el resultado de mayor a menor
def getAllPagosPaypal():
    pagosPaypal=[]
    for pay in pag.pago:
        if pay.get("forma_pago") == "PayPal":
            date_1 = "/".join(pay.get("fecha_pago").split("-")[::-1])
            paymentDate = datetime.strptime(date_1, "%d/%m/%Y")

            if paymentDate.year == 2008:
                pagosPaypal.append({
                    "codigo_cliente": pay.get("codigo_cliente"),
                    "fecha_pago": pay.get("fecha_pago"),
                    "forma_pago": pay.get("forma_pago"),
                    "id_transaccion": pay.get("id_transaccion"),
                    "total": pay.get("total"),
                })
    valores_ord = sorted(pagosPaypal, key=lambda x: x["total"], reverse=True)
    return valores_ord

# Devuelve un listado con todas las formas de pago que aparecen en la tabla pago.
# Tenga en cuenta que no deben aparecer formas de pago repetidas
def getAllFormasPago():
    formasPago = []
    for pay in pag.pago:
        formasPago.append({
            "forma_pago": pay.get("forma_pago")
        })

    # Eliminar valores repetidos usando un conjunto y luego convertirlo a lista
    unique_pay = list({client['forma_pago']:client for client in formasPago}.values())

    return unique_pay

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
    01. Obtener todos los clientes que realizaron pagos en 2008
    02. Obtener todos los pagos que se realizaron en el año 2008 mediante PayPal
    03. Obtener todas las formas de pago
    04. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllClientPayYear(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                print(tabulate(getAllPagosPaypal(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                print(tabulate(getAllFormasPago(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos
