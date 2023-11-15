class Producto():
    def __init__(self,nombre:str, precio:float, cantidad_disponible:int):
        self._nombre=nombre
        self._precio=precio
        self._cantidad_disponible=cantidad_disponible
    
    def getnombre(self):
        return self._nombre
    def getprecio(self):
        return self._precio
    def getcantidad_disponible(self):
        return self._cantidad_disponible
    def info_producto(self):
        return f'Nombre:{self._nombre}, Precio: {self._precio}, Cantidad_disponible: {self._cantidad_disponible}'
    
    def restar_cantidad(self, cantidad):
        if self._cantidad_disponible>cantidad:
            self._cantidad_disponible<=cantidad
            return True
        else:
            return False
    
    def verificar_disponibilidad(self):
        return self.verificar_disponibilidad>0
    
    def setnombre(self, nombre:str):
        self._nombre=nombre 
    def setprecio(self, precio:float):
        self._precio=precio
    def setcantidad_disponible(self, cantidad_disponible:int):
        self._cantidad_disponible=cantidad_disponible

class Snack():
    def __init__(self,tipo:str, nombre:str , precio:int ,cantidad_disponible:int):
        self._nombre=nombre
        self._precio=precio
        self._cantidad_disponible=cantidad_disponible
        self.tipo=tipo
    
    def info_producto(self):
        return f'Clase: {self.tipo}' + {self.info_producto}

class Bebidas():
    def __init__(self,clase:str, nombre:str , precio:int ,cantidad_disponible:int, tamaño:str):
        self._nombre=nombre
        self._precio=precio
        self._cantidad_disponible=cantidad_disponible
        self.clase=clase
        self.tamaño=tamaño
    def info_producto(self):
        return f'Clase: {self.clase}, Tamaño: {self.tamaño}' + {self.info_producto}
    
class Dispensadora():
    def __init__(self, nombre:str, precio:float):
        self.nombre=nombre
        self.precio=precio
        self.inventario={}
        self.total_ventas=0 

    def agregas_producto(self, producto, ):
        if producto not in self.inventario:
            self.inventario[producto]=producto
        else:
            print('Producto ya existe en el inventario')
    
    def realizar_venta(self, cantidad:int , producto:str):
        self.cantidad=cantidad
        self.producto=producto
        if producto in self.inventario:
            self.total_ventas+=producto*cantidad
            return 'Ya se realizo la venta'


def main():
    pass