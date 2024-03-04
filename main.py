from tabulate import tabulate
import modules.getClients as cliente
# print(tabulate(cliente.getAllClientName(),tablefmt="grid"))

# print(cliente.getOneClientCodigo(15))

# print(cliente.getAllClientCreditCiudad(5000,"London"))

print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia","Sur"),tablefmt="grid"))
# cliente.getAllClientPaisRegionCiudad("France"," ","Paris")

