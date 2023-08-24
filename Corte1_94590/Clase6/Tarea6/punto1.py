def menu():
    print('.Numeros divicibles: ')
    while True:
        opc=int(input(menu()))
        if opc ==1:
            n=int(input('Ingrese un numero: '))
        if n % 2==0:
            for i in range(1,n+1):
                if n % i ==0:
                    print('los numeos divisores son: ',i)
        else:
            print('Todos los numeros son divicibles entre 0')