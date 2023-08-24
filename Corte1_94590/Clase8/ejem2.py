import ejem2_2 as f
def ejem2():
    n=int(input('Ingrese un valor: '))
    m=int(input('Ingrese un valor: '))
    cmb=(f(n)/(f(m)*f(n-m)))
    print(f'El número de combinaciones posibles es: {cmb} ')

if __name__=='__main__':
    ejem2()