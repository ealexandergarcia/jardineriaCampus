from os import system  # import of the standard function os.system()
import time
from tabulate import tabulate
import requests
import storage.empleado as emp
import storage.pago as pag


# Data
def getAllData():
    # json-server producto.json -b 5504
    peticion = requests.get("http://172.16.100.141:5504", timeout=10)
    data = peticion.json()
    return data


def getAllClientName():
    clienteName = []
    for val in getAllData():
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
    return clienteName


def getOneClientCodigo(codigo):
    for val in getAllData():
        if (val.get('codigo_cliente') == codigo):
            return [{
                "Codigo_de_cliente": val.get('codigo_cliente'),
                "nombre_del_cliente": val.get('nombre_cliente')
            }]


def getAllClientCreditCiudad(limitCredit, ciudad):
    clientCredit = []
    for val in getAllData():
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad):
            # clientCredit.append(val)
            clientCredit.append({
                "codigo": val.get('codigo_cliente'),
                "Nombre": val.get('nombre_cliente'),
                "ciudad": val.get('ciudad')
            })
    return clientCredit

# Correccion del filtro de pasi/region/ciudad


def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in getAllData():
        if val.get('pais') == pais:
            if region is None or val.get('region') == region:
                if ciudad is None or val.get('ciudad') == ciudad:
                    clientZone.append(val)
    return clientZone

# 1 Filtrar por código postal


def getClientCodigoPostal(codigoPostal):
    clientPostalCode = []
    for val in getAllData():
        if (val.get('codigo_postal') == codigoPostal):
            client_info = {
                "nombre_cliente": val.get('nombre_cliente'),
                "codigo_cliente": val.get('codigo_cliente'),
                "codigo_postal": val.get('codigo_postal')
            }
            clientPostalCode.append(client_info)
    return clientPostalCode

# 2 Filtrar por representante de ventas


def getClientByRepresentanteVentas(codeRepreVen):
    clientRepreVentas = []
    for val in getAllData():
        if (val.get('codigo_empleado_rep_ventas') == codeRepreVen):
            clientRepreVentas.append({
                "Representante de ventas": val.get("codigo_empleado_rep_ventas"),
                "Credito": val.get("limite_credito"),
                "Nombre": val.get("nombre_cliente")
            })
    return clientRepreVentas
# 3 Filtrar por país y código postal


def getClientByCountryAndPostalCode(country, postal_code):
    clientsByCountryPostal = []
    for client in getAllData():
        if client.get('pais') == country and client.get('codigo_postal') == postal_code:
            clientsByCountryPostal.append(client)
    return clientsByCountryPostal

# 4 Filtrar por nombre de contacto y país


def getClientByContactNameAndCountry(contact_name, country):
    clientsByContactNameCountry = []
    for client in getAllData():
        if client.get('nombre_contacto') == contact_name and client.get('pais') == country:
            clientsByContactNameCountry.append(client)
    return clientsByContactNameCountry

# Devuelve un listado con el nombre de todos los clientes españoles


def getAllClientesEspañoles(nacionalidad):
    ClientesEspañoles = []
    for client in getAllData():
        if (client.get("pais")) == nacionalidad:
            ClientesEspañoles.append({
                "clientes españoles": client.get("nombre_cliente"),
                "Pais": client.get("pais")
            })
    return ClientesEspañoles

# Devuelve un listado con todos los clientes que sean de la ciudad de Madrid y cuyo representante de ventas tenga el código de empleado 11 o 30.


def getAllClientMadridRepre():
    clientesMadrid = []
    for client in getAllData():
        if (client.get("ciudad") == 'Madrid'):
            if (client.get("codigo_empleado_rep_ventas") == 11 or client.get("codigo_empleado_rep_ventas") == 30):
                clientesMadrid.append({
                    "Nombre_del_cliente": client.get("nombre_cliente"),
                    "Ciudad": client.get("ciudad"),
                    "Representante_ventas": client.get("codigo_empleado_rep_ventas"),
                })
    return clientesMadrid

# Obtén un listado con el nombre de cada cliente y el nombre y apellido de su representante de ventas.


def getAllClientNameRepreName():
    clientesNames = []
    for client in getAllData():
        idRepre = client.get("codigo_empleado_rep_ventas")
        for empleado in emp.empleados:
            if idRepre == empleado.get("codigo_empleado") and empleado.get("puesto") == "Representante Ventas":
                clientesNames.append({
                    "Nombre del cliente": client.get("nombre_cliente"),
                    "Nombre del representante de ventas": f'{empleado.get("nombre")} {empleado.get("apellido1")}'
                })
    return clientesNames

