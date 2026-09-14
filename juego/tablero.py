#Generacion inicial del tablero, teniendo en cuenta los datos ingresados por el usuario(A través de la funcion "tablero" para facilitar su uso).

##Generacion matriz del tablero##
def creacion_tablero(filas, columnas):
    tabla=[]
    fila_c=[]
    for q in range(1,columnas+1):
        fila_c.append(str(q))
    tabla.append(fila_c)
    fila_d=["-"for _ in range(columnas)]
    tabla.append(fila_d)
    for i in range(1,filas+1):
        filas_n=[]
        for s in range(columnas):
            filas_n.append("○")
        tabla.append(filas_n)
    tabla.append(fila_d)
    return tabla

##Funcion para mostar el tablero##
def mostrar_tablero(tablero):
    for d in tablero:
        print("+"," ".join(d),"+")

