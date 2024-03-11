import storage.producto as pr

# Devuelve un listado con todos los productos que pertenecen a la gama "ornamentales" y que
# tienen mas de 100 unidades en stock. El listado debe estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio

# def getAllProductosOrnamentales():
#     ProductosOrnamentales = []
#     for prodctos in prod.producto:
#         ProductosOrnamentales.append({
#                     "gama": prodctos.get("gama")
#                 })
#     unique_products = list({prodcto['gama']:prodcto for prodcto in ProductosOrnamentales}.values())
#     return unique_products

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= 100):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key= price)

    return condiciones

