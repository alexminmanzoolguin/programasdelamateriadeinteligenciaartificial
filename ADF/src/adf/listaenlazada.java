/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package adf;

/**
 *
 * @author alex_
 */
public class listaenlazada {
    // Nodo Inicial
	private Nodo inicio;
	// Nodo Final
	private Nodo fin;

	// Constructor de la clase
	public listaenlazada () {
		this.inicio = null;
		this.fin = null;
	}
        // Crea la lista a partir de un arreglo de valores
	public void crearSimple ( int[] valores ) {
		// por cada elemento del arreglo crea un nodo
		for (int n : valores) {
			// Nuevo objeto nodo
			Nodo nuevoNodo = new Nodo( n );
			
			if ( this.inicio == null ) {
				// Si la lista esta vacia, crea una nueva
				this.inicio = nuevoNodo;
				this.fin = nuevoNodo;
			} else {
				// Si la lista existe el ultimo elemento es apuntado al nuevo nodo
				this.fin.setSiguiente( nuevoNodo );
				// El nuevo nodo toma la posicion del ultimo elemento en las variables
				this.fin = nuevoNodo;
			}
		}
	}

	// retorna la lista de forma ordenada
	public void retornaLista () {
		Nodo recorre = this.inicio;
		while ( recorre != null ) {
			System.out.println( recorre.getValor() );
			recorre = recorre.getSiguiente();
		} 
	}
}
