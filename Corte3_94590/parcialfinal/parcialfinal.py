#---------Clase padre-----------
class ConversorNumerico:
    def __init__(self, numero:int):
        self.numero=numero
    def setNumero(self, numero):
        self.setNumero=numero
    def getNumero(self):
        return self.getNumero
    


#---------subclase Deciaml-------------------------

class Decimal(ConversorNumerico):
    def __init__(self, numero: int, converdec_bin:int, converdec_hexa:int):
        super().__init__(numero)
        self.converdec_bin=converdec_bin
        self.converdec_hexa=converdec_hexa

#---------setters-----------

    def setConverdec_bin(self, converdec_bin):
        self.Converdec_bin=converdec_bin

    def setConverdec_hexa(self, converdec_hexa):
        self.Converdec_bin=converdec_hexa

#---------getters-----------

    def getConverdec_bin(self):
        return self.Converdec_bin 
    
    def getConverdec_hexa(self):
        return self.converdec_hexa
    
#---------Conversion-------------------------

    def Conversiondec_bin(self, numero:int ):
        dec_bin=[]
        while numero > 0:
            residuo=numero%2
            if residuo==1 or residuo==0:
                residuo.append(dec_bin)
        dec_bin.reverse()
        resultado=str(dec_bin).split(",").strip("[]","") 
        print(resultado)
        return self.converdec_bin

#---------subclase Binario----------------------
class Binario(ConversorNumerico):
    def __init__(self, numero: int, converbin_dec:int):
        super().__init__(numero)
        self.converbin_dec=converbin_dec

#---------setters-----------
    def setConverbin_dec(self, converbin_dec):
        self.Converbin_dec=converbin_dec

#---------getters-----------
    def getConverbin_dec (self):
        return self.Converbin_dec 
    
#---------Conversion-------------------------6
def Conversionbin_dec(self, numero:int ):
        dec_bin=[]
        while numero > 0:
            residuo=numero%16
            if residuo==1 or residuo==0:
                residuo.append(dec_bin)
        dec_bin.reverse()
        resultado=str(dec_bin).split(",").strip("[]","") 
        print(resultado)
        return self.converdec_bin
    

#---------subclase Hexadecimal-------------------
class Hexadecimal(ConversorNumerico):
    def __init__(self, numero: int, converhexa_dec:int):
        super().__init__(numero)
        self.converhexa_dec=converhexa_dec

#---------setters-----------
    def setConverhexa_dec(self, converhexa_dec):
        self.Converhexa_dec=converhexa_dec

#---------getters-----------
    def getConverhexa_dec(self):
        return self.Converhexa_dec
    
def main():
    while True:
        conversor=ConversorNumerico()
        print("\n------------------Conversor numerio----------------------\n")
        print("1. Convercion Decimal a Binario")
        print("2. Conversion Decimal a Hexadecimal")
        print("3. Conversion de Binario a Decimal")
        print("4. Conversion de Hexadecimal a Decimal")
        print("5. Salir")

        opcion = input("Ingrese el número de la conversion de desea realizar: ") 
       
        if opcion == "1":
            decimal=Decimal()
            n=input('Ingrese un numero: ')
            decimal.Conversiondec_bin(n)
            print(f'El numero decimal {ConversorNumerico.getNumero()} es: {Decimal.getConverdec_bin}')
            
        elif opcion == "2":
            decimal=Decimal()
            n=input('Ingrese un numero: ')
            decimal.converdec_hexa(n)
            print(f'El numero decimal {ConversorNumerico.getNumero()} es: {Decimal.getConverdec_hexa}')

        elif opcion == "3":
            binario=Binario()
            n=input('Ingrese un numero: ')
            binario.Converbin_dec(n)
            print(f'El numero decimal {ConversorNumerico.getNumero()} es: {Binario.getConverbin_dec}')
            
        elif opcion == "4":
            hexadecimal=Hexadecimal()
            n=input('Ingrese un numero: ')
            hexadecimal.Converhexa_dec(n)
            print(f'El numero decimal {ConversorNumerico.getNumero()} es: {Hexadecimal.getConverhexa_dec}')
        else:
            print(f'Error, opcion invalida')





if __name__=='__main__':
    main()
    

