import random
import os
os.system('cls')

wins = 0
loses = 0

#jugarems con 2 mazos
mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*8

# definiciones
# 2 cartas al azar del mazo
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
#####################-suma valor cartas mano-################################
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
    return mano
####################-Funciones puramente visuales-################################
def victoria():
    print("\033[1;34;40m __        ___       ")
    print(" \ \      / (_)_ __  ")
    print("  \ \ /\ / /| | '_ \ ")
    print("   \ V  V / | | | | |")
    print("    \_/\_/  |_|_| |_|\033[0;37;40m")
    print("")

def derrota():
    print("\033[1;31;40m  _                    ")
    print(" | |    ___  ___  ___  ")
    print(" | |   / _ \/ __|/ _ \ ")
    print(" | |__| (_) \__ \  __/ ")
    print(" |_____\___/|___/\___| \033[0;37;40m")
    print("")

##########################################################################       
def blackjack(barajaJugador, barajaDealer):
    global wins
    global loses
    if total(barajaJugador) == 21:
        print(barajaJugador, barajaDealer)
        print ("\033[1;32;40mFelicidades! Tienes un blackjack!\033[0;37;40m")
        victoria()
        wins += 1
        volverMenu()
    elif total(barajaDealer) == 21:
        print(barajaJugador, barajaDealer)
        print ("\033[0;31;40mLástima! El dealer tiene un blackjack.\033[0;37;40m")
        derrota()
        loses += 1
        volverMenu()
##########################################################################
def volverMenu():
    volver = input("\033[1;32;40mQuieres volver al menú? (S/N) : \033[0;37;40m").lower()
    if volver == "s":
        barajaJugador = []
        barajaDealer = []
        mazo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*8
        gestionarMenu()
    else:
        print("Adiós!")
        exit()
