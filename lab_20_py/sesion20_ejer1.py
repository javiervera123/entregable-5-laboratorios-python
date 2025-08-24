# -*- coding: utf-8 -*-
"""Parte 1: Declaración Básica de Funciones
- Escribe una función llamada `bienvenida` que tome un nombre como parámetro y salude a
la persona por su nombre.
- Escribe una función llamada `area_circulo` que tome el radio de un círculo como parámetro
y retorne su área. Usa la fórmula: área = π * radio^2 (puedes usar `math.pi`).
return math.pi * radio ** 2 # realizo la formula
"""

#funcion sin parámetros
from pyscript import document, display
def bienvenida(event):
    nombre = (document.getElementById("nombre").value) #guardo  el valor ingresao del usuario por input 

    #print(f"Hola {nombre}, es un placer tenerte por aquí...")
    display(f"Hola {nombre}, es un placer tenerte por aquí...",target="saludo", append=False)
    #target nos permite mostrar por nuestra etiqueta p y append=false para que muestre un sólo valor

#punto 2 ------------------------  
import math
from pyscript import document, display

#1. defino función.
def area_circulo(radio):      
     return math.pi * (radio**2)

#4.salida por consola
#print(f"el área del círculo es {salida:.2f}")
#salida por navegador
def mostrar(event):
    try:
        # entrada
        radio=float(document.getElementById("radio").value)   

        salida =area_circulo(radio)
        # salida
        display(f"El área del círculo es {salida:.2f}", target="salida", append=False)
    except ValueError:
        display("Por favor ingresa un número válido.", target="salida", append=False)