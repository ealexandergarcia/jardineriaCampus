# Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
from os import system
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener productos desde un módulo
import modules.producto.getProducto as gP


# Función que muestra un menú para actualizar productos
def menuUpdateProductos():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idProductos = input(
            "Ingrese el ID del producto que desea actualizar: ")
        productos = gP.getProductCodigo(idProductos)

        if productos:
            print("Productos encontrado:")
            actualizarProductos(productos)
        else:
            print("Productos no encontrado.")

        continuar = input(
            "¿Desea actualizar otro productos? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un productos con nuevos datos
def actualizarProductos(productos):
    try:
        for i, (key, val) in enumerate(productos.items()):
            if key != "id" and key != "codigo_producto":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en el productos
        confirmacion = input(
            "\n¿Desea realizar cambios en este producto? (si/no): ").lower()
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
                        if 0 <= keySeleccionada < len(productos):
                            key = list(productos.keys())[keySeleccionada]
                            if key in productos:
                                nuevoValor = input(
                                    f"Ingrese el nuevo valor para '{key}': ")
                                # Validar si el campo es numérico antes de convertirlo
                                if key == "cantidadEnStock" or key == "precio_venta" or key == "precio_proveedor":
                                    if isinstance(productos[key], int):
                                        try:
                                            nuevoValor = int(nuevoValor)
                                        except ValueError:
                                            print(
                                                f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                    else:
                                        nuevoValor = int(nuevoValor)  # Conv
                                productos[key] = nuevoValor
                                print("Empleado actualizado.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información del productos excepto el campo "id" y "codigo_Productos"
                    nuevosDatos = {}
                    for key in productos.keys():
                        if key != "id" and key != "codigo_producto":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            if key == "cantidadEnStock" or key == "precio_venta" or key == "precio_proveedor":
                                if isinstance(productos[key], int):
                                    try:
                                        nuevoValor = int(nuevoValor)
                                    except ValueError:
                                        print(
                                            f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                else:
                                    nuevoValor = int(nuevoValor)  # Conv
                            nuevosDatos[key] = nuevoValor
                    productos.update(nuevosDatos)
                    print("productos actualizado.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5008/productos/{productos['id']}"
            response = requests.put(url, json=productos)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información del productos actualizada en el servidor.")

        else:
            print("No se realizarán cambios en el productos.")

    except Exception as e:
        print(f"Error: {e}")
