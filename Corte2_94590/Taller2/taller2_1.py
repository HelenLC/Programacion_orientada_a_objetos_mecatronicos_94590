def contar_enfrentamientos(equipo1, equipo2):
    contador = 0
    with open('mundiales.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.split(',')
            if equipo1 in datos and equipo2 in datos:
                contador += 1
    return contador

equipo1 = 'Argentina'
equipo2 = 'Brasil'
enfrentamientos = contar_enfrentamientos(equipo1, equipo2)
print(f"Los equipos {equipo1} y {equipo2} se han enfrentado {enfrentamientos} veces en la Copa Mundial de Fútbol Masculino.")