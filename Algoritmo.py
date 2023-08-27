"""
Created on Sun Feb 19 18:42:41 2023

@author: sadma
"""
#Este codigo te permite reducir el numero de vertices en un grafo dejando solo
#los vertices necesarios para conectar de la manera mas corta posible el vertice 
#"a" al resto de vertices, eliminando caminos ineficientes.
#Este algoritmo puede usrse par planificar actividades, es decir, a es el principio,
#y necesitamos llegar a los objetivos b,c,d,e,f,g y h, pero no puede realizarlas 
#de manera independiente, se necesita realizar una serie de requisitos para poder 
#pasar de un objetivo a otro. En el caso para llegar a "h", se necesita haber
#llegado a "f", y para llegar a "f" se necesita haber realizado "e", o "d", etc.
#Al final hay rutas en las que realizas mas o la misma cantidad de actividades 
#de las necesarias para llegar al mismo objetivo, y el algoritmo te da la ruta 
#que conecta en, menos pasos, el origen con cada objetivo.
def bla(E,V):
    S=[]
    S.append(V[0])
    V1=[]
    V1.append(V[0])
    E1=[]
    S1=[]
    
    while True:
        boo=True
        for x in S:
            diferencia(V,V1)
            for y in Vaux:
                z=(x,y)
                if z in E:
                    E1.append(z)
                    V1.append(y)
                    S1.append(y)
                    boo=False
        if boo:
            print(V1)
            print(E1)
            return V1+E1
        S=S1
        S1=[]
        
def diferencia(A,B):
    for i in B:
        if i in A:
            if i in Vaux:
                Vaux.remove(i)

V=['a','b','c','d','e','f','g','h']
Vaux=['a','b','c','d','e','f','g','h']
E=[('a','b'),('b','g'),('b','d'),('d','f'),('f','h'),('e','f'),('c','d'),('c','e'),('a','g'),('e','g'),('a','c')]
T=bla(E, V)