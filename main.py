from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
# print(empleado.emp.empleados)


# print(tabulate(cliente.getAllClientName(),tablefmt="grid"))

# print(cliente.getOneClientCodigo(15))

# print(cliente.getAllClientCreditCiudad(5000,"London"))

# print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain","Cataluña","Barcelona"),tablefmt="grid"))

# print(tabulate(cliente.getClientCodigoPostal("28942"), headers="keys",tablefmt="grid"))

# print(tabulate(cliente.getClientByRepresentanteVentas(11),tablefmt="grid"))

# print(tabulate(cliente.getClientByCountryAndPostalCode("Spain","28942"), headers="keys",tablefmt="grid"))

# print(tabulate(cliente.getClientByContactNameAndCountry("Jose","Spain"), headers="keys",tablefmt="grid"))

# print(tabulate(oficina.getAllCodigoCiudad(), headers="keys",tablefmt="grid"))

# print(tabulate(oficina.getAllCiudadTelefono("España")))

# print(tabulate(empleado.getAllNombresApellidoEmailJefe(7), headers="keys",tablefmt="grid"))

# print(tabulate(empleado.getAllNombrePuestoNombreApellidoEmailJefe(), headers="keys",tablefmt="grid"))

# print(tabulate(empleado.getAllNombreApellidoNombrePuesto(), headers="keys",tablefmt="grid"))

# print(tabulate(cliente.getAllClientesEspañoles("Spain"),headers="keys", tablefmt="grid"))

print(pago.getAllClientPayYear())