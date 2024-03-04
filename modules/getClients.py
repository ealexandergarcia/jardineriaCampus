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

def getAllClientPaisRegionCiudad(pais,region = None,ciudad = None):
    clientZone = []
    for val in cli.clientes:
        if(val.get('pais') == pais):
            if(region != val.get('region')):
                clientZone.append(val)
            else:
                clientZone.append(val)
            # if((region != None and val.get('region')==region)):
            #     clientZone.append(val)
            # elif(val.get('region')==region):
            #     clientZone.append(val)
           
        # if (val.get('pais') == pais or 
        #     (val.get('region') == region or val.get('region') == None) or 
        #     (val.get('ciudad') == ciudad or val.get('ciudad') == None)):
        #     clientZone.append(val)

        # if (val.get('pais') == pais):
        #      if (val.get('region') == region or val.get('region') == None):
        #          if(val.get('ciudad') == ciudad or val.get('ciudad') == None):
        #             clientZone.append(val)
    # print(clientZone)
    return clientZone

