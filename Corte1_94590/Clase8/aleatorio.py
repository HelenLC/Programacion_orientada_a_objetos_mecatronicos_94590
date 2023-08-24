
#capsular=tomar partes de codigo dentro de un codigo
import random as r

def app():
    pal=' '
    nombre='Que ponemos'
    while pal !='exit':
        #x=r.randint(100,180)
       # x=r.uniform(100,180)
        x=r.choice(nombre)
        print(x)
        pal=input('Para salir escriba exit---> ')

if __name__=='__main__':
    app()
