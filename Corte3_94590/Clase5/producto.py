class Producto():
    def __init__(self,nombre:str, precio:float, cantidad_disponible:int):   
        self.__nombre=nombre
        self.__precio=precio
        self.__cantidad_disponible=cantidad_disponible
 #---------- Setters ------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setPrecio(self,precio:float):
        self.__precio=precio
        
    def setCantidad_disponible(self,cantidad_disponible:int):
        self.__cantidad_disponible=cantidad_disponible

    
    #---------- Getters ------------
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def getcCntidad_disponible(self):
        return self.__cantidad_disponible
    
class Dispensadora(Producto):
    def __init__(self,producto:str, total_ventas:float):   
        self.__producto=producto
        self.__total_ventas=total_ventas
 #---------- Setters ------------
    def setProducto(self,producto:str):
        self.__producto=producto

    def setTotal_ventas(self,total_ventas:float):
        self.__total_ventas=total_ventas
        

    
    #---------- Getters ------------
    def getProducto(self):
        return self.__producto
    
    def getTotal_ventas(self):
        return self.__total_ventas
    
    def main():
        ciudadano1=Ciudadano('Franses','Carla Bruni','12549785558')
        ciudadano2=Colombiano('Español', 'Radamel Garcia','1658947952')
        ciudadano3=Ingles('Ingles','David Beckham','AS54896665')
        ciudadano4=Chino('Mandarin','ShengLong','CH84955577') 
        print('-------------Presentacion-----------------')
        print(f'Ciudadano:{ciudadano1.getNombre()}, Idioma:{ciudadano1.getIdioma()}')
        print(f'Ciudadano:{ciudadano2.getNombre()}, Idioma:{ciudadano2.getIdioma()}')
        print(f'Ciudadano:{ciudadano3.getNombre()}, Idioma:{ciudadano3.getIdioma()}')
        print(f'Ciudadano:{ciudadano4.getNombre()}, Idioma:{ciudadano4.getIdioma()}')

        print('\n---------------Como saluda el mundo------------------')
        print(f'{Ciudadano}'+darSaludo)

        print(ciudadano2.saludo())

    
