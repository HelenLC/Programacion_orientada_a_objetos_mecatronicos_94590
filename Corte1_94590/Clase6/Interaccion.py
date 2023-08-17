#while=repetitivo en el codigo
#break= termina el bucle/ejecucion
#continue=omitir el numero que es igual a i
#pass= evitar errores en el codigo y completar parte del codigo

n=int(input('Ingrese un numero:'))
i=0

while i<n:
    i+=1
    if i==4:
        continue
    print(i)