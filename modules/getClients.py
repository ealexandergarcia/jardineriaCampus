import storage.cliente as cli

def getAllClientName():
    clienteName = []
    for val in cli.clientes:
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente":val.get('nombre_cliente')
        })
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if (val.get('codigo_cliente') == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente":val.get('nombre_cliente')
            }

def getAllClientCreditCiudad(limitCredit, ciudad):
    clientCredit = []
    for val in cli.clientes:
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad):
            # clientCredit.append(val)
            clientCredit.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente":val.get('nombre_cliente'),
            "ciudad":val.get('ciudad')
        })
    return clientCredit

# Correccion del filtro de pasi/region/ciudad
def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in cli.clientes:
        if val.get('pais') == pais:
            if region is None or val.get('region') == region:
                if ciudad is None or val.get('ciudad') == ciudad:
                    clientZone.append(val)
    return clientZone

# Filtrar por código postal
def getClientCodigoPostal(codigoPostal):
    clientPostalCode = []
    for val in cli.clientes:
        if (val.get('codigo_postal') == codigoPostal):
            client_info = {
                "nombre_cliente": val.get('nombre_cliente'),
                "codigo_cliente": val.get('codigo_cliente'),
                "codigo_postal": val.get('codigo_postal')
            }
            clientPostalCode.append(client_info)
    return clientPostalCode

# Filtrar por representante de ventas
def getClientByRepresentanteVentas(codeRepreVen):
    clientRepreVentas = []
    for val in cli.clientes:
        if (val.get('codigo_empleado_rep_ventas') == codeRepreVen):
            clientRepreVentas.append(val)
    return clientRepreVentas