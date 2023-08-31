def BlackJack():
    cartas=[2,3,4,5,6,7,8,9,'A=11', 'J=10', 'Q=10', 'K=10']
    print(cartas)

x=input('Desea agregar una carta?: ')
print()

def repartir(BlackJack):
    BlackJack.insert()
    print(BlackJack)


def suma(BlackJack):
    BlackJack.sum()
    cartas=cartas+cartas
    print(BlackJack)

def salir(BlackJack):
    BlackJack.exit()
    print(BlackJack)

cartas=x

opc=' '
while x<=21:
    for i in range(22):
        print('\n\nDesea agregar una carta?:', \
              '\n1.repartir\n 2.Si \n 3.No')
if opc=='1':
    repartir(BlackJack)
elif opc=='2':
    suma(BlackJack)
elif opc=='3':
    salir(BlackJack)
        

if __name__=="__main__":
    BlackJack()