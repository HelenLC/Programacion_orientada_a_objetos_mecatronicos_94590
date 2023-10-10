# Leemos el archivo CSV
def leer_archivo():
    with open('wcm.csv', 'r', encoding='utf-8') as f:
        lineas = f.readlines()[1:]
    return lineas

# Función para buscar partidos entre dos equipos y obtener el historial
def buscadorpartidos(equipo1, equipo2, lineas):
    contador = 0
    victorias_equipo1 = 0
    victorias_equipo2 = 0
    empates = 0
    partidos = []

    for linea in lineas:
        campos = linea.split(',')
        home_team = campos[0]
        away_team = campos[1]
        home_score = int(campos[2])
        away_score = int(campos[4])
        round_info = campos[12]
        year = campos[-1].strip()
        host_country = campos[-2]

        if equipo1 in home_team and equipo2 in away_team:
            contador += 1
            if home_score > away_score:
                victorias_equipo1 += 1
                resultado = f"{home_team} {home_score} vs {away_score} {away_team} - Ronda: {round_info} - {host_country} - {year}"
                partidos.append(resultado)
            elif home_score < away_score:
                victorias_equipo2 += 1
                resultado = f"{away_team} {away_score} vs {home_score} {home_team} - Ronda: {round_info} - {host_country} - {year}"
                partidos.append(resultado)
            else:
                empates += 1
        elif equipo1 in away_team and equipo2 in home_team:
            contador += 1
            if away_score > home_score:
                victorias_equipo1 += 1
                resultado = f"{away_team} {away_score} vs {home_score} {home_team} - Ronda: {round_info} - {host_country} - {year}"
                partidos.append(resultado)
            elif away_score < home_score:
                victorias_equipo2 += 1
                resultado = f"{home_team} {home_score} vs {away_score} {away_team} - Ronda: {round_info} - {host_country} - {year}"
                partidos.append(resultado)
            else:
                empates += 1

    return contador, victorias_equipo1, victorias_equipo2, empates, partidos

def mayoresgoleadasglobal(lineas, cant_partidos):
    # Crear una lista para almacenar las mayores goleadas
    mayores_goleadas = []

    # Iterar a través de las líneas y calcular las diferencias de goles
    for linea in lineas:
        campos = linea.split(',')
        home_team = campos[0]
        away_team = campos[1]
        home_score = int(campos[2])
        away_score = int(campos[4])
        year = campos[-1].strip()

        diferencia_goles = abs(home_score - away_score)

        # Agregar la información del partido a la lista de mayores goleadas
        mayores_goleadas.append({
            'Equipos': f"{home_team} vs {away_team}",
            'Marcador': f"{home_score} - {away_score}",
            'Año': year,
            'Diferencia de Goles': diferencia_goles
        })

    # Ordenar la lista de mayores goleadas por diferencia de goles de manera descendente
    mayores_goleadas.sort(key=lambda x: x['Diferencia de Goles'], reverse=True)

    # Mostrar las N mayores goleadas según la cantidad de partidos que el usuario desee
    print(f"Las {cant_partidos} mayores goleadas globales son:")
    for i, partido in enumerate(mayores_goleadas[:cant_partidos], start=1):
        print(f"{i}. Equipos: {partido['Equipos']}, Marcador: {partido['Marcador']}, Año: {partido['Año']}")

def mayoresgoleadasmundial(lineas, cant_partidos, buscar_mundial):
    # Crear una lista para almacenar las mayores goleadas por mundial
    mayores_goleadas_mundial = []

    # Iterar a través de las líneas y calcular las diferencias de goles
    for linea in lineas:
        campos = linea.split(',')
        home_team = campos[0]
        away_team = campos[1]
        home_score = int(campos[2])
        away_score = int(campos[4])
        year = campos[-1].strip()

        if year == buscar_mundial:
            diferencia_goles = abs(home_score - away_score)

            # Agregar la información del partido a la lista de mayores goleadas por mundial
            mayores_goleadas_mundial.append({
                'Equipos': f"{home_team} vs {away_team}",
                'Marcador': f"{home_score} - {away_score}",
                'Año': year,
                'Diferencia de Goles': diferencia_goles
            })

    # Ordenar la lista de mayores goleadas por diferencia de goles de manera descendente
    mayores_goleadas_mundial.sort(key=lambda x: x['Diferencia de Goles'], reverse=True)

    # Mostrar las N mayores goleadas del mundial específico
    print(f"Las {cant_partidos} mayores goleadas del Mundial {buscar_mundial} son:\n")
    for i, partido in enumerate(mayores_goleadas_mundial[:cant_partidos], start=1):
        print(f"{i}. Equipos: {partido['Equipos']}, Marcador: {partido['Marcador']}, Año: {partido['Año']}\n")
    






# Modificamos la función menu para imprimir el historial y detalles de partidos en el formato deseado
def menu():
    while True:
        print("\n Bienvenido al sistema de consulta de partidos de la Copa Mundial de Fútbol")
        print("1. Buscar cuántas veces se han enfrentado 2 equipos en los mundiales")
        print("2. Buscar cuáles fueron las mayores goleadas de los mundiales")
        print("3. Salir")
        op = input("Elija una opción: ")

        if op == "1":
            equipo1 = input("Ingrese el nombre del primer equipo: ")
            equipo2 = input("Ingrese el nombre del segundo equipo: ")
            lineas = leer_archivo()
            total_partidos, victorias1, victorias2, empates, partidos = buscadorpartidos(equipo1, equipo2, lineas)

            print(f"Historial: ({equipo1}) - ({equipo2}) jugaron {total_partidos} partidos")
            print(f"{equipo1} = {victorias1} victorias, {empates} empates, {total_partidos - victorias1 - empates} derrotas")
            print(f"{equipo2} = {victorias2} victorias, {empates} empates, {total_partidos - victorias2 - empates} derrotas\n")

            for partido in partidos:
                print(partido)

        elif op == "2":
            cant_partidos = int(input("Cuantos partidos por mundial desea mostrar (max. 10): "))
            if cant_partidos > 10:
                print("La cantidad de partidos por mundial no puede ser mayor a 10")
                continue
            if cant_partidos < 1:
                print("La cantidad de partidos por mundial no puede ser menor a 1")
                continue
            else:
                print("a. Ver la lista completa mayores goleadas en mundiales")
                print("b. Búsqueda por mundial")
                op1 = input("Elija una opción: ")
                if op1 == "a":
                    print("Lista completa mayores goleadas en mundiales")
                    lineas = leer_archivo()
                    mayoresgoleadasglobal(lineas, cant_partidos)
                    
                elif op1 == "b":
                    buscar_mundial = input("Ingrese el año del mundial: ")
                    print("Búsqueda por mundial")
                    lineas = leer_archivo()
                    mayoresgoleadasmundial(lineas, cant_partidos, buscar_mundial)
                
        elif op == "3":
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__=='__main__':
    menu()
