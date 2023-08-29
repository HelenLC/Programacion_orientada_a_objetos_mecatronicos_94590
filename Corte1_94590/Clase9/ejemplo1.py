def agregar(milista):
    num=int(input('Que numero desea agregar: '))
    milista.append(num)
    print(milista)

def insertar(milista):
    var=int(input('Que numero desea agregar: '))
    idx=int(input('Que posicion desea agregar: '))
    milista.insert(idx,var)
    print(milista)

def borrar(milista):
    milista.clear()
    print(milista)
    
def remover(milista):
    print(milista)
    var=int(input('Que numero desea remover: '))
    milista.remove(var)
    print(milista)

def main():
    milista=[2,4,7,8]
    opc=' '
    while opc!='exit':
        print('\n\nSelecione una de las siguientes opciones:', \
              '\n1. Agregar\n 2.Insertar \n 3.Borrar: \n 4.Remover')
        opc=input('=>')

        if opc=='1':
            agregar(milista)
        elif opc=='2':
            insertar(milista)
        elif opc=='3':
            borrar(milista)
        elif opc=='4':
            remover(milista)

if __name__=='__main__':
    main()