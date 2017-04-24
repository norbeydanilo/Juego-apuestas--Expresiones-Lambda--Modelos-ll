from functools import reduce

def funcionJuego(matriz):

    #Filtro de los valores numericos. [[numeros apuesta1], [numeros apuesta2], ...]
    apuestas = [filter(lambda i: i != True and i != False, i) for i in matriz]

    #Filtro de los valores booleanos. [[boolean apuesta1], [boolean apuesta2], ...]
    apuestasBoolean = [filter(lambda i: i == True or i == False, i) for i in matriz]

    #Reduce para el calculo del promedio del jugador. [acumulacion de valores1, ...]
    promedioJugador = [reduce(lambda x,y: x + y, i)/len(i) for i in apuestas]

    #Reduce para el calculo del promedio del total de jugadores.[promedio]
    promedioApuestas = [reduce(lambda x,y: x + y, promedioJugador)/len(promedioJugador)]

    #Map para mostrar el valor acertado de cada apuesta de acuerdo al bool. [valor, 0, 0, ...]
    aciertos = map(lambda u,v: map(lambda m,n: m if (n) else 0, u, v), apuestas, apuestasBoolean)

    #Reduce para acumular el valor de las apuestas ganadas. 
    gananciasJugador = [reduce(lambda x,y: x + y, i) for i in aciertos]
    mayorGanancia = [max(gananciasJugador)]
    menorGanancia = [min(gananciasJugador)]
    
    #Map para mostrar el valor fallado de cada apuesta de acuerdo al bool. [valor, 0, 0, ...]
    fallos = map(lambda u,v: map(lambda m,n: m if (not n) else 0, u, v), apuestas, apuestasBoolean)

    #Reduce para acumular el valor de las apuestas perdidas.
    perdidasJugador = [reduce(lambda x,y: x + y, i) for i in fallos]
    mayorPerdida = [max(perdidasJugador)]
    menorPerdida = [min(perdidasJugador)]

    print "Juego de apuestas:", matriz
    print "----------------------------------------------------------------------------"
    print(">>Ganancias de cada jugador:")
    print(gananciasJugador)
    print(">>Perdidas de cada jugador:")
    print(perdidasJugador)
    print(">>Promedio de lo apostado por cada jugador:")
    print(promedioJugador)
    print(">>Promedio total apostado:")
    print(promedioApuestas)
    print(">>El que mas gano:")
    print(mayorGanancia)
    print(">>El que mas perdio:")
    print(mayorPerdida)
    print(">>El que menos gano:")
    print(menorGanancia)
    print(">>El que menos perdio:")
    print(menorPerdida)

matriz = [[100, 150, 500, 600, 250, True, False, True, False, True], [300, 600, 300, 610, 1000, False, True, False, True, False], [120, 650, 700, 1000, 890, True, False, True, True, True]]
funcionJuego(matriz)
