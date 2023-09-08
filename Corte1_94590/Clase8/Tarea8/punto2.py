def dicc():
    meses={
    'enero': 31,
    'febrero': 28, 
    'marzo': 31,
    'abril': 30,
    'mayo': 31,
    'junio': 30,
    'julio': 31,
    'agosto': 31,
    'septiembre': 30,
    'octubre': 31,
    'noviembre': 30,
    'diciembre': 31
}
    festivos= {
        'enero': ['Año Nuevo', 'Dia de los Reyes magicos'], 
        'marzo': ['Dia de san Jose'],
        'abril': ['Domingo de Ramos', 'Jueves Santo', 'Viernes Santo', 'Domingo de resurreccion'],
        'mayo': ['Dia de trabajo', 'Dia de la Ascension'],
        'junio': ['Corpus Christi','Sagrado Corazón'],
        'agosto':['Batalla de Boyaca', 'La asuncion de la virgen'],
        'octubre':['Dia de la raza'],
        'noviembre': ['Todos los santos','Independencia de Cartagena'],
        'diciembre': [' Día de la Inmaculada Concepción','Día de Navidad']
}
    usuario=input('Ingrese el mes que desea conocer: ')
    if usuario in meses:
        dias_meses=meses[usuario]
        dias_festivos=festivos.get[usuario]
        print(f'{meses} tiene {dias_meses}')
    elif dias_festivos:
        print(f'{meses} tiene {festivos}')
    else:
        print('El mes agregado no coincide')


if __name__=='__main__':
    dicc()