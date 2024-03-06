import storage.pedido as ped

# Devuelve un listado con los distintos estados por los que puede pasar un pedido

def getAllListadoEstadoPedidos():
    estados = []
    for pedido in ped.pedido:
        estados.append(pedido.get('estado'))
    estados_unicos = list(set(estados))
    return estados_unicos


