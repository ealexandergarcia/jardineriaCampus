import storage.pago as pag
from datetime import datetime
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

    # Eliminar valores repetidos usando un conjunto y luego convertirlo a lista
    unique_clients = list({client['codigo_cliente']:client for client in ClientPayYear}.values())

    return unique_clients


# Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante PayPal.
# Ordene el resultado de mayor a menor
def getAllPagosPaypal():
    pagosPaypal=[]
    for pay in pag.pago:
        if pay.get("forma_pago") == "PayPal":
            date_1 = "/".join(pay.get("fecha_pago").split("-")[::-1])
            paymentDate = datetime.strptime(date_1, "%d/%m/%Y")

            if paymentDate.year == 2008:
                pagosPaypal.append({
                    "codigo_cliente": pay.get("codigo_cliente"),
                    "fecha_pago": pay.get("fecha_pago"),
                    "forma_pago": pay.get("forma_pago"),
                    "id_transaccion": pay.get("id_transaccion"),
                    "total": pay.get("total"),
                })
    valores_ord = sorted(pagosPaypal, key=lambda x: x["total"], reverse=True)
    return valores_ord

