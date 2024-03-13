import json
import requests

def postProducto(producto):
    # json-server producto.json -b 5501
    peticion = requests.post("http://172.16.100.141:5501",timeout=10, data=json.dumps(producto))
    res = peticion.json()
    return res
