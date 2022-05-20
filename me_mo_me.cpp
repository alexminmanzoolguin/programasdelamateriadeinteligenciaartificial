#include<stdio.h>
#include <iostream>
#include<stdlib.h>
#include<conio.h>
#include<windows.h>
using namespace std;

int main(int argc, char *argv[]) {
	
	int cadena,i,j,numeros[20],opcion,auxiliar[20],numero,posicion,mayor,posicionmayor;
	float suma;
	
	printf("\n BIENVENIDOS AL GRUPO 8S12:D");
	printf("\n Ingrese el numero de caracteres:");
	scanf("%d",& cadena);
	printf("\n Ingrese los numeros:");
	for(i=0;i<cadena;i++){
		printf("\n");
		printf("%d digito:",i+1);
		scanf("%d",&numeros[i]);
	}
	
	printf("\n Los numeros ingresados son");
	for(i=0;i<cadena;i++) {
		printf(" %d",numeros[i]);
	}
	
	
	printf("\n");
	do{
		printf( "\n   1. Calcular la moda del los numeros.");
		printf( "\n   2. calcular la media de los numeros");
		printf( "\n   3. Calcular la mediana de los numeros");
		printf( "\n   4. Salir." );
		printf( "\n\n   Introduzca opcion(1-4): " );
		
		scanf( "%d", &opcion );
		switch ( opcion )
		{
			
		case 1:
			// Rellenamos el vector auxiliar inicializandolo a valores 0
			for(i=0;i<cadena;i++) {
				auxiliar[i]=0;
			}
			// Recorrer el vector comprobando las repeticiones de cada numero
			// y almacenando las mismas en el vector auxiliar segun la posicion
			// del numero
			for(i=0;i<cadena;i++) {
				numero = numeros[i];
				posicion = i;
				for(j=i;j<cadena;j++) {
					if(numeros[j]==numero) auxiliar[posicion]++;
				}
			}
			// Una vez establecidas las repeticiones de cada numero se ha de establcer
			// cual es la posicion del vector que tiene un numero de repeticiones mayor
			// ya que esta es la posicion que se corresponde con el numero que se repite
			// mas veces el vector ( MODA )
			// se establece en primer lugar el mayor como el primer elemento del vector
			mayor=auxiliar[0];
			posicionmayor = 0;
			for(i=0;i<cadena;i++) {
				if(auxiliar[i]>mayor) {
					posicionmayor=i;
					mayor=auxiliar[i];
				}
			}
			// Visualizar el elemento con mas frecuencia de aparicion
			printf("\nLa moda de los numeros es: %d",numeros[posicionmayor]);
		break;
		
		case 2: 
		
			suma = 0;
			for(i=0;i<cadena;i++) {
				suma+=numeros[i];
			}
			printf("\n La media de los numeros es: %.2f\n",suma/cadena);
			
		break;
		
		case 3:
			for (i = 0;i < cadena; i++){
				
				for (j = 0; j< cadena-1; j++){
					if (numeros[j] >numeros[j+1]){ // Ordena el array de mayor a menor, cambiar el "<" a ">" para ordenar de menor a mayor
						numero = numeros[j]; 
						numeros[j] = numeros[j+1]; 
						numeros[j+1] = numero;
					}
				}
			}
			printf("\n Los numeros  ordenados son");
			for(i=0;i<cadena;i++) {
				printf(" %d",numeros[i]);
			}
			
			// Dependiendo de si el numero d elementos del vector es par o impar
			// la mediana ha de ser el punto central del mismo o los dos puntos centrales
			// del mismo.
			if(cadena%2!=0) {
				printf("\nEL valor de la mediana es : %d",numeros[cadena/2]);
			} else {
				printf("\nEL valor 1 de la mediana es : %d",numeros[cadena/2]);
				printf("\nEL valor 2 de la mediana es : %d",numeros[(cadena/2)-1]);
			}
		break;
		}
		
	} while(opcion != 4);
	return 0;
}

