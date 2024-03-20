from os import system
import json
import time
import requests
import modules.clientes.getClients as gC
import modules.validaciones as vali

def updateCliente(key, id):
    data = gC.getClienteCodigo(id)
    
    for i in data:
        print(i.keys())
        nuevoDato = input("Ingrese el nuevo dato: ")
        if (key == "limite_credito") in  i.keys():
            nuevoDato = int(nuevoDato)
            print(type(nuevoDato))
            # i[key] = nuevoDato
            # respuesta = requests.put(f"http://154.38.171.54:5001/cliente/{id}", timeout=10, data=json.dumps(i).encode("UTF-8"))
            # if respuesta.ok:
            #     print("Guardado con éxito")
            # else:
            #     print(f"Error al guardar: {respuesta.status_code}")
        else:
            print(type(nuevoDato))
            # i[key] = nuevoDato
            # respuesta = requests.put(f"http://154.38.171.54:5001/cliente/{id}", timeout=10, data=json.dumps(i).encode("UTF-8"))
            # if respuesta.ok:
            #     print("Guardado con éxito")
            # else:
            #     print(f"Error al guardar: {respuesta.status_code}")

def updateMenuCliente(id):
    # system("clear")
    data = gC.getClienteCodigo(id)
    if(len(data)):
        nombre= data[0].get("nombre_cliente")
        print(f"Datos del cliente: {nombre}")
        while True:
            system("clear")
            if vali.solicitar_confirmacion(nombre):
                print("""
            01. Modificar Nombre del cliente
            02. Modificar Nombre del contacto del cliente
            03. Modificar Apellido del contacto del cliente
            04. Modificar telefono del cliente
            05. Modificar fax del cliente
            06. Modificar la direccion principal del cliente
            07. Modificar la direccion secundaria del cliente
            08. Modificar la ciudad del cliente
            09. Modificar la region del cliente
            10. Modificar el pais del cliente
            11. Modificar el codigo postal del cliente
            12. Modificar el limite de credito del empleado
            13. Volver
            """)
                opcion = int(input("\n Ingrese su opcion: "))
                match opcion:
                    case 1:
                        updateCliente("nombre_cliente", id)
                        time.sleep(2)  # espera en segundos
                    case 2:
                        updateCliente("nombre_contacto",id)
                        time.sleep(2)  # espera en segundos
                    case 3:
                        updateCliente("apellido_contacto",id)
                        time.sleep(2)  # espera en segundos
                    case 4:
                        updateCliente("telefono",id)
                        time.sleep(2)  # espera en segundos
                    case 5:
                        updateCliente("fax",id)
                        time.sleep(2)  # espera en segundos
                    case 6:
                        updateCliente("linea_direccion1",id)
                        time.sleep(2)  # espera en segundos
                    case 7:
                        updateCliente("linea_direccion2",id)
                        time.sleep(2)  # espera en segundos
                    case 8:
                        updateCliente("ciudad",id)
                        time.sleep(2)  # espera en segundos
                    case 9:
                        updateCliente("region",id)
                        time.sleep(2)  # espera en segundos
                    case 10:
                        updateCliente("pais",id)
                        time.sleep(2)  # espera en segundos
                    case 11:
                        updateCliente("codigo_postal",id)
                        time.sleep(2)  # espera en segundos
                    case 12:
                        updateCliente("limite_credito",id)
                        time.sleep(2)  # espera en segundos
                    case _:
                        print("Opcion invalida")
                        time.sleep(2)  # espera en segundos
            else:
                print("La validacion no es corrcta")
                time.sleep(2)  # espera en segundos
                break
