import sys
import os
from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as producto

if(__name__ == "__main__"): 

    Menu = """                                                                             
    
 __       __  ________  __    __  __    __                                                          
|  \     /  \|        \|  \  |  \|  \  |  \                                                         
| $$\   /  $$| $$$$$$$$| $$\ | $$| $$  | $$                                                         
| $$$\ /  $$$| $$__    | $$$\| $$| $$  | $$                                                         
| $$$$\  $$$$| $$  \   | $$$$\ $$| $$  | $$                                                         
| $$\$$ $$ $$| $$$$$   | $$\$$ $$| $$  | $$                                                         
| $$ \$$$| $$| $$_____ | $$ \$$$$| $$__/ $$                                                         
| $$  \$ | $$| $$     \| $$  \$$$ \$$    $$                                                         
 \$$      \$$ \$$$$$$$$ \$$   \$$  \$$$$$$      

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
            cliente.menu()
        case 2:
            cliente.menu()
        case 3:
            cliente.menu()
        case _:
            print("Opcion invalida")
