import re


def validacionCodProd(codigo):
    patron = re.match(r'^[A-Z]{2}-\d{3}$', codigo)
    return patron


def valiNombres(nombre):
    patron = re.match(r'^([A-Z][a-z]*\s*)+$', nombre)
    return patron


def valiTel(telefono):
    patron = re.match(r'^\+?\d{1,3}\s?\d{2,3}\s?\d{6,7}$', telefono)
    return patron


def valiDire(direccion):
    patron = re.match(r'^[\w\s,.\-#]{4,}(?: [\w\s,.\-#]+)*$', direccion)
    return patron

# expresión regular permitirá nombres de ciudades que consistan en letras,
# espacios en blanco, guiones, apóstrofes, comas y puntos.
def valUbi(ubicacion):
    patron = r'^[a-zA-Z\s\-\'.,áéíóúÁÉÍÓÚãäëïöüÄËÏÖÜñÑçÇ´]+(?: [a-zA-Z\s\-\'.,áéíóúÁÉÍÓÚäëïöüÄËÏÖÜñÑçÇ´]+)*$'
    return re.match(patron, ubicacion) is not None

# expresión regular valida códigos postales en el formato "XXXXX" o "XXXXX-XXXX",
# donde "X" representa un dígito.
def valCodPostal(codigo_postal):
    patron = r'^\d{5}(?:-\d{4})?$'
    return re.match(patron, codigo_postal) is not None
