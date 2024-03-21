from os import system
import json
import time
import re
import requests
from tabulate import tabulate
import modules.validaciones as vali
import modules.clientes.getClients as gC
import modules.pago.getPago as gP
import modules.pago.deletePago as dP
import modules.pago.updatePago as uP

def postPago():
    # json-server pago.json -b 5505
    pago = {}
    formasPago = gP.getAllFormasPago()
    system("clear")
    while True:
        try:
            # Codigo de cliente
            if not pago.get("codigo_cliente"):
                print("Ingrese el codigo del cliente".center(50,"="))
                codCliente = input()
                if re.match(r'^\d+$', codCliente):
                    codCliente = int(codCliente)
                    clienteValido = True if any(codCliente == i.get("codigo_cliente") for i in gC.getAllData()) else False
                    if clienteValido:
                        pago["codigo_cliente"] = codCliente
                    else:
                        raise Exception("El codigo del cliente no existe")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")

            # Forma de pago
            if not pago.get("forma_pago"):
                print("Seleccione la forma de pago".center(50,"="))
                for i, formas in enumerate(formasPago):
                    print(f"{i+1}. {formas.get('Formas de pago')}")
                seleccion = input()
                if re.match(r'^\d+$', seleccion):
                    seleccion = int(seleccion)-1
                    if 0 <= seleccion <= len(formasPago):
                        estadoSeleccionado = formasPago[seleccion].get("Formas de pago")
                        pago["forma_pago"] = estadoSeleccionado
                    else:
                        raise Exception(
                            f"Entrada inválida. Por favor, ingrese un número entero válido")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")

            # Identificador de transaccion
            if not pago.get("id_transaccion"):
                print("Ingrese el Identificador de transaccion (ej. ak-std-000001)".center(50,"="))
                idTran = input()
                if (re.match(r'^(?i)[a-z]{2}-[a-z]{3}-\d{6}$', idTran)):
                    pago["id_transaccion"] = idTran
                else:
                    raise Exception(
                        f"El identificador no cumple con el estandar")

            # Fecha de Pedido
            if not pago.get("fecha_pago"):
                print("Fecha de pago".center(50,"="))
                fechaPago = input("Ingrese la fecha de pago (ej. 2006-01-17): ")
                if vali.valFecha(fechaPago):
                    pago["fecha_pago"] = fechaPago
                else:
                    raise Exception("La fecha no cumple con lo establecido")

            # Pago total
            if not pago.get("total"):
                print("Pago total (ej. 3000):".center(50,"="))
                pagoTot = input()
                if re.match(r'^\d*\.?\d+$', pagoTot) is not None:
                    pagoTot= float(pagoTot)
                    pago["total"] = pagoTot
                    break
                raise Exception( "La dirección del cliente no cumple con lo establecido")

        except Exception as error:
            print(error)
    print(pago)
    peticion = requests.post("http://154.38.171.54:5006/pagos",
                             timeout=10, data=json.dumps(pago).encode("UTF-8"))
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
       __      __                    __        ____                        
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \____ _____ _____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
                                                       /____/                                                                                              
""")
        print("""
    01. Guardar un nuevo pago
    02. Eliminar un pago
    03. Actualizar un pago 
    04. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postPago(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                idPago = input(
                    "Ingrese el id del pago que desea eliminar: ")
                dP.deletePago(idPago)
                input("\nPresiona Enter para volver al menú...")
            case 3:
                uP.menuUpdatePago()
                input("\nPresiona Enter para volver al menú...")
            case 4:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
