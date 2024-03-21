from os import system # Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener empleados desde un módulo
import modules.empleado.getEmpleados as gE


# Función que muestra un menú para actualizar empleados
def menuUpdateEmpleados():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idEmpleado = input("Ingrese el ID del empleado que desea actualizar: ")
        empleado = gE.getEmpleadoCodigo(idEmpleado)

        if empleado:
            print("Empleado encontrado:")
            actualizarEmpleado(empleado)
        else:
            print("Empleado no encontrado.")

        continuar = input("¿Desea actualizar otro Empleado? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un Empleado con nuevos datos
def actualizarEmpleado(empleado):
    try:
        for i, (key, val) in enumerate(empleado.items()):
            if key != "id" and key != "codigo_empleado":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en el empleado
        confirmacion = input(
            "\n¿Desea realizar cambios en este empleado? (si/no): ").lower()
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
                        if 0 <= keySeleccionada < len(empleado):
                            key = list(empleado.keys())[keySeleccionada]
                            if key in empleado:
                                nuevoValor = input(f"Ingrese el nuevo valor para '{key}': ")
                                # Validar si el campo es numérico antes de convertirlo
                                if key == "codigo_jefe":
                                    if isinstance(empleado[key], int):
                                        try:
                                            nuevoValor = int(nuevoValor)
                                        except ValueError:
                                            print(
                                                f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                    else:
                                        nuevoValor = int(nuevoValor)  # Conv
                                empleado[key] = nuevoValor
                                print("Empleado actualizado.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información del empleado excepto el campo "id" y "codigo_empleado"
                    nuevosDatos = {}
                    for key in empleado.keys():
                        if key != "id" and key != "codigo_empleado":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            # Validar si el campo es numérico antes de convertirlo
                            if key == "codigo_jefe":
                                if isinstance(empleado[key], int):
                                    try:
                                        nuevoValor = int(nuevoValor)
                                    except ValueError:
                                        print(
                                            f"Error: El valor proporcionado para '{key}' no es un número válido.")
                                else:
                                    # Convertir a entero si es posible
                                    nuevoValor = int(nuevoValor)
                            nuevosDatos[key] = nuevoValor
                    empleado.update(nuevosDatos)
                    print("Empleado actualizado.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5003/empleados/{empleado['id']}"
            response = requests.put(url, json=empleado)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información del empleado actualizada en el servidor.")

        else:
            print("No se realizarán cambios en el empleado.")

    except Exception as e:
        print(f"Error: {e}")
