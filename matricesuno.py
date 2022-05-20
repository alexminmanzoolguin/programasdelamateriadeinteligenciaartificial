#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random
import sys
print("BIENVENIDO AL GRUPO 8S12")
print("MANZO OLGUIN ALEX YAZMIN 7S12")
#inciamos pa parte grafica de nuestra neurona
entradas=int(input("ingresa el numero de la entrada de la neurona "))
for e in range(entradas):
    filas=int(input("Introduce numeros de filas:"))
    columnas=int(input("Introduce numeros de comumnas:"))
for i in range(filas):
    print(random.random())
    for j in range(columnas):
        print(random.random())

ocultas=int(input("ingresa el numero de capas ocultas de la  neurona"))
for o in range(ocultas):
    filas1=int(input("Introduce numeros de filas:"))
    columnas1=int(input("Introduce numeros de comumnas:"))
for i in range(filas1):
    print(random.random())
    for j in range(columnas1):
        print(random.random())
salidas=int(input("ingresa el numero de capas ocultas de la neurona"))
for s in range(salidas):
    filas2=int(input("Introduce numeros de filas:"))
    columnas2=int(input("Introduce numeros de comumnas:"))
for i in range(filas2):
    print(random.random())
    for j in range(columnas2):
        print(random.random())
