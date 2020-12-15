# proyecto-1a-evaluacion-python-alberto-cesar-josep-maria
proyecto-1a-evaluacion-python-alberto-cesar-josep-maria created by GitHub Classroom

Objetivo:  Crear un programa capaz de jugar a Blackjack con el usuario, en una primera
versión jugará con 1 usuario, si hay tiempo se hará la versión con más de 1 usuario.

Primer dia:

Hoy hemos establecido como objetivo del proyecto de Programación crear el Juego de BLACKJACK.
Empezamos repasando la metodología SCRUM, la cual seguiremos en este proyecto, ya que nunca
habíamos trabajado con ella.
Hemos hecho nuestro primer scrum diario donde hemos hecho nuestro primer sprint planning: en 
este sprint comenzamos a desarrollar las ideas principales del proyecto: desde aprender las 
normas del juego, ya que no todos las conocemos, hasta determinar qué funciones necesitaremos 
para este juego. 
Hemos pensado que el juego será de un jugador + dealer, y además necesitaremos crear unas listas 
para nuestras barajas.También hemos decidido que haremos un menú principal con las opciones: jugar,
instrucciones, creadores y salir.

Segundo dia: 

En el SCRUM de hoy hemos repartido unas cuantas funciones entre los 3, cada uno se ha centrado en
la parte que le tocaba y hemos empezado a programar, el menú del Blackjack ha empezado a tomar forma.
Nuestras funciones principales van a ser: Def barajar(mazo), def total(mano), def pedir(mano), def victoria, def derrota, menú, volver menú, puntuación, juego, instrucciones y creadores.
Del menú, instrucciones, creadores se encarga Alberto. Hemos previsto que en esta clase de 2 horas lo podemos tener hecho.
De lo relacionado con el mazo y la mano del jugador y dealer se encarga Josep.
César está creando el juego y está incluyendo un sistema de puntuación basado en WINS y LOSES (que son las wins del Dealer).

Tercer dia:

En el Scrum de hoy hemos vuelto a repasar que funciones teníamos cada uno, hemos seguido programando
y el menú está acabado. La parte del juego y puntuaciones lleva un poco más de trabajo así que ho le hemos dedicado tiempo todos. Hemos acabado con las funciones asignadas a cada uno y nos hemos dado cuenta que necesitaremos crear alguna más porque hay posibles casos que no cubrimos. Hemos decidido incluir la función BlackJack para el caso concreto en que en la primera mano si se reparten cartas por valor de 21 ya no se pregunta por si quieres seguir cogiendo cartas y queremos que aparezca ya como BLACKJACK, win o lose (si se trata del dealer).


Cuarto dia:

En el Scrum de hoy hemos acabado todas las funciones planificadas anteriormente y hemos implementado 
una función nueva que no teníamos prevista, llamada mostrarMarcador(), la cual se accede desde el 
menú al haber acabado una partida, después de ver el resultado, hemos decidido simplificarlo y así poder realizar partidas consecutivas sin tener qe viajar tanto entre ventanas. La solución ha sido poner el marcador en el Menú principal, así el jugador siempre ve cuantas WINS y cuantas LOSES lleva antes de empezar una nueva partida.

La entrea del proyecto se ha adelantado así que la opción de incluir más jugadores la hemos descartado para poder dedicar el poco tiempo que nos queda a ensamblar todas las funciones, poder hacer que funcionen correctamente juntas y le hemos dado un pequeño toque estético.

