from os import system #import of the standard function os.system()
from tabulate import tabulate
import time
import storage.cliente as cli

def getAllClientName():
    clienteName = []
    for val in cli.clientes:
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente":val.get('nombre_cliente')
        })
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if (val.get('codigo_cliente') == codigo):
            return [{
                "Codigo_de_cliente": val.get('codigo_cliente'),
                "nombre_del_cliente":val.get('nombre_cliente')
            }]

def getAllClientCreditCiudad(limitCredit, ciudad):
    clientCredit = []
    for val in cli.clientes:
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad):
            # clientCredit.append(val)
            clientCredit.append({
            "codigo": val.get('codigo_cliente'),
            "Nombre":val.get('nombre_cliente'),
            "ciudad":val.get('ciudad')
        })
    return clientCredit

# Correccion del filtro de pasi/region/ciudad
def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in cli.clientes:
        if val.get('pais') == pais:
            if region is None or val.get('region') == region:
                if ciudad is None or val.get('ciudad') == ciudad:
                    clientZone.append(val)
    return clientZone

# 1 Filtrar por código postal
def getClientCodigoPostal(codigoPostal):
    clientPostalCode = []
    for val in cli.clientes:
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
    for val in cli.clientes:
        if (val.get('codigo_empleado_rep_ventas') == codeRepreVen):
            clientRepreVentas.append({
            "Representante de ventas": val.get("codigo_empleado_rep_ventas"),
            "Credito": val.get("limite_credito"),
            "Nombre": val.get("nombre_cliente"),
            "Nombre": val.get("nombre_cliente")
        })
    return clientRepreVentas
# 3 Filtrar por país y código postal
def getClientByCountryAndPostalCode(country, postal_code):
    clientsByCountryPostal = []
    for client in cli.clientes:
        if client.get('pais') == country and client.get('codigo_postal') == postal_code:
            clientsByCountryPostal.append(client)
    return clientsByCountryPostal

# 4 Filtrar por nombre de contacto y país
def getClientByContactNameAndCountry(contact_name, country):
    clientsByContactNameCountry = []
    for client in cli.clientes:
        if client.get('nombre_contacto') == contact_name and client.get('pais') == country:
            clientsByContactNameCountry.append(client)
    return clientsByContactNameCountry

# Devuelve un listado con el nombre de todos los clientes españoles

def getAllClientesEspañoles(nacionalidad):
    ClientesEspañoles = []
    for client in cli.clientes:
        if (client.get("pais")) == nacionalidad:
            ClientesEspañoles.append({
            "clientes españoles": client.get("nombre_cliente")
        })
    return ClientesEspañoles

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
    01. Obtener todos los clientes (codigo y nombre)
    02. Obtener un cliente por el codigo
    03. Obtener toda la informacion de un cliente de una ciudad en especifico segun su limite de credito especifico (ej: 3000, San Francisco)
    04. Obtener todos los clientes segun su pasi/region/ciudad
    05. Obtener todos los clientes por código postal
    06. Obtener todos lo clientes que segun el representante de ventas que los atendio
    07. Obtener todos los clientes por país y código postal
    08. Obtener todos los clientes Españoles
    09. Volver al menu princupal
    10. Terminar la consulta
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllClientName(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                codigoC = int(input("Ingrese el código del cliente: "))
                print(tabulate(getOneClientCodigo(codigoC), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                ciudad = input("Ingrese la ciudad deseada: ")
                limitCredit = float(input("Ingrese el límite de crédito: "))
                print(tabulate(getAllClientCreditCiudad(limitCredit, ciudad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                pais = input("Ingrese el país: ")
                region = input("Ingrese la región (opcional): ") or None
                ciudad = input("Ingrese la ciudad (opcional): ") or None
                print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 5:
                codigoPostal = input("Ingrese el código postal: ")
                print(tabulate(getClientCodigoPostal(codigoPostal), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 6:
                codeRepreVen = int(input("Ingrese el código del representante de ventas: "))
                print(tabulate(getClientByRepresentanteVentas(codeRepreVen), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 7:
                country = input("Ingrese el país: ")
                postal_code = input("Ingrese el código postal: ")
                print(tabulate(getClientByCountryAndPostalCode(country, postal_code), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 8:
                nacionalidad = "Spain" 
                print(tabulate(getAllClientesEspañoles(nacionalidad), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 9:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos