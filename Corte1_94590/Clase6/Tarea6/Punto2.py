def menu():
    print('Sucesion de sumas: ')
    while True:
        opc=int(input(menu()))
        if opc==2:
            n1=int(input('Ingrese el primer numero: '))
            n2=int(input('Ingrese el segundo numero: '))
            p=0
            for i in range(abs(n1)):
                p=p+n2
        if n1<0:
            p=-p
            print('el producto es: ',p)
