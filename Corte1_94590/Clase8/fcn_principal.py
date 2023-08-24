#main=forma en que el interprete/programador llama al archivo
#name= es el nombre de la funcion que queremos invocar 
#Tuplas son numeros

import fcn_ext

def main():
    a=int(input('Ingrese un numero: '))
    b=int(input('Ingrese un numero: '))
    r=fcn_ext.suma(a,b)  #esta invocando la suma que esta en la funcion externa
    print(r)
    print(f'Ejecutado desde{__name__}')


if __name__=="__main__":
    main() #inicia el programa
