from os import system
import re
import time
import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
import modules.producto.getProducto as gP
import modules.producto.updateProducto as uP
import modules.producto.deleteProducto as dP
import modules.validaciones as vali

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



def postProducto():
    # json-server producto.json -b 5506
    producto = {}
    # Gamas
    gammas = gG.getAllNombre()
    while True:
        try:
            # Codigo del prodcuto
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del producto (AB-132): ")
                # expresion regular que valide de una cadena Numero y letras en
                # mayusculas pero la cadena es de 6 caracteres  los dos primeros son
                # las letras en mayusculas seguido de un guion y los 3 ultimos caracteres
                if vali.validacionCodProd(codigo) is not None:
                    data = gP.getAllData()
                    codeProdExist= True if any(codigo == i.get("codigo_producto") for i in data) else False
                    if codeProdExist:
                        raise Exception(
                            "El codigo del producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception(
                        "El codigo del producto no cumple con el estandar establecido")

            # Nombre del producto
            if not producto.get("nombre"):
                nombre = input(
                    "Ingrese el nombre del producto (Martillo Grande): ")
                if vali.valiNombres(nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception(
                        "El nombre del producto no cumple con lo establecido")

            # Gamas
            if not producto.get("gama"):
                print("\nSeleccione la gama:")
                for i, gamma in enumerate(gammas):
                    print(f"{i}. {gamma}")
                seleccion = input()
                if re.match(r'^\d+$', seleccion) is not None:
                    seleccion = int(seleccion)
                    if 0 <= seleccion < len(gammas):
                        print("funciona2")
                        gamma_seleccionada = gammas[seleccion]
                        producto["gama"] = gamma_seleccionada
                    else:
                        raise Exception(
                            f"Entrada inválida. Por favor, ingrese un número entero válido")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")

            # # expresion regular que valide de una cadena Numero los primeros catacteres son
            # numeros seguido de un X y los  ultimos caracteres son numeros
            # Dimensiones
            if not producto.get("dimensiones"):
                dimensiones = input(
                    "Ingrese las dimensiones del producto (54x54): ")
                if re.match(r'^\d+[x]\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception(
                        "El nombre no cumple con el estandar establecido")

            # Proveedor
            if not producto.get("proveedor"):
                proveedor = input("Ingrese nombre del proveedor: ")
                if vali.valiNombres(proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception(
                        "El nombre no cumple con el estandar establecido")

            # Descripcion
            if not producto.get("descripcion"):
                descripcion = input("Ingrese nombre del descripcion: ")
                if vali.valTextoLargo(descripcion):
                    producto["descripcion"] = descripcion
                else:
                    raise Exception(
                        "La descripcion no cumple con el estandar establecido")

            # Cantidad de stock
            if not producto.get("cantidadEnStock"):
                cantidadStock = input("Ingrese la cantidad de stock: ")
                if re.match(r'^[0-9]+$', cantidadStock) is not None:
                    cantidadStock = int(cantidadStock)
                    producto["cantidadEnStock"] = cantidadStock
                else:
                    raise Exception(
                        "El Stock no cumple con el estandar establecido")

            # Precio de venta
            if not producto.get("precio_venta"):
                precioVenta = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', precioVenta) is not None:
                    precioVenta = int(precioVenta)
                    producto["precio_venta"] = precioVenta
                else:
                    raise Exception(
                        "El Stock no cumple con el estandar establecido")

            # Precio de proveedor
            if not producto.get("precio_proveedor"):
                precioProveedor = input("Ingrese el precio de proveedor: ")
                if re.match(r'^[0-9]+$', precioProveedor) is not None:
                    precioProveedor = int(precioProveedor)
                    producto["precio_proveedor"] = precioProveedor
                    break
                else:
                    raise Exception(
                        "El precio de proveedor no cumple con el estandar establecido")

        except Exception as error:
            print(error)

    print(producto)
    peticion = requests.post("http://154.38.171.54:5008/productos",
                             timeout=10, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

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
    02. Eliminar un producto
    03. Actualizar un producto
    04. Atras
    """)
        opcion = input("\n Ingrese su opcion: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion= int(opcion)
            match opcion:
                case 1:
                    print(tabulate(postProducto(), headers="keys", tablefmt="grid"))
                    input("\nPresiona Enter para volver al menú...")
                case 2:
                    idProducto = input(
                        "Ingrese el id del producto que desea eliminar: ")
                    dP.deleteProducto(idProducto)
                    input("\nPresiona Enter para volver al menú...")
                case 3:
                    uP.menuUpdateProductos()
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