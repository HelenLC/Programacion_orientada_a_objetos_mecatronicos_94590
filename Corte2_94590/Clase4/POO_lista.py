class Pokemon(): 
    def __init__(self): 
        self.nombre=None
        self.color=None 
        self.categoria=None
        self.tipo=None
        self.codigo=None

    def ataquepokemon(self):
        return 'Estoy atacando'  #tipo tring

def main():
    pokemones=[]
    opc='n'
    while 1: #1=True
        pokemon=Pokemon()
        pokemon.nombre=input('Nombre del pokemon: ')
        pokemon.categoria=input('Categoria del pokemon: ')
        pokemon.color=input('Color del pokemon: ')
        pokemon.tipo=input('Tipo del pokemon: ')
        pokemon.codigo=input('Ingrese el codigo del pokemon: ')
        pokemones.append(pokemon) #Append=agregar a la lista
        
        opc=input('Desea inscribir otro pokemon?: (y/n): ')
        if opc=='n':
            break
        elif opc!='y':
            print('Opcion invalida')
    
    print('--------pokedex----------')
    for i in pokemones:
        print(f'Nombre:{i.nombre}\n'
              f'Codigo:{i.codigo}\n'
              f'Tipo:{i.tipo}\n'
              f'Ataca!...{i.ataquepokemon()}\n'
              '--------------')



if __name__=='__main__':
    main()