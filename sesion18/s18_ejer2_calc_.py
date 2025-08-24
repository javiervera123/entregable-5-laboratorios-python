# -*- coding: utf-8 -*-
"""
Funciones para las 4 operaciones matemáticas
"""
# Entrada, valores numericos para hacer las operaciones math
""" Cuando traabajamos con funciones, primero debemos 
1.crear las funciones
2. crear las entradas(los datos del usuario)
3. llamamos a las funciones y se las asignamos a las variables
4. las salidas(mostramos por consola)
"""
from pyscript import document, display

def funcion_suma(num1, num2):     
    return num1 + num2
def funcion_resta(num1, num2):
    return num1 - num2
def funcion_multiplicacion(num1, num2):
    return  num1 * num2
def funcion_division(num1, num2):
    if(num2 !=0) : 
        return num1 / num2
    else:  document.getElementById("resultado18_2").innerText = "⚠️ No es posible hacer la división"
    return None



def mostrarDatos2(event):
    num1 = int(document.getElementById("n1").value)  
    num2 = int(document.getElementById("n2").value) 

    suma = funcion_suma(num1,num2)
    resta =funcion_resta(num1,num2)
    multiplicacion =funcion_multiplicacion(num1, num2)
    division = funcion_division(num1, num2) 

    display(f"mostramos las 4 operaciones matemáticas: suma {suma} resta {resta} "
            f"multiplicacion {multiplicacion} division: {division}", target="resultado18_2", append=False)
 