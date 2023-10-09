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


    #print(type(producto)) =tipo de documento

# # producto= {
#   #  CODIGO= f=open('Alimentos.txt', 'rt'), 
#    # DESCRIPCION= f=open('Alimentos.txt', 'rt'),
#     #TARIFA_IVA= 0.19
#     }
# CODIGO =producto["CÓDIGO"]
# DESCRIPCION =producto["DESCRIPCIÓN"]
# TARIFA_IVA =producto["TARIFA IVA"]

# print("CÓDIGO:", CODIGO)
# print("DESCRIPCIÓN:", DESCRIPCION)
# print("TARIFA IVA:", TARIFA_IVA)

# def main_producto():
#     f=open('Alimentos.txt', 'rt')
#     producto=f.readline().rstrip('\n').split(',')

# while True:
#     i=input('Ingrese un producto y su valor: ')
#     if i.lower() == "salir":
#         break
#     dato=i.split(',')
    

def main_valor(v_neto):
    f=open('Alimentos.txt', 'rt')
    v_iva=0.19
    v_base= v_neto/(1+v_iva)
    iva=v_neto-v_base
    return v_base, iva




if __name__=='__main__':
    main_read()
   #main_valor()
    #main_producto()