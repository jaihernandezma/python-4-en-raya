#Validación de las condiciones de los nombres
def jugador(nombre_jugador,number):
    while True:
        if nombre_jugador=="":
            nombre_jugador=input(f"¡No puedes ingresar espacios vacios!\nNombre del jugador {number}:")
        elif len(nombre_jugador)>10:
            nombre_jugador=input(f"¡No puedes ingresar un nombre tan largo!\nNombre del jugador {number}:")
        elif not nombre_jugador.isalpha():
            nombre_jugador=input(f"¡No puedes ingresar numeros, solo letras!\nNombre del jugador {number}:")
        else:
            return nombre_jugador
        
#Introduccion y validacion del numero de filas y columnas, se usará una función para las validaciones
def validar(numero,tipo):
    while True:
        if numero=="":
            numero=input(f"¡No puedes ingresar espacios vacios!\nIngresa la cantidad de {tipo} que deseas en el tablero:")
        elif not numero.isdigit():
            numero=input(f"¡Solo puedes ingresar numeros enteros positivos!\nIngresa la cantidad de {tipo} que deseas en el tablero:")
        elif int(numero)<4:
            numero=input(f"¡No puedes ingresar un numero menor a 4!\nIngresa la cantidad de {tipo} que deseas en el tablero:")
        else:
            return int(numero)
