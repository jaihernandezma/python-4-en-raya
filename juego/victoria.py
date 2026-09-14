import random
from juego.tablero import mostrar_tablero
import juego.variables as var 
##Funcion para verificar si el tablero esta lleno##
def tablero_lleno(tablero):
    # Solo necesitamos comprobar la fila superior del área de juego
    for celda in tablero[2]:
        if celda == "○":
            return False # Si hay al menos un espacio, no está lleno
    return True # Si no se encontraron espacios, está lleno

## Funcion de verificacion de los distintos casos de victoria##
def verificar_victoria(ficha, tablero, filas, columnas):

    # Verificar victoria horizontal
    for c in range(columnas - 3):
        for r in range(2, filas + 2): # Rango de filas jugables
            if tablero[r][c] == ficha and tablero[r][c+1] == ficha and tablero[r][c+2] == ficha and tablero[r][c+3] == ficha:
                return True

    # Verificar victoria vertical
    for c in range(columnas):
        for r in range(2, filas - 1): # Rango de filas jugables
            if tablero[r][c] == ficha and tablero[r+1][c] == ficha and tablero[r+2][c] == ficha and tablero[r+3][c] == ficha:
                return True

    # Verificar victoria diagonal desde abajo
    for c in range(columnas - 3):
        # Recorrido de filas jugables de abajo hacia arriba
        for r in range(5, filas + 2):
            if tablero[r][c] == ficha and tablero[r-1][c+1] == ficha and tablero[r-2][c+2] == ficha and tablero[r-3][c+3] == ficha:
                return True

    # Verificar victoria diagonal desde arriba
    for c in range(columnas - 3):
        # Recorrido de filas jugables de arriba hacia abajo
        for r in range(2, filas - 1):
            if tablero[r][c] == ficha and tablero[r+1][c+1] == ficha and tablero[r+2][c+2] == ficha and tablero[r+3][c+3] == ficha:
                return True

    return False

##Funcion para ejecutar las interacciones con el tablero##
def jugadas(filas, columnas, tablero, ganadores, jugador1, jugador2):
    global victorias_jugador1
    global victorias_jugador2
    global empate
    global contador
    global tableros_finales

    #Comporbacion del ingreso correcto de la columna jugada#
    jugada_exitosa=False
    while not jugada_exitosa:
            columna_j1=input(f"Elige en que columna deseas jugar\nTurno de {jugador1}:")
            if columna_j1.lower()=="random":
                while True:
                  #Agregamos la libreria random para que el jugador pueda dejar que la computadora eliga la casilla a jugar
                  jugadas1=random.randint(1,columnas)
                  print(f"La computadora ha elegido la columna {jugadas1}")

                  for i in range(filas+1,0,-1):
                        if tablero[i][jugadas1-1]=="○":
                            tablero[i][jugadas1-1]="X"
                            jugada_exitosa=True
                            break
                  if jugada_exitosa:
                    break
                  else:
                    print("¡Esa columna está llena! Eligiendo otra al azar.")
            elif columna_j1.strip().isdigit():
                jugadas1=int(columna_j1)
                if 1<=jugadas1<=columnas:

                          #Recorrido y confirmacion de que la casilla no se encuentra ocupada#
                  for i in range(filas+1,0,-1):
                    if tablero[i][jugadas1-1]=="○":
                      tablero[i][jugadas1-1]="X"
                      jugada_exitosa=True
                      break
                  if not jugada_exitosa:
                    print("¡Esa columna está llena! Elige otra.")
                else:
                        print("¡Esa columna no existe!")
            else:
                  print("¡Error! Solo puedes ingresar un número entero positivo.")
    mostrar_tablero(tablero)

    #Verificacion de victoria de jugador 1
    if verificar_victoria("X", tablero, filas, columnas):
        print(f"¡🄵🄴🄻🄸🄲🄸🄳🄰🄳🄴🅂 {jugador1},🄷🄰🅂 🄶🄰🄽🄰🄳🄾!")
        var.ganadores.append(f"{jugador1} ha ganado la partida (˶ˆᗜˆ˵)")
        var.victorias_jugador1+=1
        return True


        #Comprobacion del ingreso correcto de la columna jugada y alteracion del tablero#
    jugada_exitosa=False
    while not jugada_exitosa:
      columna_j2=input(f"Elige en que columna deseas jugar\nTurno de {jugador2}:")
      if columna_j2.lower()=="random":
          while True:
            #Agregamos la libreria random para que el jugador pueda dejar que la computadora eliga la casilla a jugar
            jugadas2=random.randint(1,columnas)
            print(f"La computadora ha elegido la columna {jugadas2}")

            for i in range(filas+1,0,-1):
                  if tablero[i][jugadas2-1]=="○":
                      tablero[i][jugadas2-1]="0"
                      jugada_exitosa=True
                      break
            if jugada_exitosa:
              break
            else:
              print("¡Esa columna está llena! Eligiendo otra al azar.")
      elif columna_j2.strip().isdigit():
          jugadas2=int(columna_j2)
          if 1<=jugadas2<=columnas:

                    #Recorrido y confirmacion de que la casilla no se encuentra ocupada#
            for i in range(filas+1,0,-1):
              if tablero[i][jugadas2-1]=="○":
                tablero[i][jugadas2-1]="0"
                jugada_exitosa=True
                break
            if not jugada_exitosa:
              print("¡Esa columna está llena! Elige otra.")
          else:
                  print("¡Esa columna no existe!")
      else:
            print("¡Error! Solo puedes ingresar un número entero positivo.")
    mostrar_tablero(tablero)
    #Verificacion de victoria de jugador 2

    if verificar_victoria("0", tablero, filas, columnas):
        print(f"¡🄵🄴🄻🄸🄲🄸🄳🄰🄳🄴🅂 {jugador2}, 🄷🄰🅂 🄶🄰🄽🄰🄳🄾!")
        var.ganadores.append(f"{jugador2} ha ganado la partida (˶ˆᗜˆ˵)")
        var.victorias_jugador2+=1
        return True # Devuelve True para indicar que el juego terminó

    # Verificar si hay empate
    if tablero_lleno(tablero):
        print("¡🄴🄻 🄹🅄🄴🄶🄾 🄴🅂 🅄🄽 🄴🄼🄿🄰🅃🄴!")
        var.ganadores.append("La partida ha terminado en un empate (￢_￢;)")
        var.empate+=1
        return True

    return False # Devuelve False para indicar que el juego continúa

