from os import system # Importa la función 'system' del módulo 'os' para realizar limpieza de pantalla
import requests  # Importa el módulo 'requests' para realizar solicitudes HTTP
import re  # Importa el módulo 're' para utilizar expresiones regulares
# Importa una función para obtener oficinas desde un módulo
import modules.oficina.getOficina as gO


# Función que muestra un menú para actualizar oficinas
def menuUpdateOficina():
    # Expresión regular para verificar si la cadena es "si"
    regexSi = re.compile(r'^si$', re.IGNORECASE)
    system("clear")
    while True:
        idOficina = input("Ingrese el ID de la oficina que desea actualizar: ")
        oficina = gO.getOficinaCodigo(idOficina)

        if oficina:
            print("Oficina encontrada:")
            actualizarCliente(oficina)
        else:
            print("Oficina no encontrado.")

        continuar = input("¿Desea actualizar otra oficina? (si/no): ").lower()
        if not regexSi.match(continuar):
            break


# Función para actualizar un oficina con nuevos datos
def actualizarCliente(oficina):
    try:
        for i, (key, val) in enumerate(oficina.items()):
            if key != "id":
                print(f"{i}. {key}: {val}")

        # Confirmar si se desean realizar cambios en la oficina
        confirmacion = input(
            "\n¿Desea realizar cambios en esta oficina? (si/no): ").lower()
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
                        if 0 <= keySeleccionada < len(oficina):
                            key = list(oficina.keys())[keySeleccionada]
                            if key in oficina:
                                nuevoValor = input(f"Ingrese el nuevo valor para '{key}': ")
                                # Validar si el campo es numérico antes de convertirlo
                                oficina[key] = nuevoValor
                                print("Oficina actualizada.")
                                break
                            else:
                                print("Campo no válido.")
                elif opcion == "toda":
                    # Modificar toda la información de la oficina excepto el campo "id"
                    nuevosDatos = {}
                    for key in oficina.keys():
                        if key != "id":
                            nuevoValor = input(
                                f"Ingrese el nuevo valor para '{key}': ")
                            nuevosDatos[key] = nuevoValor
                    oficina.update(nuevosDatos)
                    print("Oficina actualizada.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 'dato' o 'toda'.")

            # Realizar la actualización en el servidor
            url = f"http://154.38.171.54:5005/oficinas/{oficina['id']}"
            response = requests.put(url, json=oficina)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            print("Información de la oficina actualizada en el servidor.")

        else:
            print("No se realizarán cambios en la oficina.")

    except Exception as e:
        print(f"Error: {e}")
