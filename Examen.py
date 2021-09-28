from math import sqrt

#1942636
#Juan Carlos Valdez Flores
#Examen Medio Curso

def CalculoMedia(datos):
    adicion = 0

    for dato in datos:
        adicion += dato

    return adicion / len(datos)

def DesviacionEstandar(datos,media):
    adicion = 0
    for dato in datos:
        adicion += (dato - media)**2

    fraccion = adicion / (len(datos)-1)

    return sqrt(fraccion)


if __name__ == "__main__":
    numeros = [186,699,132,272,291,331,199,1890,788,1601]

    media = CalculoMedia(numeros)

    dE = DesviacionEstandar(numeros,media)

    print('La desviacion estadar es: {} y la media es de: {} '.format(dE,media))
