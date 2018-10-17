#Zabdiel Valentin G.V
#Ciclos while. Mision 07.

def dividir(dividendo,divisor):#Funcion que simula una division con while
    cociente=[]# Se crea una lista
    if dividendo<divisor: #Si el dividendo no puede ser dividido entonces es 0
        print("Cociente: 0")
    else:                 #Si el dividendo puede ser dividido se ejecuta
        while dividendo>=divisor:    #Se crea un siclo while que restara el dividendo del divisor
            dividendo=dividendo-divisor
            cociente.append(1)         #por cada ver que se reste el divisor se guarda un valor
        print("Cociente: ",len(cociente))#Se imprime cuantas veces se resto
    print("Residuo: ",dividendo)          #Se imprime cuanto sobro

def probadivisiones():
    print("15/6 =")
    dividir(15,6)
    print("4/6 =")
    dividir(4,6)
    print("500/21 =")
    dividir(500,21)
    print("151/32 =")
    dividir(151,32)
    print("1024/8 =")
    dividir(1024,8)



def encontrarMayor():
    datos=[]
    print("Teclea una serie de numeros para encontrar el mayor.")
    numero=int(input("Teclea tus numeros [-1 termina]: "))

    while numero != -1 and numero>=0:
        #procesan
        datos.append(numero)
        numero=int(input("Teclea tus numeros [-1 termina]: "))

    if len(datos)>0:
        print("El mayor es: ", max(datos))

    else:
        print("No hay datos o los numeros son negativos")

def leerOpcionMenu():
    print("Misión 07. Ciclos while.")
    print("Autor: Zabdiel Valentín Garduño Vivanco.")
    print("1. Calcular divisiones.")
    print("2. Encotrar mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion

def main():
    opcion= leerOpcionMenu()
    while opcion!=3:
        if opcion==1:
            print("")#Se imprime un espacio
            dividendo=int(input("Teclea el dividendo: "))
            divisor=int(input("Teclea el divisor: "))
            dividir(dividendo,divisor)
            print("")#Se imprime un espacio.
        elif opcion==2:
            print("")#Se imprime un espacio
            encontrarMayor()
            print("")
        elif opcion==3:
            print("")#Se imprime un espacio
        elif opcion>3 or opcion<1:
            print("")#Se imprime un espacio
            print("ERROR: teclea 1, 2 o 3")
            print("")#Se imprime un espacio
        opcion=leerOpcionMenu()
    print("Gracias por usar este programa, regresa pronto.")




main()

