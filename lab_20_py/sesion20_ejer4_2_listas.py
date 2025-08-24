# -*- coding: utf-8 -*-
"""
Parte 4: Parámetros de tipo lista
• Escribir un programa que defina por asignación una lista de 6 enteros en el bloque
principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la
suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la
última recibe la lista y retorna el menor.
suma=suma+lista[x]

"""
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
    
#creamos lista vacía para pedir datos al usuario
lista =[]
opc ="si"
cont = 1     #cont para decirle al usuario cuántos números lleva
while (opc == "si"):
    num = int(input(f"ingrese numero {cont} a mi lista .. "))
    lista.append(num)       #agrega valores a mi lista.
    opc = input("desea agregar más valores? si/no  ").lower()
    cont += 1   #increment contador
  

print(f"los valores de mi lista:  {lista}")
print(f"la suma de mi lista es : {funcion_suma(lista)}")
print(f"el mayor de mi lista es : {funcion_mayor(lista)}")
print(f"el menor de mi lista es : {funcion_menor(lista)}")
