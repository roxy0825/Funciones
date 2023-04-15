
def Greet():
    print("Hola como estas, espero te diviertas con python")

def GreetName(nombre):
    print("Hola como estas ", nombre, "bienvenido al curso de python")


def Suma():
    nro1= int(input("Nro 1"))
    nro2= int(input("Nro 2"))
    suma = nro1 + nro2
    print(f"{nro1} + {nro2} = {suma}")

def SumaDos(nro1,nro2):
    suma = nro1 + nro2
    print(f"{nro1} + {nro2} = {suma}")

def SumaTres(nro1, nro2 = 55):
        suma = nro1 + nro2
        print(f"{nro1} + {nro2} = {suma}")

def calcularNotas(nota1, nota2, nota3):
    Definitiva=(nota1+nota2+nota3)/3
    return Definitiva


def Observacion(notaFinal):
    if notaFinal > 3:
        print("Felicitaciones aprobaste materia")
    else:
        print("No aprueba materias")
#----------------------------------------------
def Masa():
    peso=int(input("peso: "))
    altura = int(input("altura: "))
    calcular=(peso / altura)*2
    print(f"{peso} + {altura} = {calcular}")

def Subtotal(precio, cantidad):
    sub=(cantidad * precio)
    return sub


def descuento(cantidad):
    if cantidad > 10:
        print("se le hace descuento del 7%")
    else:
        print("no tiene descuento")


if __name__=="__main__":
    Subtotal()
    descuento()



   # notaFinal=calcularNotas(3,4,5)
    #print("Nota definitiva", notaFinal)
    #Observacion(notaFinal)


    #esta es calcular nota final
   # notaFinal=calcularNotas(3,4,5)
    #print("Nota definitiva", notaFinal)



    #SumaTres(1)
    #SumaTres(1,129) #reemplaza al que esta por defecto


    #SumaDos(147,147)
    #SumaDos(2,2)
    #Funcion con parametro o argumento por defecto, es opcional enviar datos


   #Suma()

   # GreetName("Juliana")
   # GreetName("Pedro")
    #GreetName("Rosita")
   # nombre=input("Digite nombre")
   # GreetName(nombre)

    #print("Iniciando con las funciones de python")
    #Greet()
