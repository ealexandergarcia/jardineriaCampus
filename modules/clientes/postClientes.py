from os import system
import re
import time
from tabulate import tabulate
import json
import requests
import modules.clientes.getClients as gC
import modules.empleado.getEmpleados as gE
import modules.validaciones as vali
import modules.clientes.deleteClientes as dC
import modules.clientes.updateCliente as uC

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

def postCliente():
    # json-server cliente.json -b 5501
    repreVentas = gE.getRepreVentas()
    cliente = {}
    last = gC.getAllData()[-1]
    print(last)
    ultimo_elemento = last["codigo_cliente"]

    system("clear")
    while True:
        try:
            # Codigo del cliente
            if not cliente.get("codigo_cliente"):
                cliente["codigo_cliente"] = ultimo_elemento + 1

            # # Nombre del cliente
            if not cliente.get("nombre_cliente"):
                print("Nombre del cliente")
                nombre = input("Ingrese el nombre del cliente (GoldFish Garden): ")
                if vali.valiNombres(nombre) is not None:
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception("El nombre del cliente no cumple con lo establecido")

            # # Nombre del contscto
            if not cliente.get("nombre_contacto"):
                print("Nombre del contacto del clietne (Daniel G)")
                nombreCont = input("Ingrese el nombre del contacto: ")
                if vali.valiNombres(nombreCont) is not None:
                    cliente["nombre_contacto"] = nombreCont
                else:
                    raise Exception("El nombre del contacto no cumple con lo establecido")

            # # Apellido del contacto
            if not cliente.get("apellido_contacto"):
                print("Apellido del contacto del clietne (GoldFish)")
                apellidoCont = input("Ingrese el apellido del contacto: ")
                if vali.valiNombres(apellidoCont) is not None:
                    cliente["apellido_contacto"] = apellidoCont
                else:
                    raise Exception("El apellido del contacto no cumple con lo establecido")

            # # Telefono
            if not cliente.get("telefono"):
                print("Telefono del clietne")
                telefono = input("Ingrese el telefono del cliente (5556901745): ")
                if vali.valiTel(telefono) is not None:
                    cliente["telefono"] = telefono
                else:
                    raise Exception("El telefono del contacto no cumple con lo establecido")

            # # Fax
            if not cliente.get("fax"):
                print("Fax del clietne")
                fax = input("Ingrese el fax del cliente (5556901746): ")
                if vali.valiTel(fax) is not None:
                    cliente["fax"] = fax
                else:
                    raise Exception("El fax del contacto no cumple con lo establecido")

            # Direccion 1
            if not cliente.get("linea_direccion1"):
                print("Direccion Principal")
                linea_direccion1 = input("Ingrese la direccion principal del cliente (ej. CL. 123 #456 - 789): ")
                if vali.valiDire(linea_direccion1) is not None:
                    cliente["linea_direccion1"] = linea_direccion1
                else:
                    raise Exception("La direccion del cliente no cumple con lo establecido")

            # Direccion 2
            if not cliente.get("linea_direccion2"):
                print("Direccion Secundaria")
                linea_direccion2 = input("Ingrese la direccion secundaria del cliente (ej. CL. 123 #456 - 789): ")
                if not linea_direccion2 or vali.valiDire(linea_direccion2):
                    cliente["linea_direccion2"] = linea_direccion2 or None
                else:
                    raise Exception("La dirección del cliente no cumple con lo establecido")

            # Ciudad
            if not cliente.get("ciudad"):
                print("Ciudad del cliente")
                ciudad = input(
                    "Ingrese la ciudad del cliente (ej. Fuenlabrada): ")
                if not ciudad or vali.valUbi(ciudad):
                    cliente["ciudad"] = ciudad or None
                else:
                    raise Exception(
                        "La Ciudad del cliente no cumple con lo establecido")

            # # Region
            if not cliente.get("region"):
                print("Region del cliente")
                region = input(
                    "Ingrese la region del cliente (ej. Madrid): ")
                if not region or vali.valUbi(region):
                    cliente["region"] = region or None
                else:
                    raise Exception(
                        "La Region del cliente no cumple con lo establecido")

            # Pais
            if not cliente.get("pais"):
                print("Pais del cliente")
                pais = input(
                    "Ingrese el pais del cliente (ej. Spain): ")
                if vali.valUbi(pais):
                    cliente["pais"] = pais
                else:
                    raise Exception(
                        "El Pais del cliente no cumple con lo establecido")

            # Codigo Postal
            if not cliente.get("codigo_postal"):
                print("Codigo postal del cliente")
                codPostal = input("Ingrese el codigo postal del cliente (ej. 28943): ")
                if vali.valCodPostal(codPostal):
                    cliente["codigo_postal"] = codPostal
                else:
                    raise Exception(
                        "El codigo postal del cliente no cumple con lo establecido")

            # Representante de ventas
            if not cliente.get("codigo_empleado_rep_ventas"):
                print("Representantes de ventas")
                print (tabulate(repreVentas, headers="keys", tablefmt="grid"))
                # print(repreVentas)
                seleccion = input("Seleccione el identificador de su representante de ventas (ej. 31): ")
                if re.match(r'^\d+$', seleccion) is not None:
                    seleccion = int(seleccion) 
                    repreExist= True if any(seleccion == i.get("Identificador") for i in repreVentas) else False
                    if repreExist:
                        cliente["codigo_empleado_rep_ventas"] = seleccion
                    else:
                         raise Exception( "El Identificador no existe")
                else:
                    raise Exception( "El Identificador no cumple con lo establecido")

            # Limite de credito
            if not cliente.get("limite_credito"):
                limCredito = input("Ingrese su limite de credito (ej. 3000): ")
                if re.match(r'^\d*\.?\d+$', limCredito) is not None:
                    limCredito= float(limCredito)
                    cliente["limite_credito"] = limCredito
                    break
                
                raise Exception( "La dirección del cliente no cumple con lo establecido")

        except Exception as error:
            print(error)

    # peticion = requests.post("http://localhost:5501",
    #                          timeout=10, data=json.dumps(cliente).encode("UTF-8"))
    peticion = requests.post("http://154.38.171.54:5001/cliente",
                             timeout=10, data=json.dumps(cliente).encode("UTF-8"))
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
       __      __                    __        _________            __           
  ____/ /___ _/ /_____  _____   ____/ /__     / ____/ (_)__  ____  / /____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /   / / / _ \/ __ \/ __/ _ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /___/ / /  __/ / / / /_/  __(__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/   \____/_/_/\___/_/ /_/\__/\___/____/  
""")
        print("""
    01. Guardar un cliente nuevo
    02. Eliminar un cliente
    03. Actualizar un cliente
    04. Atras
    """)
        opcion = input("\n Ingrese su opcion: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion= int(opcion)
            match opcion:
                case 1:
                    print(tabulate(postCliente(), headers="keys", tablefmt="grid"))
                    input("\nPresiona Enter para volver al menú...")
                case 2:
                    idCliente = input(
                        "Ingrese el id del cliente que desea eliminar: ")
                    dC.deleteCliente(idCliente)
                    print("Se elimino correctamente")
                    input("\nPresiona Enter para volver al menú...")
                case 3:
                    # idCliente = input(
                    #     "Ingrese el id del cliente que desea actualizar: ")
                    uC.menuUpdateCliente()
                    input("\nPresiona Enter para volver al menú...")
                case 4:
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