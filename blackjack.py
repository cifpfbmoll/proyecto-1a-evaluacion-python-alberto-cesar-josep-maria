import random
import os
os.system('cls')

wins = 0
loses = 0

mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# definiciones
def barajar(mazo):
    mano = []
    for i in range(2):
        random.shuffle(mazo)
        card = mazo.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        mano.append(card)
    return mano
##########################################################################
def total(mano):
    total = 0
    for card in mano:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total
##########################################################################
def pedir(mano):
    card = mazo.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    mano.append(card)
    mano.append(carta)
    return mano
##########################################################################
def blackjack(barajaJugador, barajaDealer):
    global wins
    global loses
    if total(barajaJugador) == 21:
        print_results(barajaJugador, barajaDealer)
        print ("Felicidades! Tienes un blackjack!")
        wins += 1
        playAgain()
    elif total(barajaDealer) == 21:
        print_results(barajaJugador, barajaDealer)
        print ("Lástima! El dealer tiene un blackjack.")
        loses += 1
        volverMenu()
##########################################################################
def VolverMenu():
    volver = input("Quieres volver al menú? (S/N) : ").lower()
    if volver == "s":
        barajaJugador = []
        barajaDealer = []
        mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        gestionarMenu()
    else:
        print("Adiós!")
        exit()
##########################################################################
def mostrarBaraja():
   print("Tu baraja es ", barajaJugador, "y la del dealer es", barajaDealer)
##########################################################################
def puntuacion():
    global wins
    global loses
    if total(barajaJugador) == 21:
        mostrarBaraja()
        print("Felicidades! Tienes un Blackjack!")
        wins += 1
    elif total(barajaJugador) > 21:
        mostrarBaraja()
        print("Lástima! Tienes más de 21.")
        loses += 1
    elif total(barajaDealer) == 21:
        mostrarBaraja()
        print("Lástima! El dealer tiene un Blackjack.")
        loses +=1
    elif total(barajaDealer) > 21:
        mostrarBaraja()
        print("Vaya! El dealer se ha pasado de 21, ganas!")
        wins += 1
    elif total(barajaJugador) > total(barajaDealer):
        mostrarBaraja()
        print("Felicidades! Tienes más que el dealer!")
        wins += 1
    elif total(barajaJugador) < total(barajaDealer):
        mostrarBaraja()
        print("Lástima! Te ha ganado el dealer.")
        loses += 1
##########################################################################
def juego():
    global wins
    global loses
    eleccion = 0
    barajaJugador = barajar(mazo)
    barajaDealer = barajar(mazo)
    print("El dealer muestra una de sus cartas, y es: ", str(barajaDealer(0)))
    print("Tienes las siguientes cartas: ", str(barajaJugador), ". Con un total de :", str(total(barajaJugador)))
    blackjack(barajaJugador, barajaDealer)
    quit = False
    while not quit:
        eleccion = input("Quieres Pedir[P], Plantarte[X] o Salir[S]?").lower()
        if eleccion == "p":
            pedir(barajaJugador)
            print(barajaJugador)
            print("El total de tu mano es: ", str(total(barajaJugador)))
            if total(barajaJugador) > 21:
                print("Te has pasado de 21!")
                loses += 1
                volverMenu()
        elif eleccion == "x":
            while total(barajaDealer) < 17:
                pedir(barajaDealer)
                print(barajaDealer)
                if total(dealer_hand)>21:
                    print('El dealer se ha pasado de 21! Has ganado!')
                    wins += 1
                    volverMenu()
            puntuacion(barajaJugador, barajaDealer)
            volverMenu()
        elif eleccion == "s":
            print("Adiós!")
            quit = True
            exit()
##########################################################################
def mostrarBlackjack(menu):
    if (menu == "J") or  (menu == "j"):
        print("Vamos a jugar a BlackJack!")
        juego()
##########################################################################
def mostrarInstrucciones(menu):
        print("Instrucciones BlackJack:")
        print("--> Objetivo: Llegar a 21 con la suma del valor de las cartas. ")
        print("1. El crupier reparte dos cartas visibles a cada jugador. \n\
   El valor de las cartas son: El As vale 11 o 1, las figuras valen 10 \
y las cartas númericas su valor natural. \n\
   Si al jugador le sale un As junto con una carta de valor 10, obtiene Blackjack.")
        print("2. Al terminar de repartir las dos cartas, el crupier pondrá \
luego su primer carta boca arriba, de manera que sea visible.")
        print("3. Cada jugador compite únicamente contra el crupier, siendo \
indiferente las cartas que tengan el resto de jugadores.")
        print("4. Cada jugador tiene la posibilidad de plantarse o de pedir \
más cartas hasta llegar a 21 puntos. Alcanzar 21 puntos con \n\
   más de una carta extra no se considera BlackJack, siendo por tanto esa jugada \
inferior al Blackjack con dos cartas.")
        print("5. Si al pedir una nueva carta se pasa de 21, pierde automáticamente \
la apuesta y sus cartas y la apuesta será retirada por el crupier.")
        print("6. Cuando todos los jugadores hayan pedido sus cartas, el crupier \
mostrará su segunda carta y sacará más cartas si fuera necesario \n\
   para sumar 17 o más puntos, momento en el que se plantará.")
        print("7. Entre el crupier y el jugador, gana finalmente quién obtenga \
BLACKJACJK (As + 10) o quién tenga la puntuación más alta sin pasarse \n\
   de 21, habiendo la posibilidad de empate.")
        menu = input("Quieres volver al menú? [S/N] ").lower()
        if menu == "s":
            gestionarMenu()
        else:
            print("Adiós!!!")
            exit()
##############################################################################
def mostrarCreadores(menu):
        print("Creadores de este BlackJack:")
        print("Este juego de BlackJack hecho en Python 3.9.0 ha sido creado por:\n\
--> César Andrés Granda, Alberto Serrano y Josep Maria Jiménez <--")
        menu = input("Quieres volver al menú? [S/N] ").lower()
        if menu == "s":
            gestionarMenu()
        else:
            print("Adiós!!!")
            exit()
##############################################################################
def mostrarSalir(menu):    
    if (menu == "S") or (menu == "s"):
        print("Adiós!!!")
        exit()

# menu
def gestionarMenu():
    print("---> Bienvenido al menú <---")
    print("")
    print("           WINS = ", wins, "LOSES = ", loses)
    print("--> Para jugar a BlackJack, pulsa [J]")
    print("--> Para ver las instrucciones del Blackjack, pulsa [I]")
    print("--> Para ver los creadores de este juego, pulsa [C]")
    print("--> Para salir del menú, pulsa [S]")
    print("")
    menu = input("Que quieres hacer? Escribe la letra correspondiente: ").lower()
    if menu == "j":
        mostrarBlackjack(menu)
    elif menu == "i":
        mostrarInstrucciones(menu)
    elif menu == "c":
        mostrarCreadores(menu)
    elif menu == "s":
        mostrarSalir(menu)
    else:
        print("--> ", menu, "no es una letra correspondiente. <--")
# programa principal 

if __name__ == "__main__":
    gestionarMenu()
