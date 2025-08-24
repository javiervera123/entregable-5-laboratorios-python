# -*- coding: utf-8 -*-
"""
Parte 4: Parámetros de tipo lista
• Escribir un programa que defina por asignación una lista de 6 enteros en el bloque
principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la
suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la
última recibe la lista y retorna el menor.
suma=suma+lista[x]     
"""
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display
lista = []
def funcion_suma(lista):
    suma = 0
    for i in range(len(lista)):  # len me trae el tamaño de la lista        
        suma += lista[i]        
    return suma 
def funcion_mayor(lista):
    mayor= lista[0]
    for i in range(1,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
""" opcional o mejor opcion
def funcion_mayor(*numeros):
    return mayor(numeros)"""

def funcion_menor(lista):
    menor= lista[0]
    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor
""" opcional o mejor opcion
def funcion_menor(*numeros):
    return menor(numeros)"""
    
def ingresar_numeros_20_4_1(event):
    num = int(document.getElementById("input_20_4_numero").value.strip())
    lista.append(num) 
    document.getElementById("input_20_4_numero").value=""
    
def calcular_20_4_1(event):
    menor = funcion_menor(lista)
    mayor = funcion_mayor(lista)
    suma = funcion_suma(lista)   
    
    display(f"los valores de mi lista:  {lista}", target ="resultado20_4_1", append=True)
    display(f"la suma de mi lista es : {suma }", target ="resultado20_4_1", append=True)
    display(f"el mayor de mi lista es : {mayor}", target ="resultado20_4_1", append=True)
    display(f"el menor de mi lista es : {menor}", target ="resultado20_4_1", append=True)

def limpiar_20_4_1(event):
    lista = []
    menor, mayor, suma =0,0,0
    document.getElementById("input_20_4_numero").value = ""
    document.getElementById("resultado20_4_1").innerHTML = ""