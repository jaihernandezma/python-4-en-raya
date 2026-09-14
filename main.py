import random
import sys
import juego.variables as var
from juego.estadisticas import guardar_y_mostrar_estadisticas
print("¡🄱🄸🄴🄽🅅🄴🄽🄸🄳🄾🅂 🄰🄻 🄼🄴🄹🄾🅁 🄹🅄🄴🄶🄾 🄳🄴 🄲🄾🄽🄴🄲🅃🄰4!")

from juego.validaciones import jugador #importacion condiciones nombres


#Introduccion de los nombres de los jugadores.
#Se invoca la funcion para comprobar las validaciones de los nombres
nombre_1=input("Nombre de un jugador: ")
nombre_1=jugador(nombre_1,1)

while True: #Verificacion de nombres diferentes
    nombre_2=input("Nombre del otro jugador: ")
    nombre_2=jugador(nombre_2, 2)

    if nombre_2.lower()==nombre_1.lower():
        print("¡Los nombres no pueden ser iguales! Por favor, elige un nombre diferente para el otro jugador.")
    else:
        break
#formato nombres
nombre_1=nombre_1.capitalize().title()
nombre_2=nombre_2.capitalize().title()


#Elegir quien empieza:
eleccion=random.randint(1,2)
if eleccion==1:
  jugador1=nombre_1+" "+"(X)"
  jugador2=nombre_2+" "+"(0)"
  print(f"Empieza {jugador1}, sigue {jugador2}")
else:
  jugador1=nombre_2+" "+"(X)"
  jugador2=nombre_1+" "+"(0)"
  print(f"Empieza {jugador1}, sigue {jugador2}")

from juego.validaciones import validar #importacion condiciones tablero

filas=input("Ingresa la cantidad de filas que deseas en el tablero:")
filas=validar(filas,"filas")

columnas=input("Ingresa la cantidad de columnas que deseas en el tablero:")
columnas=validar(columnas,"columnas")

from juego.tablero import creacion_tablero #importacion tablero

tablero=creacion_tablero(filas, columnas)

from juego.tablero import mostrar_tablero

from juego.victoria import tablero_lleno #importar condicion para tablero lleno

from juego.victoria import verificar_victoria #importar condiciones de victoria

#Mensaje recordatorio a los jugadores
print("¡ATENCIÓN, RECUERDA!:")
print("1. GANARÁS AL CONECTAR 4 EN RAYA SEA HORIZONTAL, VERTICAL O DIAGONAL.\n2. SI TE GUSTA EL AZAR, PON -RANDOM- Y DEJA QUE LA MÁQUINA DECIDA.")
print("¡¡SUERTE!!")
print()
mostrar_tablero(tablero)

from juego.victoria import jugadas

while True:
    juego_terminado = jugadas(filas, columnas, tablero, var.ganadores, jugador1, jugador2)


#Si termina el juego se pregunta para volver a iniciar o no
    if juego_terminado:
        #Contamos las partidas que se han terminado para acumular las totales
        var.contador+=1
        #Ponemos en una lista el tablero final que se ha jugado
        var.tableros_finales.append(tablero)
        seguir_jugando=True
        while True:# solicitud se continuacion(si/no)
          respuesta=input("¿¿Vamos por otra ronda? (si/no): ").strip().lower()
          if respuesta=="si":
            #se vuelve a preguntar las filas y columnas y se empieza otra vez a jugar con el nuevo tablero
              filas=input("Ingresa la cantidad de filas que deseas en el tablero:")
              filas=validar(filas,"filas")
              columnas=input("Ingresa la cantidad de columnas que deseas en el tablero:")
              columnas=validar(columnas,"columnas")
              tablero=creacion_tablero(filas, columnas)
              mostrar_tablero(tablero)
              break
              #si la persona dice que no, se guardan los respectivos datos en un archivo
          elif respuesta=="no":
              guardar_y_mostrar_estadisticas(jugador1, jugador2, var.contador, var.victorias_jugador1, var.victorias_jugador2, var.empate, var.tableros_finales, var.ganadores)

              break
          #Ponemos una restriccion por si el jugador pone algo diferente a si o no
          else:
              print("Respuesta invalida. Por favor escribe 'si' o 'no'.")
        if respuesta=="no":
          break