import requests
import modules.pedido.getPedido as gO

def deletePedido(id):
    data = gO.getPedidoCodigo(id)

    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")