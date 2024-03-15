from os import system
import re
import time
from tabulate import tabulate
import requests
import modules.getGamas as gG
import modules.getProducto as gP
import modules.validaciones as vali


def postProducto():
    # json-server producto.json -b 5506
    producto = {}
    while True:
        try:
            if (not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                # expresion regular que valide de una cadena Numero y letras en mayusculas pero la cadena es de 6 caracteres  los dos primeros son las letras en mayusculas seguido de un guion y los 3 ultimos caracteres
                if (vali.validacionCodProd(codigo) is not None):
                    data = gP.getProductCodigo(codigo)
                    if (data):
                        print(tabulate(data, headers="keys", tablefmt="grid"))
                        raise Exception(
                            "El codigo del producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception(
                        "El codigo del producto no cumple con el estandar establecido")

            # if(not producto.get("nombre")):
            #     nombre = input("Ingrese el nombre del producto: ")
            #     if(vali.valiNombres(nombre) is not None):
            #         producto["nombre"] = nombre
            #         break
            #     else:
            #         raise Exception("El nombre del producto no cumple con lo establecido")

            # expresion regular que valide de una cadena Numero los primeros catacteres son numeros seguido de un X y los  ultimos caracteres son numeros
            # if (not producto.get("dimensiones")):
            #     dimensiones = input("Ingrese las dimensiones del producto (54x54): ")
            #     if (re.match(r'^\d+[x]\d+$', dimensiones) is not None):
            #         producto["dimensiones"] = dimensiones
            #     else:
            #         raise Exception(
            #             "El nombre no cumple con el estandar establecido")

            # if (not producto.get("proveedor")):
            #     proveedor = input("Ingrese nombre del proveedor: ")
            #     if (vali.valiNombres(proveedor) is not None):
            #         producto["proveedor"] = proveedor
            #     else:
            #         raise Exception(
            #             "El nombre no cumple con el estandar establecido") 

            if (not producto.get("descripcion")):
                descripcion = input("Ingrese nombre del descripcion: ")
                if (re.match(r'^[A-Z][^.]*\.?(\s*[A-Z][^.]*\.?)*$', descripcion) is not None):
                    producto["descripcion"] = descripcion
                    break
                else:
                    raise Exception(
                        "La descripcion no cumple con el estandar establecido") 
        except Exception as error:
            print(error)

    print(producto)
    # producto = {
    #     "codigo_producto": input("Ingrese el codigo del producto: "),
    #     "nombre": input("Ingrese el nombre del producto: "),
    #     "gama": gG.getAllNombre()[int(input(f"Seleccione la gama:\n"+"\t\n".join([f"{i}. {val}" for i, val in enumerate(gG.getAllNombre())])+"\t\n"))],
    #     "dimensiones": input("Ingrese las dimensiones del producto: "),
    #     "proveedor": input("Ingrese el proveedor del producto: "),
    #     "descripcion": input("Ingrese la descripcion del producto: "),
    #     "cantidad_en_stock": int(input("Ingrese la cantidad de stock: ")),
    #     "precio_venta": float(input("Ingrese el precio de venta: ")),
    #     "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    # }
    # peticion = requests.post("http://172.16.100.141:5506",
    #                          timeout=10, data=json.dumps(producto))
    # res = peticion.json()
    # res["Mensaje"] = "Producto Guardado"
    # return [res]


def menu():
    while True:
        system("clear")

        print("""
    ___       __          _       _      __                                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______                                   
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/                                   
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /                                       
/_/  |_\__,_/_/_/_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/             __           __            
  ____/ /___ _/ /_____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                          /_/                                                                                                                                            
    """)
        print("""
    01. Guardar un producto nuevo
    02. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postProducto(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            # case 2:
            #     # print(psProducto.postProducto())
            #     print(tabulate(psProducto.postProducto(), headers="keys", tablefmt="grid"))
            #     input("\nPresiona Enter para volver al menú...")
            #     input("\nPresiona Enter para volver al menú...")
            case 2:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
