from os import system #import of the standard function os.system()
from tabulate import tabulate
import time
import storage.cliente as cli
import storage.empleado as emp
import storage.pago as pag


def getAllClientPago():
    clientesPagos = []
    clientesSinPagos = []
    for client in cli.clientes:
        idClient = client.get("codigo_cliente")
        for pago in pag.pago:
            if idClient == pago.get("codigo_cliente"):
                clientesPagos.append({
                            "cod_cliente": client.get("codigo_cliente"),
                            "Nombre del cliente": client.get("nombre_cliente")
                        })
            else:
                clientesSinPagos.append({
                            "cod_cliente": client.get("codigo_cliente"),
                            "Nombre del cliente": client.get("nombre_cliente")
                        })
    clientesPagos = list({client['Nombre del cliente']:client for client in clientesPagos}.values())
    clientesSinPagos = list({client['Nombre del cliente']:client for client in clientesSinPagos}.values())
    return clientesSinPagos, clientesPagos