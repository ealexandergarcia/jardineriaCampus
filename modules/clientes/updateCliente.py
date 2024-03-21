from os import system # Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener clientes desde un módulo
import modules.clientes.getClients as gC


# Función que muestra un menú para actualizar clientes
def menuUpdateCliente():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idCliente = input("Ingrese el ID del cliente que desea actualizar: ")
        cliente = gC.getClienteCodigo(idCliente)

        if cliente:
            print("Cliente encontrado:")
            actualizarCliente(cliente)
        else:
            print("Cliente no encontrado.")

        continuar = input("¿Desea actualizar otro cliente? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un cliente con nuevos datos
def actualizarCliente(cliente):
    try:
        for i, (key, val) in enumerate(cliente.items()):
            if key != "id" and key != "codigo_cliente":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en el cliente
        confirmacion = input(
            "\n¿Desea realizar cambios en este cliente? (si/no): ").lower()
        if confirmacion == "si":
            while True:
                # Preguntar si se desea editar un dato específico o modificar toda la información
                opcion = input(
                    "\n¿Desea editar un dato específico o modificar toda la información? (dato/toda): ").lower()
                if opcion == "dato":
                    # Editar un dato específico
                    keySeleccionada = input("Ingrese el campo que desea editar: ")
                    if re.match(r'^\d+$', keySeleccionada):
                        keySeleccionada = int(keySeleccionada)
                        if 0 <= keySeleccionada < len(cliente):
                            key = list(cliente.keys())[keySeleccionada]
                            if key in cliente:
                                nuevoValor = input(f"Ingrese el nuevo valor para '{key}': ")
                                # Validar si el campo es numérico antes de convertirlo
                                if key == "codigo_empleado_rep_ventas" or key == "limite_credito":
                                    if isinstance(cliente[key], int):
                                        try:
                                            nuevoValor = int(nuevoValor)
                                        except ValueError:
                                            print(
                                                f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                    else:
                                        nuevoValor = int(nuevoValor)  # Conv
                                cliente[key] = nuevoValor
                                print("Cliente actualizado.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información del cliente excepto el campo "id" y "codigo_cliente"
                    nuevosDatos = {}
                    for key in cliente.keys():
                        if key != "id" and key != "codigo_cliente":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            # Validar si el campo es numérico antes de convertirlo
                            if key == "codigo_empleado_rep_ventas" or key == "limite_credito":
                                if isinstance(cliente[key], int):
                                    try:
                                        nuevoValor = int(nuevoValor)
                                    except ValueError:
                                        print(
                                            f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                else:
                                    # Convertir a entero si es posible
                                    nuevoValor = int(nuevoValor)
                            nuevosDatos[key] = nuevoValor
                    cliente.update(nuevosDatos)
                    print("Cliente actualizado.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5001/cliente/{cliente['id']}"
            response = requests.put(url, json=cliente)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información del cliente actualizada en el servidor.")

        else:
            print("No se realizarán cambios en el cliente.")

    except Exception as e:
        print(f"Error: {e}")
