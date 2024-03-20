import requests
import json
from tabulate import tabulate
import modules.producto.getProducto as gP

def updateProductoNombre(codigo):
    while True:
        if codigo != None:
            producto = gP.getProductCodigo2(codigo)
            if(producto):
                print(tabulate(producto, headers="keys", tablefmt="grid"))
                opc = int(input("""
                    Este es el producto que desea actualizar?
                    1. si
                    0. no
                """))
                if opc:
                    headers={'Content-type': 'application/json', 'charset':'UTF-8'}
                    producto[0]["nombre"] = input("Ingrese el nuevo nombre del producto")
                    peticion = requests.put(f"http://154.38.171.54:5008/productos/{producto[0].get('id')}", headers= headers, data=json.dumps(producto[0]))
                    data = peticion.json()
                    return data
                else:
                    codigo = None
            else:
                print(f"El produicto {codigo} no existe")
                codigo = None
        else:
            codigo = input("Ingrese el codigo del producto")