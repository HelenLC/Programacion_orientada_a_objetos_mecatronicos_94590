import math as m

a= int(input('ingrese un valor'))
b= int(input('ingrese un valor'))
c= int(input('ingrese un valor'))
x1=(-b+m.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-m.sqrt(b**2-4*a*c))/(2*a)
print('las soluciones son', x1, 'y', x2)

#sqrt= raiz
