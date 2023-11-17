class Articulos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def setNombre(self,nombre):
        self.nombre=nombre

    def setPrecio(self, precio):
        self.precio=precio

    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio

class No_Iva(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0

class Iva5(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.05

class Iva19(Articulos):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.19

def calcular_precio_bruto(articulo):
    return articulo.precio * (1 + articulo.iva)

def calcular_valor_iva(articulo):
    return articulo.precio * articulo.iva

# Crear una lista de alimentos de la canasta familiar
alimentos = [
    No_Iva("Lentejas", 3000),
    Iva5("Docena de huevos", 20000),
    Iva19("Harina", 3500)
]

def main():
    for articulo in alimentos:
        print("Nombre: ", articulo.nombre)
        print("Precio bruto: ", calcular_precio_bruto(articulo))
        print("Valor de IVA: ", calcular_valor_iva(articulo))

if __name__=='__main__':
    main()