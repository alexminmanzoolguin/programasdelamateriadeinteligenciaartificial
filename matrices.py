import numpy as np
from numpy import random as rd
import sys
class topologia:
    def __init__(self, num_nodos,matriz_o,matriz_n):
        self.num_nodos=num_nodos
        self.matriz_o=matriz_o
        self.matriz_n=matriz_n

        
def crear_matrices(renglones,columnas):
     if len (renglones[0])== len (columnas):
        renglones =rd.randint(0,2,(5,5))
columnas=rd.randint(0,2,(5,5))
matriz_re=[]
for i in range(len(renglones)):
    matriz_re.append([])
    for j in range(len(columnas)):
        valor=float(input("fila{},columna{}:".format(sin((rand()%181)/180))))
        matriz_re[i].append(valor)
print()
for fila in matriz_re:
    print("[",end="")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
        print()
    
#funcion de red neurona
        def topologia(aux,tem):
            num_capas_ocul=int(input("numero de capas ocultas:"))
            aux= sys.getsizeof(topologia)*(num_capas_ocult+2)

            for i in range(num_capas_ocult):
                           i= i + (num_capas_ocult+2)
                           if i==0:
                            print("capa de entrada")
                            else {
                                if i== num_capas_ocult:
                                print("Capa salida")
                                else
                                print("capa oculta")
                                
        print("numero de neuronas")
tem=int(input("numero de neuronas:"))

(aux+i)-> num_nodos=tem;

for i in range(num_capas_ocult+2):
	
		if i==0
			(aux+i)->matriz_o=NULL;
		else
		
			(aux+i)->matriz_o=crea_matriz((aux+i)->num_nodos,(aux+i-1)->num_nodos);
			(aux+i)->matriz_n=crea_matriz((aux+i)->num_nodos,(aux+i-1)->num_nodos);

	    
	

        
            
