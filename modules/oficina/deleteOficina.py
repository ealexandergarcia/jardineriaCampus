import requests
import modules.oficina.getOficina as gO

def deleteOficina(id):
    data = gO.getOficinaCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}",timeout=10)
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al eliminar: {peticion.status_code}")
