class Pokemon(): #constructor
    def __init__(self): #self: permite indicar el objeto; permite colocar los atributos, caracteristicas etc.
        self.nombre=None
        self.color=None #None=nada, no se le esta asignando ningun valor
        self.categoria=None
        self.tipo=None
        self.codigo=None
#variable=se manejan en minuscula
#clases= La primera letra es en mayuscula como Pokemon
#funcion=main y en minuscula
#campo/atributo= se usan igual que las variables
#metodos=Primera palabra en minuscula y la segunda en mayuscula


    def correr(self):
        return 'Estoy corriendo'
    def volar(self):
        return 'Estoy volando'
    def quemar(self):
        return 'Estoy quemando'



def main():
    Pikachu=Pokemon()
    Pikachu.nombre='Pikachu'
    Pikachu.color='Amarillo'
    Pikachu.categoria='Raton'
    Pikachu.tipo='Electrico'
    Pikachu.codigo=25
    print(f'{Pikachu.nombre}:{Pikachu.correr()}')

    Charizard=Pokemon()
    Charizard.nombre='Charizard'
    Charizard.color='Naranja'
    Charizard.categoria='Dragon'
    Charizard.tipo='Fuego'
    Charizard.codigo=6
    print(f'{Charizard.nombre}:{Charizard.volar()}')

    Ninetales=Pokemon()
    Ninetales.nombre='Ninentales'
    Ninetales.color='Baige'
    Ninetales.categoria='Zorro'
    Ninetales.tipo='Fuego'
    Ninetales.codigo=38
    Ninetales=Pikachu
    print(f'{Ninetales.nombre}:{Ninetales.quemar()}')




if __name__=='__main__':
    main()