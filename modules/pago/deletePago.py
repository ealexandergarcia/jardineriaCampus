import requests
import modules.pago.getPago as gP


def deletePago(id):
    data = gP.getPagoCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if peticion.ok:
            print("Guardado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")
