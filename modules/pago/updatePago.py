# Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
from os import system
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener pagos desde un módulo
import modules.pago.getPago as gP


# Función que muestra un menú para actualizar pagos
def menuUpdatePago():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idPago = input("Ingrese el ID del pago que desea actualizar: ")
        pago = gP.getPagoCodigo(idPago)

        if pago:
            print("Pago encontrado:")
            actualizarPago(pago)
        else:
            print("Pago no encontrado.")

        continuar = input("¿Desea actualizar otro pago? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un pago con nuevos datos
def actualizarPago(pago):
    try:
        for i, (key, val) in enumerate(pago.items()):
            if key != "id" and key != "codigo_Pago" and key != "codigo_cliente":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en el pago
        confirmacion = input(
            "\n¿Desea realizar cambios en este pago? (si/no): ").lower()
        if confirmacion == "si":
            while True:
                # Preguntar si se desea editar un dato específico o modificar toda la información
                opcion = input(
                    "\n¿Desea editar un dato específico o modificar toda la información? (dato/toda): ").lower()
                if opcion == "dato":
                    # Editar un dato específico
                    keySeleccionada = input(
                        "Ingrese el campo que desea editar: ")
                    if re.match(r'^\d+$', keySeleccionada):
                        keySeleccionada = int(keySeleccionada)
                        if 0 <= keySeleccionada < len(pago):
                            key = list(pago.keys())[keySeleccionada]
                            if key in pago:
                                nuevoValor = input(
                                    f"Ingrese el nuevo valor para '{key}': ")
                                # Validar si el campo es numérico antes de convertirlo
                                if key == "total":
                                    if isinstance(pago[key], int):
                                        try:
                                            nuevoValor = int(nuevoValor)
                                        except ValueError:
                                            print(
                                                f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                    else:
                                        nuevoValor = int(nuevoValor)  # Conv
                                pago[key] = nuevoValor
                                print("Cliente actualizado.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información del pago excepto el campo "id" y "codigo_Pago"
                    nuevosDatos = {}
                    for key in pago.keys():
                        if key != "id" and key != "codigo_Pago" and key != "codigo_cliente":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            # Validar si el campo es numérico antes de convertirlo
                            if key == "total":
                                if isinstance(pago[key], int):
                                    try:
                                        nuevoValor = int(nuevoValor)
                                    except ValueError:
                                        print(
                                            f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                else:
                                    nuevoValor = int(nuevoValor)  # Conv
                            pago[key] = nuevoValor
                        nuevosDatos[key] = nuevoValor
                    pago.update(nuevosDatos)
                    print("pago actualizado.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5006/pagos/{pago['id']}"
            response = requests.put(url, json=pago)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información del pago actualizada en el servidor.")

        else:
            print("No se realizarán cambios en el pago.")

    except Exception as e:
        print(f"Error: {e}")
