from os import system #import of the standard function os.system()
from tabulate import tabulate
from datetime import datetime
import time
import storage.pedido as ped

# Devuelve un listado con los distintos estados por los que puede pasar un pedido
def getAllListadoEstadoPedidos():
    estados = []
    for pedido in ped.pedido:
        estados.append(pedido.get('estado'))
    estados_unicos = list(set(estados))
    return estados_unicos

# Devuelve un listado con el codigo de pedido,codigo cliente, fecha esperada y
# fecha de entrega de los pedidos que no han sido entregados a tiempo
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for pedidos in ped.pedido:
        if (pedidos.get("estado") == "Entregado" and pedidos.get("fecha_entrega") is None):
            pedidos["fecha_entrega"]= pedidos.get("fecha_esperada")
        if pedidos.get("estado") == "Entregado":

            date_1 = "/".join(pedidos.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(pedidos.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0 :
                pedidosEntregado.append({
                    "codigo_pedido": pedidos.get("codigo_pedido"),
                    "codigo_cliente": pedidos.get("codigo_cliente"),
                    "fecha_esperada": pedidos.get("fecha_esperada"),
                    "fecha_de_entrega": pedidos.get("fecha_entrega")
                })

    return pedidosEntregado

# Devuelve un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega 
# de los pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fecha esperada
def getAllPedidosEntregadosAntesDeTiempo():
    pedidosEntregados = []
    for pedidos in ped.pedido:
        if (pedidos.get("estado") == "Entregado" and pedidos.get("fecha_entrega") is None):
            pedidos["fecha_entrega"]= pedidos.get("fecha_esperada")
        if pedidos.get("estado") == "Entregado":

            date_1 = "/".join(pedidos.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(pedidos.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2 :
                pedidosEntregados.append({
                    "codigo_pedido": pedidos.get("codigo_pedido"),
                    "codigo_cliente": pedidos.get("codigo_cliente"),
                    "fecha_esperada": pedidos.get("fecha_esperada"),
                    "fecha_de_entrega": pedidos.get("fecha_entrega")
                })

    return pedidosEntregados

# Devuelve un listado de todos los pedidos que fueron rechazados en 2009
def getAllPedidosRechazados():
    pedidosRechazados = []
    for pedidos in ped.pedido:
        if pedidos.get("estado") == "Rechazado":
            if pedidos.get("fecha_pedido")[0:4] == "2009" and pedidos.get("fecha_esperada")[0:4] == "2009":
                pedidosRechazados.append({
                    "codigo_pedido": pedidos.get("codigo_pedido"),
                    "codigo_cliente": pedidos.get("codigo_cliente"),
                    "fecha_esperada": pedidos.get("fecha_esperada"),
                    "estado": pedidos.get("estado"),
                    "fecha_de_entrega": pedidos.get("fecha_entrega"),
                    "comentario": pedidos.get("comentario")
                })
    return pedidosRechazados

# Devuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año
def getAllEntregadosEnero():
    entregadosEnero = []

    for pedido in ped.pedido:
        if (pedido.get("estado") == "Entregado" and pedido.get("fecha_entrega") is None):
            pedido["fecha_entrega"]= pedido.get("fecha_esperada")
        if pedido.get("estado") == "Entregado":
            date_1 = "/".join(pedido.get("fecha_entrega").split("-")[::-1])
            dateLine = datetime.strptime(date_1, "%d/%m/%Y")

            if dateLine.month == 1:
                entregadosEnero.append({
                    "codigo_pedido": pedido.get("codigo_pedido"),
                    "codigo_cliente": pedido.get("codigo_cliente"),
                    "estado": pedido.get("estado"),
                    "fecha_de_entrega": pedido.get("fecha_entrega")
                })
    return entregadosEnero

# Menu
def menu():
    while True:
        system("clear")
        
        print(""" 

    ____                        __              __        ____           ___     __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \___  ____/ (_)___/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/  
          /_/                                                                                
                                                                                                      
    """)
        print ("""
    01. Obtener todos los distintos estados por los que puede pasar un pedido
    02. Obtener datos de todos los pedidos que no han sido entregados a tiempo
    03. Obtener datos de los pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fecha esperada
    04. Obtener todos los pedidos que fueron rechazados en 2009
    05. Obtener todos los pedidos que han sido entregados en el mes de enero de cualquier año
    06. Volver al menu princupal
    """)
        opcion = int(input("\n Ingrese su opcion: "))

        match opcion:
            case 1:
                print(tabulate(getAllListadoEstadoPedidos(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 2:
                print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 3:
                print(tabulate(getAllPedidosEntregadosAntesDeTiempo(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 4:
                print(tabulate(getAllPedidosRechazados(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 5:
                print(tabulate(getAllEntregadosEnero(), headers="keys", tablefmt="grid"))
                input("\nPresiona Enter para volver al menú...")
            case 6:
                break
            case _:
                print("Opcion invalida")
                time.sleep(2) # espera en segundos
