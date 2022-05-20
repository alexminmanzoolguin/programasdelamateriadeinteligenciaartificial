#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
print("BIENVENIDO AL GRUPO 8S12")
print("MANZO OLGUIN ALEX YAZMIN 7S12")
#inciamos pa parte grafica de nuestra neurona
entradas=input("ingresa el numero de la entrada de la neurona ")
for fil,col in entradas:
#se crea las matriz de entrada
fil= OKI(input("Indique el numero de filas de la matriz de entrada"))
col=OKI(input("Indique el numero de columnas de la matriz de entrada"))
em=fil
f=-1;c=-1
acum=crea_matriz(fil,col)
print(acum)
def OKI(n):
    try:
        n=int(n)
        except:
            n=OKI(input("caracter no valido"))
            return n
#funcion para matriz
def crea_matriz(fil,col):
    f=-1;c=-1
    e_fil=[]
    f+=1
    for c in range(col):
        c+=1
        valor= input ("introduzca el componente (%d,%d):"%(f,c))
        e_col.append(e_col)
        matriz=np.array(e_fil,float)
        return matriz
        

capa_oculta=input("ingresa el numero de la capa oculta de la neurona ")
capa_salida=input("ingresa el numero la capa de salida de la neurona ")



