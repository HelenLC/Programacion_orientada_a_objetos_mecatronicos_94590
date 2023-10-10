class IMC():
    def __init__(self): 
        self.nombre=None
        self.estatura=None
        self.peso=None
        
    def setNombre(self,nombre :str):
        self.__nombre = nombre

    def setAltura(self,altura:int):
        self.__altura = altura

    def setPeso(self,peso :float):
        self.__peso =peso

    def calcular_IMC(peso, altura):
        IMC =peso/((altura / 100) ** 2)
        if IMC <= 18.5:
            return 'Por debajo'
        elif IMC <= 24.9:
            return 'Saludable'
        elif IMC <= 29.9:
            return 'Sobrepeso'
        elif IMC <= 34.9:
            return 'Obesidad 1'
        elif IMC <= 39.9:
            return 'Obesidad 2'
        else:
            return 'Obesidad 3'

def main():
    Pedro_Caceres=IMC()
    Pedro_Caceres.nombre='Pedro Caceres'
    Pedro_Caceres.estatura=188
    Pedro_Caceres.peso=97
    print(f'{Pedro_Caceres.nombre}:{Pedro_Caceres.calcular_IMC()}')

    Maria_Perez=IMC()
    Maria_Perez.nombre='Maria Perez'
    Maria_Perez.estatura=160
    Maria_Perez.peso=47
    print(f'{Maria_Perez.nombre}:{Maria_Perez.calcular_IMC()}')

    Julian_Dominguez=IMC()
    Julian_Dominguez.nombre='Julian Dominguez'
    Julian_Dominguez.estatura=158
    Julian_Dominguez.peso=58
    print(f'{Julian_Dominguez.nombre}:{Julian_Dominguez.calcular_IMC()}')

    Jessica_Fuentes=IMC()
    Jessica_Fuentes.nombre='Jessica Fuentes'
    Jessica_Fuentes.estatura=170
    Jessica_Fuentes.peso=58
    print(f'{Jessica_Fuentes.nombre}:{Jessica_Fuentes.calcular_IMC()}')


if __name__=='__main__':
    calcular_IMC=()
    main()