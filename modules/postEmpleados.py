from os import system
import json
import time
import re
import requests
from tabulate import tabulate
import modules.getEmpleados as gE
import modules.validaciones as vali

def postEmpleado():
    # json-server empleado.json -b 5503
    last = gE.getAllData()[-1]
    ultimo_elemento = last["codigo_empleado"]
    empleado = {}
    puestos = gE.getAllPuesto()
    system("clear")
    while True:
        try:
            #Codigo de empleado
            if not empleado.get("codigo_empleado"):
                empleado["codigo_cliente"] = ultimo_elemento + 1

            # # Nombre del cliente
            if not empleado.get("nombre"):
                print("Nombre del Empleado")
                nombre = input("Ingrese el nombre del Empleado (Marcos): ")
                if vali.valiNombres(nombre):
                    empleado["nombre"] = nombre
                else:
                    raise Exception("El nombre del empleado no cumple con lo establecido")

            # # Primer Apellido del Empleado
            if not empleado.get("apellido1"):
                print("Apellido del Empleado ")
                apellidoPEmpleado = input("Ingrese el primer apellido del empleado (Lopez): ")
                if vali.valiNombres(apellidoPEmpleado):
                    empleado["apellido1"] = apellidoPEmpleado
                else:
                    raise Exception("El apellido del contacto no cumple con lo establecido")
            
            # # Segundo Apellido del Empleado
            if not empleado.get("apellido2"):
                print("Segundo apellido del Empleado")
                apellidoSEmpleado = input("Ingrese el Segundo apellido del empleado (Lopez): ")
                if vali.valiNombres(apellidoSEmpleado):
                    empleado["apellido2"] = apellidoSEmpleado
                else:
                    raise Exception("El apellido del empleado no cumple con lo establecido")
            
            # extension
            if not empleado.get("extension"):
                print("Extension")
                extensionEmpleado = input("Ingrese la extension del empleado (3897): ")
                if re.match(r"\b\d{4}\b", extensionEmpleado):
                    empleado["extension"] = extensionEmpleado
                else:
                    raise Exception("La extension no cumple con lo establecido")    

            # Email
            if not empleado.get("email"):
                print("Email")
                emailEmpleado = input("Ingrese el email del empleado (marcos@jardineria.es):")
                if vali.valEmail(emailEmpleado):
                    empleado["email"] = emailEmpleado
                else:
                    raise Exception("El email no cumple con lo establecido")    

            # Oficina
            if not empleado.get("codigo_oficina"):
                codigo = input("Ingrese el codigo de la oficina (BCN-ES): ")
                if (re.match(r'^[A-Z]{3}-[A-Za-z0-9]{1,3}$', codigo)):
                    data = True if any(codigo == i.get("codigo_oficina") for i in gE.getAllData()) else False
                    if data:
                        empleado["codigo_oficina"] = codigo
                    else:
                        raise Exception("El codigo de la oficina no existe")
                else:
                    raise Exception(
                    "El codigo de la oficina no cumple con el estandar establecido")

            # Codigo Jefe
            if not empleado.get("codigo_jefe"):
                codigoJefe = int(input("Ingrese el codigo de Jefe"))
                jefe_valido = True if any(codigoJefe == i.get("codigo_empleado") for i in gE.getAllData()) else False
                if jefe_valido:
                    empleado["codigo_jefe"] = codigoJefe
                else:
                    raise Exception("El codigo de jefe no existe")
                
            # Puesto
            if not empleado.get("puesto"):
                print("\nSeleccione el puesto")
                for i, puesto in enumerate(puestos):
                    print(f"{i}. {puesto}")
                seleccion = input()
                if re.match(r'^\d+$', seleccion):
                    seleccion = int(seleccion)
                    if 0 <= seleccion <= len(puestos):
                        puestoSeleccionado = puestos[seleccion]
                        empleado["puesto"] = puestoSeleccionado
                        break
                    else:
                        raise Exception(
                            f"Entrada inválida. Por favor, ingrese un número entero válido")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")


        except Exception as error:
            print(error)
    # print(empleado)
    peticion = requests.post("http://154.38.171.54:5003/empleados",
                             timeout=10, data=json.dumps(empleado).encode("UTF-8"))
    res = peticion.json()
    return [res]

def deleteEmpleado(id):
    data =  gE.getEmpleadoCodigo(id)

    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")

def menu():
    while True:
        system("clear")

        print("""
    ___       __          _       _      __                         __      __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/__    \__,_/\__,_/\__/\____/____/  
  ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____                       
 / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/                       
/ /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )                        
\__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/                         
                           /_/                                                                                                                                                                                                
    """)
        print("""
    01. Guardar un empleado nuevo
    02. Eliminar un Empleado
    03. Atras
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(postEmpleado(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                idEmpleado = input(
                    "Ingrese el id del empleado que desea eliminar: ")
                print(tabulate(deleteEmpleado(idEmpleado), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos
