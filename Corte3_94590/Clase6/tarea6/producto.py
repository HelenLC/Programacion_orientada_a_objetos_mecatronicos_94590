class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_disponible = cantidad_disponible

    def get_nombre(self) -> str:
        return self.__nombre

    def get_precio(self) -> float:
        return self.__precio

    def info_producto(self) -> str:
        return f'Nombre: {self.__nombre}, Precio: {self.__precio}, Cantidad disponible: {self.__cantidad_disponible}'

    def restar_cantidad(self, cantidad: int) -> bool:
        if self.__cantidad_disponible >= cantidad:
            self.__cantidad_disponible -= cantidad
            return True
        else:
            print("Error: Cantidad insuficiente.")
            return False

    def verificar_disponibilidad(self) -> bool:
        return self.__cantidad_disponible > 0


class Snack(Producto):
    def __init__(self, tipo: str, nombre: str, precio: float, cantidad_disponible: int):
        super().__init__(nombre, precio, cantidad_disponible)
        self.tipo = tipo

    def info_producto(self) -> str:
        return f'{super().info_producto()}, Tipo: {self.tipo}'


class Bebida(Producto):
    def __init__(self, clase: str, tamaño: str, nombre: str, precio: float, cantidad_disponible: int):
        super().__init__(nombre, precio, cantidad_disponible)
        self.clase = clase
        self.tamaño = tamaño

    def info_producto(self) -> str:
        return f'{super().info_producto()}, Clase: {self.clase}, Tamaño: {self.tamaño}'


class Dispensadora:
    def __init__(self, productos_iniciales=None):
        self.__productos = productos_iniciales or []
        self.__total_ventas = 0.0

    def agregar_producto(self, producto: Producto) -> None:
        if isinstance(producto, Producto):
            self.__productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado a la dispensadora.")
        else:
            print("Error: El objeto no es un Producto válido.")

    def realizar_venta(self, cantidad: int, producto_nombre: str) -> None:
        for prod in self.__productos:
            if prod.get_nombre() == producto_nombre:
                if prod.restar_cantidad(cantidad):
                    self.__total_ventas += cantidad * prod.get_precio()
                    print(f'Venta de {cantidad} unidades de {producto_nombre} realizada.')
                else:
                    print(f'Error: No hay suficiente cantidad disponible de {producto_nombre} para la venta.')
                return
        print(f'Error: Producto {producto_nombre} no encontrado en la dispensadora.')

    def obtener_total_venta(self) -> float:
        return self.__total_ventas

producto1 = Snack("Salado", "Papas", 2000, 10)
producto2 = Snack("Dulce", "Chocorramo", 2700, 5)
producto3 = Bebida("Agua", "250ml", "Cristal", 2800, 6)
producto4 = Bebida("Gaseosa", "500ml", "Coca Cola", 4000, 8)

productos_preexistentes = [producto1, producto2, producto3, producto4]

dispensadora = Dispensadora(productos_preexistentes)

def main():
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar productos en la dispensadora")
        print("4. Mostrar total de ventas")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad_disponible = int(input("Ingrese la cantidad disponible del producto: "))
            tipo_producto = input("Es Snack o Bebida: ").capitalize()

            if tipo_producto == "Snack":
                tipo = input("Ingrese el tipo de snack: ")
                nuevo_producto = Snack(tipo, nombre, precio, cantidad_disponible)
            elif tipo_producto == "Bebida":
                clase = input("Ingrese la clase de bebida: ")
                tamaño = input("Ingrese el tamaño de la bebida: ")
                nuevo_producto = Bebida(clase, tamaño, nombre, precio, cantidad_disponible)
            else:
                print("Tipo de producto no reconocido.")

            dispensadora.agregar_producto(nuevo_producto)

        elif opcion == "2":
            producto_nombre = input("Ingrese el nombre del producto para la venta: ")
            cantidad_venta = int(input("Ingrese la cantidad a vender: "))
            dispensadora.realizar_venta(cantidad_venta, producto_nombre)

        elif opcion == "3":
            print("\nInformación de productos en la dispensadora:")
            for producto in dispensadora._Dispensadora__productos:
                print(producto.info_producto())

        elif opcion == "4":
            print(f"\nTotal de ventas: ${dispensadora.obtener_total_venta()}")

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")
        
if __name__=='__main__':
    main()
