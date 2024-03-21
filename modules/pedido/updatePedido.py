from os import system # Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener pedidos desde un módulo
import modules.pedido.getPedido as gP


# Función que muestra un menú para actualizar pedidos
def menuUpdatePedidos():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idPedidos = input("Ingrese el ID del pedido que desea actualizar: ")
        pedidos = gP.getPedidoCodigo(idPedidos)

        if pedidos:
            print("Pedidos encontrado:")
            actualizarPedidos(pedidos)
        else:
            print("Pedidos no encontrado.")

        continuar = input("¿Desea actualizar otro pedidos? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un pedidos con nuevos datos
def actualizarPedidos(pedidos):
    try:
        for i, (key, val) in enumerate(pedidos.items()):
            if key != "id" and key != "codigo_Pedidos" and key != "codigo_cliente":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en el pedidos
        confirmacion = input(
            "\n¿Desea realizar cambios en este pedidos? (si/no): ").lower()
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
                        if 0 <= keySeleccionada < len(pedidos):
                            key = list(pedidos.keys())[keySeleccionada]
                            if key in pedidos:
                                nuevoValor = input(f"Ingrese el nuevo valor para '{key}': ")
                                pedidos[key] = nuevoValor
                                print("pedidos actualizado.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información del pedidos excepto el campo "id" y "codigo_Pedidos"
                    nuevosDatos = {}
                    for key in pedidos.keys():
                        if key != "id" and key != "codigo_Pedidos":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            nuevosDatos[key] = nuevoValor
                    pedidos.update(nuevosDatos)
                    print("pedidos actualizado.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5007/pedidos/{pedidos['id']}"
            response = requests.put(url, json=pedidos)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información del pedidos actualizada en el servidor.")

        else:
            print("No se realizarán cambios en el pedidos.")

    except Exception as e:
        print(f"Error: {e}")
