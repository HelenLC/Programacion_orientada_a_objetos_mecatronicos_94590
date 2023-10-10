matriz = [[1] * 10 for _ in range(5)]
import random
def main():
    for i in range(5):
        for j in range(10):
            matriz[i][j] = random.randint(1, 100)

print("Matriz original:")
for fila in matriz:
    print(fila)

maximo = matriz[0][0]
numero_max = (0, 0)
for i in range(5):
    for j in range(10):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
            numero_max = (i, j)

minimo = matriz[0][0]
numero_min = (0, 0)
for i in range(5):
    for j in range(10):
        if matriz[i][j] < minimo:
            minimo = matriz[i][j]
            numero_min = (i, j)

print("El número más alto es", maximo, "en la posición", numero_max)
print("El número más bajo es", minimo, "en la posición", numero_min)

matriz_ordenada = sorted([num for fila in matriz for num in fila], reverse=True)
matriz_ordenada = [matriz_ordenada[i:i+10] for i in range(0, 50, 10)]

print("Matriz ordenada de mayor a menor:")
for fila in matriz_ordenada:
    print(fila)
if __name__=='__main__':
    main()