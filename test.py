from random import randint


baraja = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
finalJuego = False
puntosJugador = 0
puntosIA =  0

print("Siete y medio")
while (finalJuego == False):
    print("Juegas")
    puntosSacados = randint(0,36)
    print("Has sacado un "+str(baraja[puntosSacados]))
    puntosJugador = puntosJugador + baraja[puntosSacados]
    print("Tienes "+str(puntosJugador) +" puntos ")

    print("Le toca a la IA")
    puntosSacados = randint(0,36)
    print("La IA ha sacado un "+str(baraja[puntosSacados]))
    puntosIA = puntosIA + baraja[puntosSacados]
    print("La IA tiene "+str(puntosIA)+" puntos")
    
    if (puntosJugador >= 7.5 or puntosIA >= 7.5):
        print("Fin del juego")
        finalJuego = True
        break
    
print("Gracias por jugar")