# Muestra el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes de ventas


def getAllClientPago():
    clientesSinPagos = []
    clientePago = []
    for client in getAllData():
        idClient = client.get("codigo_cliente")
        idRepre = client.get("codigo_empleado_rep_ventas")
        has_pago = False
        for pago in pag.pago:
            if idClient == pago.get("codigo_cliente"):
                has_pago = True
                break
        if not has_pago:
            for empleado in emp.empleados:
                if idRepre == empleado.get("codigo_empleado") and empleado.get("puesto") == "Representante Ventas":
                    clientesSinPagos.append({
                        "cod_cliente": client.get("codigo_cliente"),
                        "Nombre del cliente": client.get("nombre_cliente"),
                        "Nombre del representante de ventas": f'{empleado.get("nombre")} {empleado.get("apellido1")}'
                    })
        else:
            for empleado in emp.empleados:
                if idRepre == empleado.get("codigo_empleado") and empleado.get("puesto") == "Representante Ventas":
                    clientePago.append({
                        "cod_cliente": client.get("codigo_cliente"),
                        "Nombre del cliente": client.get("nombre_cliente"),
                        "Nombre del representante de ventas": f'{empleado.get("nombre")} {empleado.get("apellido1")}'
                    })
    return clientePago, clientesSinPagos


clientes_con_pagos, clientes_sin_pagos = getAllClientPago()

# Menu


def menu():
    while True:
        system("clear")
        print(""" 

    ____                        __              __        _________            __           
   / __ \___  ____  ____  _____/ /____     ____/ /__     / ____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /   / / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / /___/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/   \____/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                               
                                                                                                    
    """)
        print("""
    01. Obtener todos los clientes (codigo y nombre)
    02. Obtener un cliente por el codigo
    03. Obtener toda la informacion de un cliente de una ciudad en especifico segun su limite de credito especifico (ej: 3000, San Francisco)
    04. Obtener todos los clientes segun su pasi/region/ciudad
    05. Obtener todos los clientes por código postal
    06. Obtener todos lo clientes que segun el representante de ventas que los atendio
    07. Obtener todos los clientes por país y código postal
    08. Obtener todos los clientes Españoles
    09. Obtener todos los clientes que sean de la ciudad de Madrid y cuyo representante de ventas tenga el código de empleado 11 o 30
    10. Obtener todos los nombres de cada cliente y el nombre y apellido de su representante de ventas.
    11. Obtener todos los clientes que hayan realizado pagos junto con el nombre de sus representantes de ventas
    12. Obtener todos los clientes que no hayan realizado pagos junto con el nombre de sus representantes de ventas
    13. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllClientName(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                codigoC = int(input("Ingrese el código del cliente: "))
                print(tabulate(getOneClientCodigo(codigoC),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                ciudad = input("Ingrese la ciudad deseada: ")
                limitCredit = float(input("Ingrese el límite de crédito: "))
                print(tabulate(getAllClientCreditCiudad(
                    limitCredit, ciudad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                pais = input("Ingrese el país: ")
                region = input("Ingrese la región (opcional): ") or None
                ciudad = input("Ingrese la ciudad (opcional): ") or None
                print(tabulate(getAllClientPaisRegionCiudad(
                    pais, region, ciudad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 5:
                codigoPostal = input("Ingrese el código postal: ")
                print(tabulate(getClientCodigoPostal(codigoPostal),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 6:
                codeRepreVen = int(
                    input("Ingrese el código del representante de ventas: "))
                print(tabulate(getClientByRepresentanteVentas(
                    codeRepreVen), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 7:
                country = input("Ingrese el país: ")
                postal_code = input("Ingrese el código postal: ")
                print(tabulate(getClientByCountryAndPostalCode(
                    country, postal_code), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 8:
                nacionalidad = "Spain"
                print(tabulate(getAllClientesEspañoles(
                    nacionalidad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 9:
                print(tabulate(getAllClientMadridRepre(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 10:
                print(tabulate(getAllClientNameRepreName(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 11:
                print(tabulate(clientes_con_pagos, headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 12:
                print(tabulate(clientes_sin_pagos, headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 13:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
