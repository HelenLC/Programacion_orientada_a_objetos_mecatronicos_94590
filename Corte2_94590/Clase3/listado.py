

def inscripcion():
    estuciantes = {}
    datos = {}
    while 1:
        opc = ("desea inscribir un estudiante (y/n): ")
    
        if opc == "y":
            nombre = input("nombre: ")
            edad = input("edad: ")
            codigo = input("codigo: ")
            genero = input("genero: ")
            datos["edad"]=edad
            datos["codigo"]=codigo
            datos["genero"]=genero
            estudiantes[nombre]
            datos={}
            print(estudiantes)
        elif opc == "n":
            for key, value in estuciantes.items():
                print(f"estudiante:{key},edad:{value}")
             break
        else:
             print("ingrese una opcion valida")

def main():
    inscripcion()





if __name__=="__main__":
    main()