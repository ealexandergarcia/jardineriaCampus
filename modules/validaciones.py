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
# Expresion regular que valida el correo electronico
def valEmail(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email)

# Expresion regular que verifica si la cadena cumple con el formato yyyy-mm-dd
def valFecha(fecha):
    patron = r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])'
    return re.match(patron, fecha)

# expresión regular busca patrones que cumplan con las siguientes condiciones:
# Comienza con una letra mayúscula.
# Luego, puede haber cero o más palabras (cada una comenzando con una letra mayúscula y seguida de cero o más caracteres que no sean un punto).
# Cada palabra puede terminar con un punto opcional.
def valTextoLargo(texto):
    patron = r'^[A-Z][^.]*\.?(\s*[A-Z][^.]*\.?)*$'
    return re.match(patron, texto)

def solicitar_confirmacion(nombre_cliente):
    pattern = r'\b(s[ií]|S[IÍ])\b'
    confirmacion = input(f"Si realmente desea modificar la informacion de {nombre_cliente} escriba Si: ")
    return re.match(pattern, confirmacion)