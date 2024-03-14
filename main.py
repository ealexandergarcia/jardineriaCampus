# import sys
# import os
import modules.getClients as listCliente
import modules.postClientes as CRUDCliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as listProducto
import modules.postProductp as CRUDProducto

# print(tabulate(producto.getAllStocksPriceGama("Ornamentales",100),headers="keys",tablefmt="grid"))

# # Suponiendo que la función getAllClientPago() devuelve dos valores
# clientes_con_pagos, clientes_sin_pagos = pr.getAllClientPago()

# # Si solo quieres imprimir los clientes con pagos
# print("Clientes con pagos:")
# print(tabulate(clientes_sin_pagos,headers="keys",tablefmt="grid"))

# # Si solo quieres imprimir los clientes sin pagos
# print("Clientes sin pagos:")
# print(tabulate(clientes_con_pagos,headers="keys",tablefmt="grid"))


def menuCliente():
    while True:
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
                print("Opcion invalida")


def menuProducto():
    while True:
        print("""                                                                             
    __  ___                        __               
   /  |/  /__  ____  __  __   ____/ /__             
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \            
 / /  / /  __/ / / / /_/ /  / /_/ /  __/            
/_/ _/_/\___/_/ /_/\__,_/__ \__,_/\___/_            
   / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                             
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
                print("Opcion invalida")


def mainMenu():
    while True:
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
            
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠞⠛⠋⠉⠙⠛⢶⣤⡀⠀⢀⣠⣤⡶⠶⠶⠶⢦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣞⠋⠁⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⢀⣀⣤⡶⠶⠾⠛⠛⠷⠶⣤⣹⣇⠀⢀⣀⣀⣀⣀⣀⣀⣀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠡⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⣀⣀⣙⣻⣟⠉⠉⠁⠀⠀⢀⣈⣉⣉⣛⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠖⠛⠋⠉⢉⠙⠛⢷⡤⠶⠖⠚⠛⠉⠉⢉⣉⠉⠙⠻⢦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢹⣿⠀⠀⠀⠀⢠⣶⡶⠶⠞⠋⠉⣀⣠⣤⣴⣶⡿⠛⠛⠛⣷⣤⣤⡶⠶⠚⣻⣿⣿⡟⠛⠲⢾⣷⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠈⠉⠀⠀⠀⠀⠘⠛⠻⢿⣟⠛⠋⠉⠁⣴⣿⣿⠿⣷⡄⠀⣸⡇⠀⠀⠀⣼⣯⣿⡿⢿⣷⠀⣠⣿⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣌⡛⠷⢦⣼⣿⣯⣿⣷⡿⢿⣿⡿⠟⠷⠶⠶⠿⠿⠾⠿⠿⢛⣻⠿⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠶⠤⣷⣾⣿⣿⠿⠛⠁⠀⢤⡀⠀⠀⠀⠀⢀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠟⠛⠉⠀⠀⠀⠀⠀⠈⠛⠷⣶⡞⠛⠋⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⢷⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣦⠀⠀⠀⣀⣸⣷⣀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⢸⣧⣬⣿⣤⣨⣿⡛⠛⠶⠶⠶⠶⠦⡤⠤⢴⣿⣀⣿⠦⠶⠛⠋⠁⣨⡇⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⣿⣴⢿⡇⠀⢿⡏⠉⢹⡟⠛⠛⠛⠛⠷⠶⠶⢶⣾⣯⠀⣿⠦⠶⠶⠶⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠟⡇⠀⢸⡇⠀⢸⣿⠾⣶⠶⣶⣦⣤⣤⡟⠁⡟⠀⣿⣤⣤⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠈⠙⠷⢶⣤⣀⠀⠀⠀⠀⢸⡇⠀⣷⣀⣸⡇⠀⢸⡷⠶⢻⡆⠀⠀⠀⢸⡇⠀⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣀⣴⠾⠉⠉⠙⠛⠶⠶⢾⡇⠀⡏⠉⢹⡇⠶⢾⡇⠀⠀⣷⣀⣀⣠⣿⠀⠀⡇⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⣠⡾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡇⠀⢸⡇⠀⠈⣷⠀⠀⣏⠉⠁⠀⣿⠀⠀⣧⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⡇⠀⠸⠷⠀⠀⣿⠀⠀⣿⠀⠀⠀⣿⠀⠀⣿⡀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⢻⡇⠀⠀⣿⠀⠀⠘⣿⠈⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣠⡀⠀⠀⣠⡀⠀⠀⠀⠀⢹⣇⠀⢸⡇⠀⠀⠈⣿⡄⢹⡙⠻⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠛⠃⠀⠈⠛⠃⠀⠀⠀⠀⠀⣿⢀⣾⠀⠀⠀⠀⠈⠁⢸⡇⠀⠀⠈⠙⠳⠶⣦⣄⣀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣼⠇⠀⠀⠀⠀⠀⢠⣾⡁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣷⡄
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
            """
            print(f"{pepe} {Menu}")
            opcion = int(input("Ingrese su opcion: "))

            match opcion:
                case 1:
                    menuCliente()
                case 2:
                    oficina.menu()
                case 3:
                    empleado.menu()
                case 4:
                    pedido.menu()
                case 5:
                    pago.menu()
                case 6:
                    menuProducto()
                case 7:
                    break
                case _:
                    print("Opcion invalida")
        except KeyboardInterrupt:
            print("\nSaliendo del menú...")
            break


if (__name__ == "__main__"):
    mainMenu()
