"""
Examen inteligencia artificial 20310407
"""
#Algoritmo pim, reduce una matriz de nodos y vertices "con peso" a una grafo
#con la menor cantidad de peso posible que conecte el nodo "0, o 1" al cualquier
#otro nodo.
#En el ejemplo de la prectica "algoritmo" en el que cada nodo es un objetivo y
#cada vertice una actividad, ahora podemos definir la dificultad de cada act.
#y por lo tanto dar el camino de actividades mas "sencillo" para lograr todos
#los objetivos.

def prim(w,n,s):
    v=[]
    while(len(v)!=n):
        v.append(0)
    v[s]=1
    E=[]
    for i in range(0, n-1):
        minimo=9
        add_ver=0
        e = []
        for j in range(0,n):
            if(v[j]==1):
                for k in range(0,n):
                    if(v[k]==0 and w[j][k] < minimo):
                        add_ver = k
                        e=[j,k]
                        minimo=w[j][k]
        v[add_ver]=1
        E.append(e)
    return E

n=6
s=0
w=[#1,2,3,4,5,6 coordenadas de concecciones entre las aristas 9=no existe conección
   [9,4,2,9,3,9],   #1
   [4,9,9,5,9,9],   #2
   [2,9,9,1,6,3],   #3
   [9,5,1,9,9,6],   #4
   [3,9,6,9,9,2],   #5
   [9,9,3,6,2,9],   #6
   ]

print(prim(w,n,s))
# El resultado se imprime de 0 a 5, no de 1 a 6 para los vertices