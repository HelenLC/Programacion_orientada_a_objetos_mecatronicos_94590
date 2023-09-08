import random

def programa():
    num_aleatorio=[]
    for i in range(15):
        numero=int(input('Agrega un valor: '))
        num_aleatorio.append(numero)
        num_aleatorio.sort()
        print("Números aleatorios ordenados de menor a mayor:")
        print(num_aleatorio)
        if numero=='exit':
            break

if __name__=='__main__':
    programa()