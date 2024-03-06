import storage.empleado as emp

# Devuelve los datos de los empleados que tienen un jefe = 7


def getAllNombresApellidoEmailJefe(codigo):
    NombresApellidoEmailJefe = []
    for val in emp.empleados:
        if (val.get("codigo_jefe")) == codigo:
            NombresApellidoEmailJefe.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe"),
            })
    return NombresApellidoEmailJefe

# Devuelve el nombre del puesto, nombre, apellidos y email de la empresa


def getAllNombrePuestoNombreApellidoEmailJefe():
    NombrePuestoNombreApellidoEmail = []
    for val in emp.empleados:
        if (val.get("codigo_jefe")) == None:
            NombrePuestoNombreApellidoEmail.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email")
            })
    return NombrePuestoNombreApellidoEmail

# Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados que no sean Representante Ventas


def getAllNombreApellidoNombrePuesto():
    NombrePuestoNombreApellidoEmail = []
    for val in emp.empleados:
        if (val.get("puesto")) != "Representante Ventas":
            NombrePuestoNombreApellidoEmail.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto": val.get("puesto")
            })
    return NombrePuestoNombreApellidoEmail
