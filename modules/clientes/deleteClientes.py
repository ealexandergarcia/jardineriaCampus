import requests
import modules.clientes.getClients as gC

def deleteCliente(id):
    data = gC.getClienteCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}", timeout=10)
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")
