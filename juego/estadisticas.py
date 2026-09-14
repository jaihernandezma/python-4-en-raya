def guardar_y_mostrar_estadisticas(jugador1, jugador2, contador, victorias_jugador1, victorias_jugador2, empate, tableros_finales, ganadores):
    print("¡Gracias por jugar! Aqui tienes tus estadisticas")

    with open("Estadisticas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("===========================================\n\n")
        archivo.write("=== Estadísticas de la sesión del juego ===\n")
        archivo.write(f"Nombre del jugador 1: {jugador1}\n")
        archivo.write(f"Nombre del jugador 2: {jugador2}\n")
        archivo.write(f"Numero de partidas jugadas: {contador}\n")
        archivo.write(f"Numero de victorias de {jugador1}: {victorias_jugador1}\n")
        archivo.write(f"Numero de victorias de {jugador2}: {victorias_jugador2}\n")
        archivo.write(f"Numero de empates: {empate}\n")
#usaremos un ciclo para recorrer la lista creada con los tableros finales del juego y asi poder imprimir cada ronda con su tablero y ganador
        for i in range(len(tableros_finales)):
            archivo.write("\n")
            archivo.write(f"=== Tablero al final de la partida #{i+1} ===\n")
            for fila in tableros_finales[i]:
                archivo.write("     "+"+"+" "+" ".join(fila)+" "+"+\n")
            archivo.write(f"{ganadores[i]}\n")

        archivo.write("\n===========================================\n")

#Aqui imprimimos el archivo previamente creado
    with open("Estadisticas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea, end="")
