def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

def encontrar_numeros_perfectos(cantidad):
    numeros_perfectos = []
    numero = 1
    while len(numeros_perfectos) < cantidad:
        if es_numero_perfecto(numero):
            numeros_perfectos.append(numero)
        numero += 1
    return numeros_perfectos

cantidad = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))

if cantidad <= 0 or cantidad > 10:
    print("La cantidad ingresada no es válida. Debe estar entre 1 y 10.")
else:
    numeros_perfectos = encontrar_numeros_perfectos(cantidad)
    print(f"Los {cantidad} primeros números perfectos son:")
    for numero_perfecto in numeros_perfectos:
        print(numero_perfecto)