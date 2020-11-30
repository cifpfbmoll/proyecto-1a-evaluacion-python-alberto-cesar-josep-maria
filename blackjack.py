import random
import os
os.system('cls')

# definiciones

def mostrarBlackjack(menu):
    if (menu == "J") or  (menu == "j"):
        print("Vamos a jugar a BlackJack!")
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
        print("---> Bienvenido al menú <---")
        print("")
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