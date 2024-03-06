import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []

    for val in of.oficina:
        codigoCiudad.append({
            "Codigo": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Otro
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "Ciudad": val.get("ciudad"),
                "Telefono": val.get("telefono"),
                "Oficinas": val.get("codigo_oficina"),
                "Pais": val.get("pais"),
            })
    return ciudadTelefono

