# -*- coding: utf-8 -*-
"""
Parte 3: Uso de Funciones con Parámetros Arbitrarios
- Escribe una función llamada `mayor_valor` que acepte un número arbitrario de argumentos
y retorne el mayor valor.

"""
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display
tupla_numeros=() #defino mi tupla vacía
def mayor_valor(*tupla_numeros):
    return max(tupla_numeros) if tupla_numeros else None

    
def ingresar_numeros_20_3(event):
    global tupla_numeros
    try:
        numeros=float(document.getElementById("input_20_3_numero").value)
        tupla_numeros = tupla_numeros + (numeros,)
        display(f"Número {numeros} agregado OK", target="resultado20_3", append=False)
        document.getElementById("input_20_3_numero").value =""
    except ValueError:
        display("El valor debe ser numérico.", target="resultado20_3", append=False)

def calcular_mayor_20_3(event):
    if not tupla_numeros:
        display("No hay números ingresados.", target="resultado20_3", append=False)
        return
    mayor =mayor_valor(*tupla_numeros)
    display(f"📊 Los números ingresados son: {tupla_numeros} El mayor es: {mayor}", 
            target="resultado20_3", append=False)
    document.getElementById("input_20_3_numero").value =""



