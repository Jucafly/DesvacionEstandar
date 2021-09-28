from math import sqrt

#1942636
#Juan Carlos Valdez Flores
#Examen Medio Curso

#Media
def CalculoMedia(datos):
    adicion = 0

    for dato in datos:
        adicion += dato

    return adicion / len(datos)

#Desviacion Estandar
def DesviacionEstandar(datos,media):
    adicion = 0
    for dato in datos:
        adicion += (dato - media)**2

    fraccion = adicion / (len(datos)-1)

    return sqrt(fraccion)

#Aqui Empieza el Codigo
if __name__ == "__main__":
    #numeros = [160,591,114,229,230,270,128,1657,624,1503]
    numeros = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    media = CalculoMedia(numeros)

    dE = DesviacionEstandar(numeros,media)

    print('La desviacion estadar es: {} y la media es de: {} '.format(dE,media))
