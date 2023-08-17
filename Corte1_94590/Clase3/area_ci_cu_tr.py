print('figuras validad:  \n',
      '1. calcula el area de un circulo \n',\
      '2. calcula el  area de un rectangulo/cuadrado \n',\
      '3. calcula el area de un triangulo')
fig=input('Ingrese una figura para calcular su area:')
A='NAN'
if (fig=='circulo'):
    r=int(input('ingrese el valor del radio:'))
    A=3.1416*r**2
elif(fig=='rectangulo'):
    b=int(input('ingrese el valor de la base:'))
    h=int(input('ingrese el valor de la altura:'))
    A=b*h
elif(fig=='triangulo'):
    b=int(input('ingrese el valor de la base:'))
    h=int(input('ingrese el valor de la altura:'))
    A=b*h/2
else:
    print('Ingreso una opcion invalida')
print('el valor del area es', A)