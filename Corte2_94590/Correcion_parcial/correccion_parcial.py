from random import choice as c


def repartir():
    deck='A23456789JQK'
    return c(deck)

def valor(card):
    jack=['J','Q','K']

    if card in jack:
        card=10
    elif card=='A':
        card=11
    else:
        card=int(card)
    return card 

def conteo(mano,card):
    cartas=[]
    for i in range (len(mano,card)):  
        cartas.append(cartas,card)
    print(cartas)
    print(f'conteo: {sum(cartas)}')

def inicio():
    mano=[]
    mano.append(repartir())
    mano.append(repartir())
    print(f'Mano inicial: {mano}')
    conteo_mano = conteo(mano)
    print(f'Conteo inicial: {conteo_mano}')

    if conteo_mano==21:
         print("Black Jack")
         return

    opc='y'
    while opc=='y':
        opc=input('Quiere otra carta? (y/n)')
        if opc=='y':
            nueva_carta = repartir()
            mano.append(repartir())
            print(f'Nueva carta: {nueva_carta}')
            conteo_mano = conteo(mano)
            print(f'Mano actual: {mano}')
            print(f'Conteo actual: {conteo_mano}')
        if conteo_mano > 21:
                print('------------Busted---------')
                break
        elif conteo_mano==21:
                print("-----------Black Jack--------")
                break
        elif opc == 'n':
            break
        else:
            print('Opción inválida')
            opc = 'y'
        if conteo_mano < 21:
            print('------Fin de la apuesta------')
       



if __name__=='__main__':
    inicio()