# -*- coding: utf-8 -*-
"""
Parte 1: Condicionales
- Escribir un programa que solicite al usuario un número por teclado y determine si es par o
impar. Mostrar un mensaje adecuado en cada caso.
"""
from js import document
from pyscript import display


def funcion_par_impar(n):
    if(n % 2 ==0):
        resultado = ("ES  PAR")   
    else:
        resultado = ("ES  IMPAR")  
    return resultado

def mostrarDatosprincipal19_1(event):
    try:
        n = int(document.getElementById("input_19_par").value)

        resultado = funcion_par_impar(n)  

        display(f"El número {n},  {resultado}", target="resultado19_1", append=False)        
 
    except ValueError as e:
                display(f"Por favor ingresa un dato válido. Error: {e}", target="resultado19_1", append=False)
    except Exception as e:# otro error
                display(f"Por favor ingresa un dato válido. error{e}", target="resultado19_1", append=False)
    
    