##########################################################################
def puntuacion(barajaJugador, barajaDealer):
    global wins
    global loses
    if total(barajaJugador) == 21:
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[1;34;40mFelicidades! Tienes un Blackjack!\033[0;37;40m")
        victoria()
        wins += 1
    elif total(barajaJugador) > 21:
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[0;31;40mLástima! Tienes más de 21.\033[0;37;40m")
        derrota()
        loses += 1
    elif total(barajaDealer) == 21:
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[1;31;40mLástima! El dealer tiene un Blackjack.\033[0;37;40m")
        derrota()
        loses +=1
    elif total(barajaDealer) > 21:
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[0;34;40mVaya! El dealer se ha pasado de 21, ganas!\033[0;37;40m")
        victoria()
        wins += 1
    elif total(barajaJugador) > total(barajaDealer):
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[0;34;40mFelicidades! Tienes más que el dealer!\033[0;37;40m")
        victoria()
        wins += 1
    elif total(barajaJugador) < total(barajaDealer):
        print("Tu mano es ", barajaJugador, "y la del dealer es", barajaDealer)
        print("\033[0;31;40mLástima! Te ha ganado el dealer.\033[0;37;40m")
        derrota()
        loses += 1
##########################################################################
def juego():
    global wins
    global loses
    eleccion = 0
    barajaJugador = barajar(mazo)
    barajaDealer = barajar(mazo)
    print("El dealer muestra una de sus cartas, y es: ", str(barajaDealer[0]))
    print("Tienes las siguientes cartas: ", str(barajaJugador), ". Con un total de :", str(total(barajaJugador)))
    blackjack(barajaJugador, barajaDealer)
    quit = False
    while not quit:
        eleccion = input("\033[1;32;40mQuieres Pedir\033[0;37;40m[P]\033[1;32;40m, Plantarte\033[0;37;40m[X]\033[1;32;40m o Salir\033[0;37;40m[S]\033[1;32;40m?\033[0;37;40m").lower()
        if eleccion == "p":
            pedir(barajaJugador)
            print(barajaJugador)
            print("El total de tu mano es: ", str(total(barajaJugador)))
            if total(barajaJugador) > 21:
                print("\033[0;31;40mTe has pasado de 21!\033[0;37;40m")
                derrota()
                loses += 1
                volverMenu()
        elif eleccion == "x":
            while total(barajaDealer) < 17:
                pedir(barajaDealer)
                print(barajaDealer)
                if total(barajaDealer)>21:
                    print('\033[0;34;40mEl dealer se ha pasado de 21! Has ganado!\033[0;37;40m')
                    victoria()
                    wins += 1
                    volverMenu()
            puntuacion(barajaJugador, barajaDealer)
            volverMenu()
        elif eleccion == "s":
            print("Adiós!")
            quit = True
            exit()
##########################################################################
#La chacha de la limpieza
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')            
#######################-Visual + arrancamos partida-############################
def mostrarBlackjack(menu):
    if (menu == "J") or  (menu == "j"):
        print("\033[0;32;93mVamos a jugar a BlackJack!\033[0;37;40m")       
        print("              __               ")                                
        print("        _..-''--'----_.        ")                                
        print("      ,''.-''| .---/ _`-._     ")                                
        print("    ,' \ \  ;| | ,/ / `-._`-.  ")                                
        print("  ,' ,',\ \( | |// /,-._  / /  ")                                
        print("  ;.`. `,\ \`| |/ / |   )/ /   ")                                
        print(" / /`_`.\_\ \| /_.-.'-''/ /    ")                                
        print("/ /_|_:.`. \ |;'`..')  / /     ")                                
        print("`-._`-._`.`.;`.\  ,'  / /      ")                                
        print("    `-._`.`/    ,'-._/ /       ")                                
        print("      : `-/     \`-.._/        ")                                
        print("      |  :      ;._ (          ")                                
        print("      :  |      \  ` \         ")                                
        print("       \         \   |         ")                                
        print("        :        :   ;         ")                                
        print("        |           /          ")                                
        print("        ;         ,'           ")                                
        print("       /         /             ")                                
        print("      /         /              ")                                
        print("               /               ")
        juego()
##########################################################################
def mostrarInstrucciones(menu):

    print("\033[0;32;93m╦┌┐┌┌─┐┌┬┐┬─┐┬ ┬┌─┐┌─┐┬┌─┐┌┐┌┌─┐┌─┐")
    print("║│││└─┐ │ ├┬┘│ ││  │  ││ ││││├┤ └─┐")
    print("╩┘└┘└─┘ ┴ ┴└─└─┘└─┘└─┘┴└─┘┘└┘└─┘└─┘\033[0;37;40m")
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
    menu = input("\033[1;32;40mQuieres volver al menú? \033[0;37;40m[S/N] \033[0;37;40m").lower()
    if menu == "s":
        gestionarMenu()
    else:
        print("Adiós!!!")
        exit()
##############################################################################
def mostrarCreadores(menu):
    print("\033[0;32;93mCreadores de este BlackJack:\033[0;37;40m")
    print("Este juego de BlackJack hecho en Python 3.9.0 ha sido creado por:\n\
    --> César Andrés Granda, Alberto Serrano y Josep Maria Jiménez <--")
    print("\033[1;36;40m ██████╗███████╗███████╗ █████╗ ██████╗ ")
    print("██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗")
    print("██║     █████╗  ███████╗███████║██████╔╝")
    print("██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗")
    print("╚██████╗███████╗███████║██║  ██║██║  ██║")
    print(" ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print(" █████╗ ██╗     ██████╗ ███████╗██████╗ ████████╗ ██████╗ ")
    print("██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗")
    print("███████║██║     ██████╔╝█████╗  ██████╔╝   ██║   ██║   ██║")
    print("██╔══██║██║     ██╔══██╗██╔══╝  ██╔══██╗   ██║   ██║   ██║")
    print("██║  ██║███████╗██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝")
    print("╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ")
    print("     ██╗ ██████╗ ███████╗███████╗██████╗ ")
    print("     ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗")
    print("     ██║██║   ██║███████╗█████╗  ██████╔╝")
    print("██   ██║██║   ██║╚════██║██╔══╝  ██╔═══╝ ")
    print("╚█████╔╝╚██████╔╝███████║███████╗██║     ")
    print(" ╚════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝     ")
    menu = input("\033[1;32;40mQuieres volver al menú? \033[0;37;40m[S/N] \033[0;37;40m").lower()
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

# menu y hacemos bonito
def gestionarMenu():
    clear()
    print("\033[1;32;93m                  ---> Bienvenido al menú <---\n")
    print("\033[1;37;40m.------..------..------..------..------..------..------..------..------.")
    print("|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |")
    print("| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |")
    print("| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |")
    print("| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|")
    print("`------'`------'`------'`------'`------'`------'`------'`------'`------'\n")
    print("\033[1;34;40m")
    print("          ╦ ╦┬┌┐┌┌─┐                        \033[1;31;40m╦  ┌─┐┌─┐┌─┐┌─┐\033[1;34;40m")
    print("          ║║║││││└─┐= ", wins, "                   \033[1;31;40m║  │ │└─┐├┤ └─┐= ", loses,"\033[1;34;40m")
    print("          ╚╩╝┴┘└┘└─┘                        \033[1;31;40m╩═╝└─┘└─┘└─┘└─┘\033[0;37;40m")
    print("\n")
    print("\033[0;32;93m--> Para jugar a BlackJack, pulsa\033[0;37;40m[J]\033[0;32;93m")
    print("--> Para ver las instrucciones del Blackjack, pulsa\033[0;37;40m [I]\033[0;32;93m")
    print("--> Para ver los creadores de este juego, pulsa\033[0;37;40m [C]\033[0;32;93m")
    print("--> Para salir del menú, pulsa\033[0;37;40m [S]\033[0;32;93m")
    print("")
    menu = input("\033[1;32;40mQue quieres hacer? Escribe la letra correspondiente: \033[0;37;40m").lower()
    if menu == "j":
        clear()
        mostrarBlackjack(menu)
    elif menu == "i":
        clear()
        mostrarInstrucciones(menu)
    elif menu == "c":
        clear()
        mostrarCreadores(menu)
    elif menu == "s":
        clear()
        mostrarSalir(menu)
    else:
        print("--> ", menu, "no es una letra correspondiente. <--")

# programa principal 
clear()
gestionarMenu()