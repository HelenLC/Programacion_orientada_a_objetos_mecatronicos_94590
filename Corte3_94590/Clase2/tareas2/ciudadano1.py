class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre


    def setEdad(self, edad:int):
        self.edad = edad


    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def informacion(self):
        print(f"Nombre: {self.nombre} es profesional en su profesion")

class Profesor(Ciudadano):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
    def dame_info(self):
        return f"{self.nombre} es un profesor de {self.asignatura}"
class Medico(Ciudadano):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def atender_paciente(self):
        return f"{self.nombre} está atendiendo a un paciente"

class Ingeniero(Ciudadano):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
    def investigar(self):
        return f"{self.nombre} está investigando en {self.especialidad}"

    def investigar(self, tema):
        return f"{self.nombre} está investigando {tema} en {self.especialidad}"
    
            
def main():
    pro = Profesor("Juan", 35, "Matemáticas")
    print(pro.dame_info())
    
    med = Medico("María", 40, "Cardiología")
    print(med.atender_paciente())
    
    ing = Ingeniero("Pedro", 30, "Informática")
    print(ing.investigar("Virus"))


if __name__ == "__main__":
    main()