 /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package adf;

import java.util.Scanner;

/**
 *
 * @author alex_
 */
public class ADF {

    

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       
        ADF adf1=new ADF();
        adf1.cinta();
        adf1.funciondetrasmision();
        adf1.edos_finales();
        int[] arreglo_base = null;
       
    }

    private String cinta() {
         Scanner teclado=new Scanner(System.in);
         StringBuilder ala= new StringBuilder();
         System.out.println("......BIENVENIDOS AL GUPO 8S12.....");
        System.out.println("Ingresa el numero de bits de la cadena");
  int tam_cadena = teclado.nextInt();
  String numerobinario="";
  numerobinario= numerobinario+(tam_cadena%2);
  tam_cadena=tam_cadena/2;
  while(tam_cadena>=2){
      numerobinario=numerobinario+ (tam_cadena%2);
      tam_cadena=tam_cadena/2;
  }
  numerobinario= numerobinario+tam_cadena;
 StringBuilder cadena = ala.append(numerobinario);
      		cadena = ala.reverse(); 
                System.out.println(cadena);
 return null;

    }
 

    private void funciondetrasmision() {
Scanner teclado=new Scanner(System.in);
 int[] []ft = new int[4][8];
           System.out.println("Ingresa el numero de estados ");
        int num_edos= teclado.nextInt();
        
    for (int i = 0; i < ft.length; i++) {
        for (int j=0; j < ft.length ; j++){
            if (i == 0) {
                ft[i][j]=num_edos*2;
                System.out.println("numero[" + i +j+ "]= " ); 
         
                       ft[i][j] = teclado.nextInt();
                System.out.println("numero[" + i +j+ "]= "+ft[i][j]);
                }

        
    }
    }
    }
    private void edos_finales() {
      Scanner teclado=new Scanner(System.in);
     System.out.println("Ingresa el numero de estados finales");
        int num_edos_final = teclado.nextInt();
        int edo_fin = 0;
        for(int i=0;i<edo_fin;i++){
          int edosfin = i+1;
          edo_fin = num_edos_final+edosfin;
          System.out.println(edo_fin);
        }
        
        System.out.println("Conjunto de estados finales");
        for(int k=0;k<edo_fin;k++){
          int edo = 0;
            if(edo==(edo_fin+k)){
                System.out.println("La cadena es valida");
            }
        }
        boolean k = false;
        boolean num_edos_fin = false;
        if(k==num_edos_fin){
            System.out.println("la cadena no es valida");
        }
        
        
    }


}