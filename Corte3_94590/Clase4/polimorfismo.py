#polimorfismo= indicar un metodo en el que se comporta un elemento(hijo) 
class Ciudadano():
    def __init__(self,idioma:str, nombre:str):  
        self.__idioma=idioma
        self.__nombre=nombre

#---------- Setters ------------
    def setIdioma(self,idioma:str):
        self.__idioma=idioma

    def setNombre(self,nombre:str):
        self.__nombre=nombre

 #---------- Getters ------------
    def getIdioma(self):
        return self.__idioma
    
    def getNombre(self):
        return self.__nombre
#------------Sobrecarga-----------


class Colombiano(Ciudadano):
    def __init__(self, idioma: str, nombre: str, cc:str):   #super para llamar a la super clase(ciudadano)
        super().__init__(idioma, nombre)
        self.__cc=cc
    
    def setCC(self, cc:str):
        self.__cc=cc

    def getCC(self):
        return self.__cc
    
#----------Sobrecarga------------
    def saludo(self):
        return f'Qiubo parce'
    
class Ingles(Ciudadano):
    def __init__(self, idioma: str, nombre: str, id:str):   #super para llamar a la super clase(ciudadano)
        super().__init__(idioma, nombre)
        self.__id=id
    
    def setCC(self, id:str):
        self.__id=id

    def getCC(self):
        return self.__id
    
#----------Sobrecarga------------
    def saludo(self):
        return f'Hello my friend!'
    
class Chino(Ciudadano):
    def __init__(self, idioma: str, nombre: str, sfz:str):   #super para llamar a la super clase(ciudadano)
        super().__init__(idioma, nombre)
        self.__sfz=sfz
    
    def setCC(self, sfz:str):
        self.__sfz=sfz

    def getCC(self):
        return self.__sfz
    
#----------Sobrecarga------------
    def saludo(self):
        return f'Hola c'  
    
    def darSaludo(objeto):
        return objeto.saludo()

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


if __name__=='__main__':
    main()