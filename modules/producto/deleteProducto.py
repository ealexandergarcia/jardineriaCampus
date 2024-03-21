import requests
import modules.producto.getProducto as gP


def deleteProducto(id):
    data = gP.getProductCodigo(id)

    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")
