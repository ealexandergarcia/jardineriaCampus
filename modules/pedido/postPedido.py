from os import system
import json
import time
import re
import requests
from tabulate import tabulate
import modules.pedido.getPedido as gP
import modules.clientes.getClients as gC
import modules.pedido.deletePedido as dP
import modules.pedido.updatePedido as uP
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



def postPedido():
    # json-server pago.json -b 5504
    pedido = {}
    estados = gP.getAllListadoEstadoPedidos()
    last = gP.getAllData()[-1]
    ultimo_elemento = last["codigo_pedido"]
    system("clear")
    while True:
        try:
            #Codigo de empleado
            if not pedido.get("codigo_pedido"):
                pedido["codigo_pedido"] = ultimo_elemento + 1
            
            # Fecha de Pedido
            if not pedido.get("fecha_pedido"):
                print("Fecha de pedido".center(50,"="))
                fechaPedido = input("Ingrese la fecha de pedido (ej. 2006-01-17): ")
                if vali.valFecha(fechaPedido):
                    pedido["fecha_pedido"] = fechaPedido
                else:
                    raise Exception("La fecha no cumple con lo establecido")

            # Fecha Esperada
            if not pedido.get("fecha_esperada"):
                print("Fecha esperada".center(50,"="))
                fechaEsperada = input("Ingrese la fecha esperada (ej. 2006-01-17): ")
                if vali.valFecha(fechaEsperada):
                    pedido["fecha_esperada"] = fechaEsperada
                else:
                    raise Exception("La fecha no cumple con lo establecido")

            # Fecha Entrega
            if not pedido.get("fecha_entrega"):
                print("Fecha de entrega".center(50,"="))
                fechaEntrega = input("Ingrese la fecha de entrega (ej. 2006-01-17): ")
                if not fechaEntrega or vali.valFecha(fechaEntrega):
                    pedido["fecha_entrega"] = fechaEntrega or None
                else:
                    raise Exception("La fecha no cumple con lo establecido")

            # Estado del pedido
            if not pedido.get("estado"):
                print("Seleccione el estado del pedido".center(50,"="))
                for i, estado in enumerate(estados):
                    print(f"{i}. {estado.get('Estado del pedido')}")
                seleccion = input()
                if re.match(r'^\d+$', seleccion):
                    seleccion = int(seleccion)
                    if 0 <= seleccion <= len(estados):
                        estadoSeleccionado = estados[seleccion].get("Estado del pedido")
                        pedido["estado"] = estadoSeleccionado
                    else:
                        raise Exception(
                            f"Entrada inválida. Por favor, ingrese un número entero válido")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")

            # comentario
            if not pedido.get("comentario"):
                print("Ingrese un comentario del pedido: ".center(50,"="))
                comentario = input()
                if not comentario or vali.valTextoLargo(comentario):
                    pedido["comentario"] = comentario or None
                else:
                    raise Exception(
                        "El comentario no cumple con el estandar establecido")

            # Codigo de cliente
            if not pedido.get("codigo_cliente"):
                print("Ingrese el codigo del cliente".center(50,"="))
                codCliente = input()
                if re.match(r'^\d+$', codCliente):
                    codCliente = int(codCliente)
                    clienteValido = True if any(codCliente == i.get("codigo_cliente") for i in gC.getAllData()) else False
                    if clienteValido:
                        pedido["codigo_cliente"] = codCliente
                        break
                    else:
                        raise Exception("El codigo del cliente no existe")
                else:
                    raise Exception(
                        f"Entrada inválida. Por favor, ingrese un número entero válido")
        except Exception as error:
            print(error)

    peticion = requests.post("http://154.38.171.54:5007/pedidos",
                             timeout=10, data=json.dumps(pedido).encode("UTF-8"))
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
       __      __                    __        ____           ___     __          
  ____/ /___ _/ /_____  _____   ____/ /__     / __ \___  ____/ (_)___/ /___  _____
 / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
/ /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
\__,_/\__,_/\__/\____/____/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/                                                                                       
""")
        print("""
    01. Guardar un nuevo pedido
    02. Eliminar un pedido
    03. Actualizar un Pedido 
    04. Atras
    """)
        opcion = input("\n Ingrese su opcion: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion= int(opcion)

            match opcion:
                case 1:
                    print(tabulate(postPedido(), headers="keys", tablefmt="grid"))
                    input("\nPresiona Enter para volver al menú...")
                case 2:
                    idPedido= input(
                        "Ingrese el id del pedido que desea eliminar: ")
                    dP.deletePedido(idPedido)
                    input("\nPresiona Enter para volver al menú...")
                case 3:
                    uP.menuUpdatePedidos()
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