from os import system
import json
import time
from tabulate import tabulate
import requests
import re
import modules.getOficina as gO
import modules.validaciones as vali


def postOficina():
    # json-server oficina.json -b 5502
    oficina = {}
    
    while True:
        try: 
            if not oficina.get("codigo_oficina"):
                codigo = input("Ingrese el codigo de la oficina (BCN-ES): ")
                if (re.match(r'^[A-Z]{3}-[A-Za-z0-9]{1,3}$', codigo)):
                    data = gO.getOficinaCodigo(codigo)
                    if data:
                        print(tabulate(data, headers="keys", tablefmt="grid"))
                        raise Exception(
                            "El codigo de la oficina ya existe")
                    else:
                        oficina["codigo_oficina"] = codigo
                else:
                    raise Exception(
                    "El codigo del producto no cumple con el estandar establecido")

            # Ciudad
            if not oficina.get("ciudad"):
                print("Ciudad de la oficina: ")
                ciudad = input(
                    "Ingrese la ciudad de la oficina (ej. Barcelona): ")
                if vali.valUbi(ciudad):
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception(
                        "La Ciudad no cumple con lo establecido")

            # # Region
            if not oficina.get("region"):
                print("Region de la oficina: ")
                region = input(
                    "Ingrese la region del cliente (ej. Barcelona): ")
                if vali.valUbi(region):
                    oficina["region"] = region
                else:
                    raise Exception(
                        "La Region no cumple con lo establecido")

            # Pais
            if not oficina.get("pais"):
                print("Pais de la oficina")
                pais = input(
                    "Ingrese el pais la oficina(ej. España): ")
                if vali.valUbi(pais):
                    oficina["pais"] = pais
                else:
                    raise Exception(
                        "El Pais del cliente no cumple con lo establecido")

            # Codigo Postal
            if not oficina.get("codigo_postal"):
                print("Codigo postal de la oficina")
                codPostal = input("Ingrese el codigo postal de la oficina (ej. 28943): ")
                if vali.valCodPostal(codPostal):
                    oficina["codigo_postal"] = codPostal
                else:
                    raise Exception(
                        "El codigo postal del cliente no cumple con lo establecido")
            # Telefono
            if not oficina.get("telefono"):
                print("Telefono de la oficina")
                telefono = input("Ingrese el telefono de la oficina (5556901745): ")
                if vali.valiTel(telefono) is not None:
                    oficina["telefono"] = telefono
                else:
                    raise Exception("El telefono del contacto no cumple con lo establecido")
            # Direccion 1
            if not oficina.get("linea_direccion1"):
                print("Direccion Principal")
                linea_direccion1 = input("Ingrese la direccion principal de la oficina (ej. CL. 123 #456 - 789): ")
                if vali.valiDire(linea_direccion1) is not None:
                    oficina["linea_direccion1"] = linea_direccion1
                else:
                    raise Exception("La direccion no cumple con lo establecido")

            # Direccion 2
            print("Direccion Secundaria")
            linea_direccion2 = input("Ingrese la direccion secundaria de la oficina (ej. CL. 123 #456 - 789): ") or None
            if linea_direccion2 is None:
                oficina["linea_direccion2"] = linea_direccion2
                break
            elif vali.valiDire(linea_direccion2):
                oficina["linea_direccion2"] = linea_direccion2
                break
            else:
                raise Exception("La dirección del cliente no cumple con lo establecido")


        except Exception as error:
            print(error)

    peticion = requests.post("http://localhost:5502",
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
