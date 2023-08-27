#Algoritmo de las Reinas de ajedrez.
#Busca la posición de 4 reinas en un mapa de 4x4 en la que ninguna de ellas
#esté en posicion para atacarse entre ellas, es decir no deben compartir ni fila,
#columna, ni diagonales. Este algoritmo no retorna las coordenadas de cada reina
#pero genera una respuesta True si se puede solucionar el problema, y un False
#si no se puede.
#No se me ocurre ninguna aplicacion que no tenga que ver con ia o matematicas
#aplicable a la vida real, fuera de dar acomodo a objetos con restricciones de
#posición, como torres electricas, columnas etc.

def cuatro_reinas(fila):
    k=0  # inicia en la columna 0, que es la primera
    n=len(fila)
    # como fila(k) se incrementa antes de usarla, se hace fila(0) igual a -1, que es la posicion inexistente 0
    fila[k]=-1
    while k>-1:
        fila[k]+=1
        # se busca un movimiento legal en la columna k
        while(fila[k]<n) and not legal(fila,k):
            fila[k]+= 1
        if fila[k]<n:
            if k==n-1:
                return True
            else:
                k+=1  # siguiente columna
                fila[k]=-1
        else:
            k-=1  # regresar a columna anterior
    return False  # no hay solución

def legal(fila,columna):
    for i in range(columna):
        if fila[i]==fila[columna] or fila[i]-fila[columna]==columna-i or fila[columna]-fila[i]==columna-i:
            return False
    return True

fila = [0,0,0,0]
if cuatro_reinas(fila) == True:
    print("True")
else:
    print("False")