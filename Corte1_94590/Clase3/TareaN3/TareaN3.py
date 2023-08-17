#Ejercicio N1

x=input('Ingrese una letra del abecedario:')
vocal='a,e,i,o,u'
consonante='b,c,d,f,g,h,j,k,l,m,n,ñ,p,q,r,s,t,v,w,x,y,z'
print('La letra ingresada es consonante',consonante)
print('La letra ingresada es vocal', vocal)

#Ejercicio N2

x=int(input('Ingrese valor del producto:'))
v=x*0.19
print('Su producto vale:',v)

#Ejercicio N3

lado1 = float(input("ingrese el primer lado: "))
lado2 = float(input("ingrese el segundo lado: "))
lado3 = float(input("ingrese el tercer lado: "))

if lado1 == lado2 and lado1 == lado3:
    print(" el triangulo es equilátero")
elif lado1 == lado2 or lado1 == l3 or lado2 == lado3:
    print("el triangulo es isoseles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("el triangulo es escaleno")