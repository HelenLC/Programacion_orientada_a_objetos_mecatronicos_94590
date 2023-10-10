#realice un programa en donde permita  crear una lista de 10 números aleatorios entre 1 y 50 (todos numeros enteros)  despues cree tres funciones donde se reciba la lista como parametro para mayor, minimo y primos
from random import randint as r

def lista():
    for i in range(10):
        lista.append(r(1,50))
        print(lista)
    return lista

def num_maximo(lista):
    for numero in lista:
        if numero>num_maximo:
            num_maximo=numero(lista)
        return num_maximo
    
def num_minimo(lista):
    for numero in lista:
        if numero<num_minimo:
            num_minimo=numero(lista)
        return num_minimo
    
def num_primo(numero):
    if numero % 1 == numero:
        return True
    if numero % numero == 1:
        return True
    if numero % 2 == 0:
        return False
    
def primo(lista):
    primo = [numero for numero in lista if num_primo(numero)]
    return primo

print('El numero maximo es: ',[num_maximo])
print('El numero minimo es: ',[num_minimo])
print('El numero primo es: ',[primo])

if __name__=='__main__':
    lista=[]
    lista()