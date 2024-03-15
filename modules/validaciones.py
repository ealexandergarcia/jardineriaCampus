import re


def validacionCodProd(codigo):
    val = re.match(r'^[A-Z]{2}-\d{3}$', codigo)
    return val

def valiNombres(nombre):
    val = re.match(r'^([A-Z][a-z]*\s*)+$', nombre)
    return val
