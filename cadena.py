#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import sys
sys.float_info.epsilon
#introducir la matriz de entada o input
print("introducir la matriz de entada o input")
filas=int(input("Introduce numeros de filas:"))
columnas=int(input("Introduce numeros de comumnas:"))
matriz_in=[]
for i in range(filas):
    matriz_in.append([])
    for j in range(columnas):
        valor=float(input("fila{},columna{}:".format(i+1, j+1)))
        matriz_in[i].append(valor)
print()
for fila in matriz_in:
    print("[",end="")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
        print()
INPUT_X = np.array(matriz_in)
print ("INPUT_X:\n", INPUT_X)

#introducir la matriz hidden
print("introducir la matriz hidden")
hi=int(input("introduce el numero de capas ocultas:"))
lim_hi=int(input("introduce el limite:"))

for hi in range (lim_hi):
   hi= hi + lim_hi
       
filas_hi=int(input("Introduce numeros de filas:"))
columnas_hi=int(input("Introduce numeros de comumnas:"))
matriz_hi=[]
for i in range(filas_hi):
    matriz_hi.append([])
    for j in range(columnas_hi):
        valor=float(input("fila{},columna{}:".format(i+1, j+1)))
        matriz_hi[i].append(valor)
    
print()
for fila in matriz_hi:
    print("[",end="")
    for elemento  in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
        print()
print()

  
#introducir la matriz resultado
print("introducir la matriz salida")

filas_re=int(input("Introduce numeros de filas:"))
columnas_re=int(input("Introduce numeros de comumnas:"))
matriz_re=[]
for i in range(filas_re):
    matriz_re.append([])
    for j in range(columnas_re):
        valor=float(input("fila{},columna{}:".format(i+1, j+1)))
        matriz_re[i].append(valor)
print()
for fila in matriz_re:
    print("[",end="")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
        print()

 
   
#multiplicacion de matrices entrada con hidden
   
        def multiplicar_matrices(matriz_in,matriz_hi):
            if len (matriz_in[0])== len (matriz_hi):
                matriztotal=[]
                for i in range(len(matriz_in)):
                    matriztotal.append([])
                    for j in range (len(matriz_hi[0])):
                        matriztotal[i].append(0)
                for i in range(len(matriz_in)):
                    for j in range(len(matriz_hi)):
                        for k in range(len(matriz_in[0])):
                            matriztotal[i][j] += matriz_in[i][k]*matriz_hi[k][j]
                            
                        return matriztotal
                    else:
                        return None
                    c=multiplicar_matrices(matriz_in,matriz_hi)
                    if c==None:
                        print("[",end="")
                        for elemento in fila:
                            print(elemento,end="")
                            print("]")
                          
                             
#caculo de matriz hideen
print("suma de la matriz ")

for i in range(filas_hi):
    suma=sum(matriz_hi[i])
    matriz_hi[i].append(suma)
    print(suma)


print("aplicar la funcion sigmoide")
  
for s in range(filas_hi):
    simm=1/(1 + np.exp(-(suma)))
    matriz_hi[s].append(simm)
    print(simm)
   

#calculo de multiplicacion resultado
    
print("multiplicacion de matrices ")
 def multiplicar_matrices(matriz_re,matriz_hi):
            if len (matriz_re[0])== len (matriz_hi):
                matriztotal1=[]
                for i in range(len(matriz_re)):
                    matriztotal1.append([])
                    for j in range (len(matriz_hi[0])):
                        matriztotal1[i].append(0)
                for i in range(len(matriz_re)):
                    for j in range(len(matriz_hi)):
                        for k in range(len(matriz_re[0])):
                            matriztotal1[i][j] += matriz_in[i][k]*matriz_hi[k][j]
                            
                        return matriztotal
                    else:
                        return None
                    c=multiplicar_matrices(matriz_re,matriz_hi)
                    if c==None:
                        print("[",end="")
                        for elemento in fila:
                            print(elemento,end="")
                            print("]")

#aplicar la funcion sigmoide
       print("aplicar la funcion sigmoide")
for t in range(filas_hi):
    simtol=1/(1 + np.exp(-())
    mul_hi[t].append(simtol)
    print(simtol)


#metodo de entrenamiento
eps= 2.220446049250313e-16
i=0
w(i)=print(fila_hi)
totalpesos= print(w(i))
              if i< totalpesos:
totalpesos= totalpesos + eps
              if totalpesos=> w(i)
              print(w(i))
              i=i+1
              w=w(i+1)
              else
              totalpesos= totalpesos -2*eps
             if totalpesos=> w(i)
             print(w(i))
             else
             totalpesos= totalpesos + 2*eps
              else
              print("fin")

    
#eps = 1.0
#while eps + 1 > 1:
    #eps /= 2
#eps *= 2
#print("The machine precision is:", eps)
    

    

  
