def main_read():
    f=open('Alimentos.txt', 'rt')
    producto=f.read().split("\n")#split es dividir
    f.close
    print(producto)
    print(len(producto))
    elemento=[]
    for i in producto:
        elemento.append(i.split(","))
    print(elemento)
    print(elemento[1][1])

def calcular_valorbruto(producto, valorneto):
    IVA = {open('Alimentos.txt','rt')}
   
    if producto in IVA:
        valorbase = valorneto / (1 + IVA[producto])
        valor_IVA = valorneto - valorbase

        return valorbase, valor_IVA
    else:
        return None

while True:
    producto = input("Ingrese el nombre del producto o 'salir' para terminar: ")
    
    if producto.lower() == "salir":
        break

    valorneto = float(input("Ingrese el valor neto del producto: "))

    resultado = calcular_valorbruto(producto, valorneto)

    if resultado:
        valorbase, valor_IVA = resultado
        print("Valor base del producto:", valorbase)
        print("Valor del IVA:", valor_IVA)
    else:
        print("El producto ingresado no está en la lista de productos con IVA.")


if __name__=='__main__':
    main_read()
    calcular_valorbruto(producto, valorneto)
    #main_producto()