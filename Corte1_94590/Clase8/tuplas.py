#*=forma de escritura
#radint=numeros enteros
#uniform=flotantes
#shoice=caracteres
def app(a,*args,**wargs):
    print(args)
    print(wargs)

if __name__=='__main__':
    app(1,2,5,7,9,m=1,b=2)
