

def impar(n):
    # if n == 0:
    #     return 1
    # else:
    #     num = (2*n+1)+impar(n-1)

    if n >0:
        num = (2*n+1)+impar(n-1)
        return num
    else:
        return 1


def main():
    num = int(input("ingrese un numero: "))
    resultado = impar(num)
    print(f"el resultado es: {resultado}")




if __name__ == "__main__":
    main()