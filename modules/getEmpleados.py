from os import system #import of the standard function os.system()
from tabulate import tabulate
import time
import storage.empleado as emp

# Devuelve los datos de los empleados que tienen un jefe = 7
def getAllNombresApellidoEmailJefe(codigo):
    NombresApellidoEmailJefe = []
    for val in emp.empleados:
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
    for val in emp.empleados:
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
    for val in emp.empleados:
        if (val.get("puesto")) != "Representante Ventas":
            NombrePuestoNombreApellidoEmail.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto": val.get("puesto")
            })
    return NombrePuestoNombreApellidoEmail

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
    01. Obtener todos los empleados que estan al mando de un jefe en especifico
    02. Obtener datos del Jefe jefazo
    03. Obtener todos los empleados que no son representantes de ventas
    04. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                codigoJefe = int(input("Ingrese el código del Jefe: "))
                print(tabulate(getAllNombresApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                print(tabulate(getAllNombrePuestoNombreApellidoEmailJefe(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                print(tabulate(getAllNombreApellidoNombrePuesto(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos