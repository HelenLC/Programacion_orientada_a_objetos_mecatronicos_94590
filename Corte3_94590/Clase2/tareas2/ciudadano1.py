class Ciudadano():
    def __init__(self,nombre:str, edad:int, cc:int):
        self._nombre=nombre
        self._edad=edad
        self._cc=cc

    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_cc(self):
        return self._cc 
    
    def set_nombre(self, nombre:str):
        self._nombre=nombre 

    def set_edad(self, edad:int):
        self._edad=edad
    def set_cc(self, cc:int):
         self._cc=cc

    def _informacion(self):
        return print(f'nombre{self._nombre}, edad{self._edad}, cc{self._cc}')
    def legado(self):
        return 'Gracias por su aporte y/o conocimiento'
    
class Lingüista(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, especialidad:str,tiempo:int):
        super().__init__(nombre, edad, documento)
        self.__especialidad=especialidad
        self.__tiempo=tiempo
    def getEspecialidad(self):
        return self.__especialidad
    def getTiempo(self):
        return self.__tiempo
    def setNombre(self,especialidad:str):
        self.__especialidad=especialidad
    def setEdad(self,tiempo:int):
         self.__tiempo=tiempo
    def logro(self):
         return 'Muchas gracias Sr/Sra.Lingüista'
    
class Profesor(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, especialidad:str,tiempo:int):
        super().__init__(nombre, edad, documento)
        self.__especialidad=especialidad
        self.__tiempo=tiempo
    def getEspecialidad(self):
        return self.__especialidad
    def getTiempo(self):
        return self.__tiempo
    def setNombre(self,especialidad:str):
        self.__especialidad=especialidad
    def setEdad(self,tiempo:int):
         self.__tiempo=tiempo
    def logro(self):
         return 'Muchas gracias Sr/Sra.Profesor'
    
class Paleontólogo(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, especialidad:str,tiempo:int):
        super().__init__(nombre, edad, documento)
        self.__especialidad=especialidad
        self.__tiempo=tiempo
    def getEspecialidad(self):
        return self.__especialidad
    def getTiempo(self):
        return self.__tiempo
    def setNombre(self,especialidad:str):
        self.__especialidad=especialidad
    def setEdad(self,tiempo:int):
         self.__tiempo=tiempo
    def logro(self):
         return 'Muchas gracias Sr/Sra.	Paleontólogo'
        
def main():
    profecional=[]
    profecional1=Lingüista('Maria',42,1150487922,'Sintaxis',15)
    profecional2=Profesor('Eduardo',35,101525483,'profesor',10)
    profecional3=Paleontólogo('Asucena',60,1022287433,'Anatomía comparada',30)
    profecional.append(profecional1)
    profecional.append(profecional2)
    profecional.append(profecional3)

if __name__=='__main__':
    main()