#;=?Diferenciar lo mismo de dos lineas en una sola linea
#str= convertir un entero a texto"
#def=funcion / nombre de la funcion 

n=int(input('Ingrese la cantidad de numero solicitados:'))
x=1;num=2
numero='1 '
while x<n:
    for i in range(2,num+1):
        primo=num%i
        if (primo==0 and num==i):
            numero+=str(f'{num} ')
            num+=1
            x+=1
        elif (primo==0 and num!=1):
            num+=1
            break
print(numero)
