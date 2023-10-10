def main(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo = main(lista[1:])
        if lista[0] > maximo:
            return lista[0]
        else:
            return maximo
lista = [80, 105, 8, 120, 50]
mayor = main(lista)
print("El mayor elemento de la lista es:", mayor)

if __name__=='__main__':
    main=[]