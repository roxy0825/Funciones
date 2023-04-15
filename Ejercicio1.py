




def productos():
    Prod=int(input("Nombre de producto: "))
    Cant=int(input("ingrese cantidad: "))
    prec=int(input("ingrese precio producto: "))
    subtotal= Cant + prec
    print(f"{Prod} +{subtotal} " )

if __name__=="__main__":
    productos()