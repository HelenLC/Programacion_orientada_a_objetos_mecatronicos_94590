class Ciudadano:
    def __init__(self, nombre, edad, cedula):
        self.__nombre = nombre
        self.__edad = edad
        self.__cedula = cedula

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero.")

    def setcedula(self, cedula):
        if len(cedula) >= 8 and len(cedula) <= 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos.")

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_cedula(self):
        return self.__cedula


    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False
def main():
        mostrar=[]
        usuario=Ciudadano
        usuario.setnombre(input('Ingrese su nombre:'))
        usuario.setedad(int(input('Ingrese su edad: ')))
        usuario.setcedula(int(input('Ingrese su cedula')))
        mostrar.appende(usuario)
        print(f"Nombre: {usuario.__nombre} - Edad: {usuario.__edad} - CC: {usuario.__cedula}")
    
if __name__=='__main__':
    main()
