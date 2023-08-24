def menu():
    print('Serie de Fibbonacci: ')
    while True:
        opc=int(input(menu()))
        if opc==3:
            n=int(input('Ingrese un numero: '))
            a,b=0,1
            print(a,' ',b)
            for i in range(n-2):
                c=a+b
                a = b
                b = c
                print(c)