class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCedula(self, cedula:int):
        if 8 <= len(cedula) <= 10:
            self.cedula = cedula
        else:
            print("El número de cedula debe tener entre 8 y 10 dígitos")

    def setEdad(self, edad:int):
        if edad > 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero")

    def getNombre(self):
        return self.nombre

    def getCedula(self):
        return self.cedula


    def getEdad(self):
        return self.edad

    def mostrar(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - CC: {self.cedula}")

    def MayorDeEdad(self):
        if self.edad >= 18:
            return f'{self.edad}Es mayor de edad'
        else:
            return f'{self.edad}Es menor de edad o de la tercera edad'
   
            
def main():
    mostrar = []
    ciudadano1 = Ciudadano("Helen Lopez", "1121706388", 19)
    mostrar.append(ciudadano1)

    print(f'Nombre:{ciudadano1.nombre}\n'
          f'Edad:{ciudadano1.edad}\n'
          f'Cedula{ciudadano1.cedula}')
    print(ciudadano1.MayorDeEdad())

if __name__ == "__main__":
    main()