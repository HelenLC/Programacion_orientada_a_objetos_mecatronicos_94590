class Articulos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_bruto(self):
        return self.precio

    def calcular_valor_iva(self):
        return 0


class Alimentos(Articulos):
    def calcular_valor_iva(self):
        return self.precio * 0.05


class ArticulosBasicos(Articulos):
    def calcular_valor_iva(self):
        return self.precio * 0.19


class ArticulosLujo(Articulos):
    def calcular_valor_iva(self):
        return self.precio * 0.19


def calcular_precio_total(articulos):
    precio_total = 0
    valor_iva_total = 0

    for articulo in articulos:
        precio_total += articulo.calcular_precio_bruto()
        valor_iva_total += articulo.calcular_valor_iva()

    return precio_total, valor_iva_total
articulos = [
    Alimentos("Arroz", 1000),
    ArticulosBasicos("Jabón", 500),
    ArticulosLujo("Perfume", 2000)
]

# Calcular el precio bruto y el valor de IVA
precio_total, valor_iva_total = calcular_precio_total(articulos)

# Imprimir los resultados
print(f"Precio bruto total: {precio_total}")
print(f"Valor de IVA total: {valor_iva_total}")