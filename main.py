from os import system
import re
import time
import requests
import modules.getClients as listCliente
import modules.postClientes as CRUDCliente
import modules.getOficina as listOficina
import modules.postOficina as CRUDOficina
import modules.getEmpleados as listEmpleado
import modules.postEmpleados as CRUDEmpleado
import modules.getPedido as listPedido
import modules.postPedido as CRUDPedido
import modules.getPago as listPago
import modules.postPago as CRUDPago
import modules.getProducto as listProducto
import modules.postProductp as CRUDProducto
import json

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

def menuCliente():
    while True:
        system("clear")
        print("""
    __  ___                        __        _________            __
   /  |/  /__  ____  __  __   ____/ /__     / ____/ (_)__  ____  / /____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /   / / / _ \/ __ \/ __/ _ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /___/ / /  __/ / / / /_/  __(__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/_/\___/_/ /_/\__/\___/____/


        1. Reportes de los clientes
        2. Guardar, Actualizar y Eliminar Clientes
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listCliente.menu()
            case 2:
                CRUDCliente.menu()
            case 3:
                break
            case _:
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

def menuOficinas():
    while True:
        system("clear")
        print("""
    __  ___                        __        ____  _____      _
   /  |/  /__  ____  __  __   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/

        1. Reportes de las oficinas
        2. Guardar, Actualizar y Eliminar Oficinas
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listOficina.menu()
            case 2:
                CRUDOficina.menu()
            case 3:
                break
            case _:
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

def menuEmpleado():
    while True:
        system("clear")
        print("""
    __  ___                        __        ______                __               __
   /  |/  /__  ____  __  __   ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/
                                                        /_/
        1. Reportes de los empleados
        2. Guardar, Actualizar y Eliminar Empleados
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listEmpleado.menu()
            case 2:
                CRUDEmpleado.menu()
            case 3:
                break
            case _:
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

def menuPedidos():
    while True:
        system("clear")
        print("""
    __  ___                        __        ____           ___     __
   /  |/  /__  ____  __  __   ____/ /__     / __ \___  ____/ (_)___/ /___  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/
        1. Reportes de los pedidos
        2. Guardar, Actualizar y Eliminar Pedidos
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listPedido.menu()
            case 2:
                CRUDPedido.menu()
            case 3:
                break
            case _:
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

def menuPagos():
    while True:
        system("clear")
        print("""
    __  ___                        __        ____
   /  |/  /__  ____  __  __   ____/ /__     / __ \____ _____ _____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_/    \__,_/\__, /\____/____/
                                                     /____/
        1. Reportes de las oficinas
        2. Guardar, Actualizar y Eliminar Oficinas
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listPago.menu()
            case 2:
                CRUDPago.menu()
            case 3:
                break
            case _:
                print("""

   ____             _   __           _              __  ___     __
  / __ \____  _____(_)_/_/ ____     (_)___ _   ____/_/_/ (_)___/ /___ _
 / / / / __ \/ ___/ / __ \/ __ \   / / __ \ | / / __ `/ / / __  / __ `/
/ /_/ / /_/ / /__/ / /_/ / / / /  / / / / / |/ / /_/ / / / /_/ / /_/ /
\____/ .___/\___/_/\____/_/ /_/  /_/_/ /_/|___/\__,_/_/_/\__,_/\__,_/
    /_/
""")
                print(imgerror)
                time.sleep(2)  # espera en segundos

def menuProducto():
    while True:
        system("clear")
        print("""
    __  ___                        __        ____                 __           __
   /  |/  /__  ____  __  __   ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/

        1. Reportes de los productos
        2. Guardar, Actualizar y Eliminar Productos
        3. Volver al menu princupal
        """)
        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                listProducto.menu()
            case 2:
                CRUDProducto.menu()
            case 3:
                break
            case _:
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

def mainMenu():
    while True:
        system("clear")
        try:

            Menu = """
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ /
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/
                                                    /_/
        1. Cliente
        2. Oficina
        3. Empleado
        4. Pedido
        5. Pago
        6. Producto
        7. Salir
        """
            pepe = """
⠄⠄⠄⠄⠄⠄⠄⣠⣴⣶⣿⣿⡿⠶⠄⠄⠄⠄⠐⠒⠒⠲⠶⢄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣠⣾⡿⠟⠋⠁⠄⢀⣀⡀⠤⣦⢰⣤⣶⢶⣤⣤⣈⣆⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢰⠟⠁⠄⢀⣤⣶⣿⡿⠿⣿⣿⣊⡘⠲⣶⣷⣶⠶⠶⠶⠦⠤⡀⠄⠄
⠄⠔⠊⠁⠁⠄⠄⢾⡿⣟⡯⣖⠯⠽⠿⠛⠛⠭⠽⠊⣲⣬⠽⠟⠛⠛⠭⢵⣂⠄
⡎⠄⠄⠄⠄⠄⠄⠄⢙⡷⠋⣴⡆⠄⠐⠂⢸⣿⣿⡶⢱⣶⡇⠄⠐⠂⢹⣷⣶⠆
⡇⠄⠄⠄⠄⣀⣀⡀⠄⣿⡓⠮⣅⣀⣀⣐⣈⣭⠤⢖⣮⣭⣥⣀⣤⣤⣭⡵⠂⠄
⣤⡀⢠⣾⣿⣿⣿⣿⣷⢻⣿⣿⣶⣶⡶⢖⣢⣴⣿⣿⣟⣛⠿⠿⠟⣛⠉⠄⠄⠄
⣿⡗⣼⣿⣿⣿⣿⡿⢋⡘⠿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠄⠄
⣿⠱⢿⣿⣿⠿⢛⠰⣞⡛⠷⣬⣙⡛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣓⡀⠄
⢡⣾⣷⢠⣶⣿⣿⣷⣌⡛⠷⣦⣍⣛⠻⠿⢿⣶⣶⣶⣦⣤⣴⣶⡶⠾⠿⠟⠁⠄
⣿⡟⣡⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣙⡛⠓⠒⠶⠶⠶⠶⠶⠶⠶⠶⠿⠟⠄⠄⠄
⠿⡐⢬⣛⡻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠟⠃⠄⠄⠄⠄⠄⠄
⣾⣿⣷⣶⣭⣝⣒⣒⠶⠬⠭⠭⠭⠭⠭⠭⠭⣐⣒⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄⠄⠄⠄⠄
            """
            print(pepe, Menu)
            opcion = input("Ingrese su opcion: ")
            if(re.match(r'[0-9]+$', opcion) is not None):
                opcion= int(opcion)
                match opcion:
                    case 1:
                        menuCliente()
                    case 2:
                        menuOficinas()
                    case 3:
                        menuEmpleado()
                    case 4:
                        menuPedidos()
                    case 5:
                        menuPagos()
                    case 6:
                        menuProducto()
                    case 7:
                        break
                    case _:
                        system("clear")
                        print(imgerror)
                        print("""
      ____             _   __           _              __  ___     __
     / __ \____  _____(_)_/_/ ____     (_)___ _   ____/_/_/ (_)___/ /___ _
    / / / / __ \/ ___/ / __ \/ __ \   / / __ \ | / / __ `/ / / __  / __ `/
   / /_/ / /_/ / /__/ / /_/ / / / /  / / / / / |/ / /_/ / / / /_/ / /_/ /
   \____/ .___/\___/_/\____/_/ /_/  /_/_/ /_/|___/\__,_/_/_/\__,_/\__,_/
        /_/
    # """)
                        time.sleep(2)

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

        except KeyboardInterrupt:
            print("\nSaliendo del menú...")
            break


if(__name__ == "__main__"):

    # peticion = requests.get("http://154.38.171.54:5008/productos?gama=Ornamentales&cantidadEnStock=100&_sort=-precio_venta")
    # data = json.dumps(peticion.json(), indent=4)
    # print(data)
    mainMenu()
    # print(listCliente.getAllClientPago())

    # CRUDPago.menu()

# # Actualziar los json para agregar el id
#     with open("storage/pago.json", "r") as f:
#         fichero = f.read()
#         data = json.loads(fichero)
#         for i, val in enumerate(data):
#             data[i]["id"] = (i+1)
#         data = json.dumps(data, indent=4).encode("utf-8")
#         with open("storage/pago.json", "wb+") as f1:
#             f1.write(data)
#             f1.close()
    