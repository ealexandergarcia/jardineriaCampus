# import json
import requests

def getAllGama():
    # json-server gama_producto.json -b 5507
    peticion = requests.get("http://154.38.171.54:5004/gama",timeout=10)
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
