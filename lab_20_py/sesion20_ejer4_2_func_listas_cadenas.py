# -*- coding: utf-8 -*-
"""
•ejer 4 punto 2 Escribir una función que reciba una lista de string y nos retorne el que 
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que
tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))

"""
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display
lista_palabras =[]

def funcion_lista_cadena(palabras):
    pos = 0
    for i in range(len(palabras)):
        if len(palabras[i]) > len(palabras[pos]):
            pos = i
        elif len(palabras[i]) == len(palabras[pos]) and palabras[i] < palabras[pos]: #compara cadenas
            pos = i
    return palabras[pos]
"""el elif se puede trabajar así
    resultado = max(palabras, key=lambda p: (len(p), p))
    print("Palabra con más caracteres (desempate alfabético):", resultado)
"""
def ingresar_str_20_4_2(event):
    try:
        palabras = document.getElementById("input_20_4_2_str").value
        # Verificar que no esté vacío y que contenga solo letras
        if not palabras.strip():
            raise ValueError("El nombre no puede estar vacío")
        if any(char.isdigit() for char in palabras):
            raise ValueError("El nombre no puede contener números")
        
        lista_palabras.append(palabras)       #agrega valores a mi lista.
        document.getElementById("input_20_4_2_str").value =""
    except ValueError as e:
        # Mostrar el error 
        display(str(e), target="resultado20_4_2", append=False)

def calcular_20_4_2(event):
     mas_caracteres = funcion_lista_cadena(lista_palabras)
     display(f"las palabras ingresadas son: {lista_palabras} "
    f"\nPalabra con más caracteres: {mas_caracteres}", target ="resultado20_4_2", append=False)

def limpiar_20_4_2(event):
    lista_palabras.clear() # o listas_palabras=[]
    document.getElementById("input_20_4_2_str").value =""
    document.getElementById("resultado20_4_2").innerHTML = ""