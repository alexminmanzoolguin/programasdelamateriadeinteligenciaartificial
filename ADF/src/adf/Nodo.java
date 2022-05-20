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
class Nodo {
   private final int valor;
	private Nodo siguiente;
	public Nodo ( int valor ) {
		this.valor = valor;
	}
	public void setSiguiente (Nodo sig) {
		this.siguiente = sig;
	}
	public int getValor () {
		return this.valor;
	}
	public Nodo getSiguiente () {
		return this.siguiente;
	} 
}
