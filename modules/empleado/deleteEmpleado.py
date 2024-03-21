import requests
import modules.empleado.getEmpleados as gE

def deleteEmpleado(id):
    data =  gE.getEmpleadoCodigo(id)

    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.ok:
            print("Eliminado con éxito")
        else:
            print(f"Error al guardar: {peticion.status_code}")
