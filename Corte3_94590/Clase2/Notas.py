class Estudiantes():
    def __init__(self, nombre:str, codigo:int, carrera:str, materia: str, notas: float):     #Método Constructor
        self.__nombre=nombre
        self.__codigo=codigo
        self.__carrera=carrera
        self.__materia=materia
        self.__notas=notas

    #---------- Setters ------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setCodigo(self,codigo:int):
        self.__codigo=codigo
    def setCarrera(self,carrera:str):
        self.__carrera=carrera
    def setMateria(self,materia:str):
        self.__materia=materia
    def setNotas(self,notas:float):
        self.__notas=notas
    
    #---------- Getters ------------
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getCarrera(self):
        return self.__carrera
    def getMateria(self):
        return self.__materia
    def getNotas(self):
        return self.__notas
    

#--------------Metodo---------------
def __promedio(self):
    n=self.getnotas()
    return round(sum(n)/len(n),2)

def getpromedio(self):
    average=self.__promedio()
    if average<3:
        return f'El estudiante {self.getnombre()} '

def main():
    while 1:
        nota=[]
        nombre=input('Nombre: ')
        codigo=input('Codigo: ')
        materia=input('Materia: ')
        carrera=input('Carrera: ')
        numero_notas=input('Cantidad de notas: ')
        for i in range(int(numero_notas)):
            nota.append(input(f'Nota {i+1}: '))

        usuario=Estudiantes(nombre,codigo,carrera,materia,nota)
        universidad.append(usuario)




    usuario=Estudiantes
    usuario.setNombre('Mariana')
    usuario.setCodigo(115478536)
    usuario.setMateria('Porgramación')
    usuario.setCarrera('Ingenieria')
    usuario.setNotas(2.5)

    print(f'Nombre: {usuario.getNombre()}' f'Codigo: {usuario.getCodigo()}' f'Materia: {usuario.getMateria()} \n'\
           f'Carrera: {usuario.getCarrera}'  f'Notas: {usuario.getNotas()}')

if __name__=="__main__":
    main()