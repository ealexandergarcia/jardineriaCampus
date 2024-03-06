import storage.pago as pag
# Devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago
# en 2008. Tenga en cuenta que debera eliminar aquellos codigos de cliente que aparezcan repeditos

def getAllClientPayYear():
    ClientPayYear = []
    for pay in pag.pago:
        año = pay.get("fecha_pago")
        if año[0:4] == "2008":
            ClientPayYear.append({
            "codigo_cliente": pay.get("codigo_cliente"),
            "fecha_pago": pay.get("fecha_pago")
        })
    return ClientPayYear
