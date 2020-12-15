import os
import random
os.system('cls')


# El usuario elige el numero de mazos que va a usar
mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(4)

# se inicializa la puntuación
victorias = 0
derrotas = 0

# Mezclar mazo y nombrar J,Q,K,A
def mezclar(mazo):
    mano = []
    for i in range(2):
        random.shuffle(mazo)
        carta = mazo.pop()
        if carta == 11:carta = "J"
        if carta == 12:carta = "Q"
        if carta == 13:carta = "K"
        if carta == 14:carta = "A"
        mano.append(carta)
    return mano

def jugar_de_nuevo():
    again = input("Quieres jugar de Nuevo? (Y/N) : ").lower()
    if again == "y":
        mano_dealer = []
        mano_jugador = []
        mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        juego()
    else:
        print("Adiós!")
        gestionarMenu()

#suma de los puntos de las cartas
def total(mano):
    total = 0
    for carta in mano:
        if carta == "J" or carta == "Q" or carta == "K":
            total+= 10
        elif carta == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += carta
    return total

#Coger una carta más
def hit(mano):
    carta = mazo.pop()
    if carta == 11:carta = "J"
    if carta == 12:carta = "Q"
    if carta == 13:carta = "K"
    if carta == 14:carta = "A"
    mano.append(carta)
    return mano

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

#visualizar resultados manos
def print_resultados(mano_dealer, mano_jugador):
    clear()

    print("\n    Bienvenido a la mesa de BlackJack!\n")
    print ("The dealer has a " + str(mano_dealer) + " for a total of " + str(total(mano_dealer)))
    print ("You have a " + str(mano_jugador) + " for a total of " + str(total(mano_jugador)))

#BlackJack 21 puntos dealer y jugador
def blackjack(mano_dealer, mano_jugador):
    global victorias
    global derrotas
    if total(mano_jugador) == 21:
        print_resultados(mano_dealer, mano_jugador)
        print ("Tienes un BLACKJACK!\n")
        victorias += 1
        jugar_de_nuevo()
    elif total(mano_dealer) == 21:
        print_resultados(mano_dealer, mano_jugador)
        print ("F en el chat! Pierdes,el Dealer tiene BlackJack.\n")
        derrotas += 1
        jugar_de_nuevo()

def puntuar(mano_dealer, mano_jugador):
        global victorias
        global derrotas
        if total(mano_jugador) == 21:
            print_resultados(mano_dealer, mano_jugador)
            print ("Enhorabuena! tienes un BlackJack!\n")
            victorias += 1
        elif total(mano_dealer) == 21:
            print_resultados(mano_dealer, mano_jugador)
            print ("F en el chat! Pierdes,el Dealer tiene un BlackJack.\n")
            derrotas += 1
        elif total(mano_jugador) > 21:
            print_resultados(mano_dealer, mano_jugador)
            print ("Pierdes, sumas más de 21.\n")
            derrotas += 1
        elif total(mano_dealer) > 21:
            print_resultados(mano_dealer, mano_jugador)
            print ("El Dealer tiene más de 21, Tu GANAS!\n")
            victorias += 1
        elif total(mano_jugador) < total(mano_dealer):
            print_resultados(mano_dealer, mano_jugador)
            print ("Tu puntuación es menor que la del Dealer. PIERDES.\n")
            derrotas += 1
        elif total(mano_jugador) > total(mano_dealer):
            print_resultados(mano_dealer, mano_jugador)
            print ("Tu puntuación es mayor! tu GANAS!\n")
            victorias += 1

def juego():
    global victorias
    global derrotas
    choice = 0
    clear()
    mano_dealer = mezclar(mazo)
    mano_jugador = mezclar(mazo)
    print ("The dealer is showing a " + str(mano_dealer[0]))
    print ("You have a " + str(mano_jugador) + " for a total of " + str(total(mano_jugador)))
    blackjack(mano_dealer, mano_jugador)
    quit=False
    while not quit:
        choice = input("¿Que quieres hacer? [c]oger carta, [p]lantarse, or [s]alir al menú: ").lower()
        if choice == 'c':
            hit(mano_jugador)
            print(mano_jugador)
            print("Total mano: " + str(total(mano_jugador)))
            if total(mano_jugador)>21:
                print('Te has pasado')
                derrotas += 1
                jugar_de_nuevo()
        elif choice=='p':
            while total(mano_dealer)<17:
                hit(mano_dealer)
                print(mano_dealer)
                if total(mano_dealer)>21:
                    print('El Dealer se ha pasado, tu GANAS!')
                    victorias += 1
                    jugar_de_nuevo()
            puntuar(mano_dealer,mano_jugador)
            jugar_de_nuevo()
        elif choice == "s":
            print("Adiós!")
            gestionarMenu()

import random
import os
os.system('cls')

# definiciones

def mostrarBlackjack(menu):
    if (menu == "J") or  (menu == "j"):
        print("Vamos a jugar a BlackJack!")
        juego()
##########################################################################
def mostrarInstrucciones(menu):    
    if (menu == "I") or (menu == "i"):
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
        menu = input("Quieres volver al menú? [S/N] ")
        if (menu == "S") or (menu == "s"):
            gestionarMenu()
        else:
            print("Adiós!!!")
##############################################################################
def mostrarCreadores(menu):    
    if (menu == "C") or (menu == "c"):
        print("Creadores de este BlackJack:")
        print("Este juego de BlackJack hecho en Python 3.9.0 ha sido creado por:\n\
--> César Andrés Granda, Alberto Serrano y Josep Maria Jiménez <--")
    menu = input("Quieres volver al menú? [S/N] ")
    if (menu == "S") or (menu == "s"):
        gestionarMenu()
    else:
        print("Adiós!!!")
##############################################################################
def mostrarSalir(menu):    
    if (menu == "S") or (menu == "s"):
        print("Adiós!!!")

# menu
def gestionarMenu():
        clear()
        print("\033[1;32;40m ---> Bienvenido al menú <---  \n")
        print("")
        print("-"*30+"\n")
        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (victorias, derrotas))
        print("-"*30+"\n")
        print("--> Para jugar a BlackJack, pulsa [J]")
        print("--> Para ver las instrucciones del Blackjack, pulsa [I]")
        print("--> Para ver los creadores de este juego, pulsa [C]")
        print("--> Para salir del menú, pulsa [S]")
        print("")
        menu = input("Que quieres hacer? Escribe la letra correspondiente: ")
        if (menu == "J") or (menu == "j"):
            mostrarBlackjack(menu)
        elif (menu == "I") or (menu == "i"):
            mostrarInstrucciones(menu)
        elif (menu == "C") or (menu == "c"):
            mostrarCreadores(menu)
        elif (menu == "S") or (menu == "s"):
            mostrarSalir(menu)
        else:
                print("--> ", menu, "no es una letra correspondiente. <--")
# programa principal 

gestionarMenu()

if __name__ == "__main__":
   juego()