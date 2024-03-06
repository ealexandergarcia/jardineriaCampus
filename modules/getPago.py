import storage.pago as pag
# Devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago
# en 2008. Tenga en cuenta que debera eliminar aquellos codigos de cliente que aparezcan repeditos

def getAllClientPayYear():
    ClientPayYear = []
    for pay in pag.pago:
        año = pay.get("fecha_pago")
        if año[0:4] == "2008":
            ClientPayYear.append(pay.get("codigo_cliente"))
    cliente_unicos = list(set(ClientPayYear))
    return cliente_unicos
