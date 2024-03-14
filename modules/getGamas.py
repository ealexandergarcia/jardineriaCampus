# import json
import requests

def getAllGama():
    # json-server gama_producto.json -b 5502
    peticion = requests.get("http://172.16.103.33:5502",timeout=10)
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
