from os import system  # import of the standard function os.system()
from tabulate import tabulate
import time
import requests

def getAllData():
    # json-server empleado.json -b 5503
    peticion = requests.get("http://localhost:5503", timeout=10)
    data = peticion.json()
    return data


# Devuelve los datos de los empleados que tienen un jefe = 7
def getAllNombresApellidoEmailJefe(codigo):
    NombresApellidoEmailJefe = []
    for val in getAllData():
        if (val.get("codigo_jefe")) == codigo:
            NombresApellidoEmailJefe.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe"),
            })
    return NombresApellidoEmailJefe

# Devuelve el nombre del puesto, nombre, apellidos y email de la empresa


def getAllNombrePuestoNombreApellidoEmailJefe():
    NombrePuestoNombreApellidoEmail = []
    for val in getAllData():
        if (val.get("codigo_jefe")) == None:
            NombrePuestoNombreApellidoEmail.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email")
            })
    return NombrePuestoNombreApellidoEmail

# Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados que no sean Representante Ventas

def getAllNombreApellidoNombrePuesto():
    NombrePuestoNombreApellidoEmail = []
    for val in getAllData():
        if (val.get("puesto")) != "Representante Ventas":
            NombrePuestoNombreApellidoEmail.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto": val.get("puesto")
            })
    return NombrePuestoNombreApellidoEmail

# Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados que sean Representante Ventas
def getRepreVentas():
    repreVentas = []
    for val in getAllData():
        if (val.get("puesto")) == "Representante Ventas":
            repreVentas.append({
                "Identificador": val.get("codigo_empleado"),
                "apellidos": f"{val.get('nombre')} {val.get('apellido1')} {val.get('apellido2')}"
            })
    return repreVentas

# Menu


def menu():
    while True:
        system("clear")

        print(""" 
    ____                        __              __        ______                __               __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                        /_/                                                                                                                                        
    """)
        print("""
    01. Obtener todos los empleados que estan al mando de un jefe en especifico
    02. Obtener datos del Jefe jefazo
    03. Obtener todos los empleados que no son representantes de ventas
    04. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                codigoJefe = int(input("Ingrese el código del Jefe: "))
                print(tabulate(getAllNombresApellidoEmailJefe(
                    codigoJefe), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                print(tabulate(getAllNombrePuestoNombreApellidoEmailJefe(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                print(tabulate(getAllNombreApellidoNombrePuesto(),
                      headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2)  # espera en segundos

# keyboard.add_hotkey("ctrl+m", mainMenu)
