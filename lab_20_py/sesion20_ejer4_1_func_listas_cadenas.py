# -*- coding: utf-8 -*-
"""
•ejer 4 punto 2 Escribir una función que reciba una lista de string y nos retorne el que 
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que
tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
"""
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

#paso2 pedir datos //entrada
#creamos lista vacía para pedir datos al usuario
lista_palabras =[]
opc ="si"
cont = 1     #cont para decirle al usuario cuántos números lleva
while (opc == "si"):
    palabras = input(f"ingrese palabra {cont} a la lista para comparar cúal tiene más caracteres.. ")
    lista_palabras.append(palabras)       #agrega valores a mi lista.
    opc = input("desea agregar más valores? si/no  ").lower()
    cont += 1   #increment contador
#paso3 llamamos a la función
mas_caracteres = funcion_lista_cadena(lista_palabras)

#paso 4. mostrar // salida
print(f"Palabra con mas caracteres: {mas_caracteres}")