# -*- coding: utf-8 -*-
"""
Bucle For: Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""
from js import document     # para el dom de js
from pyscript import display

cant1, cant2, cant3, cant4 = 0,0,0,0
lista_coord = []

def enviar_coordenadas(event):
    global lista_coord, cant1, cant2, cant3, cant4
    
    try:
        # 1. cantidad de puntos a procesar
        n_str = document.getElementById("input_19_2_puntos").value
        if n_str.strip() == "":
            display("⚠️ Debe ingresar un valor", target="resultado19_2_2", append=False)
            return  
        n = int(n_str)
        document.getElementById("input_19_2_puntos").disabled = True

        # 2. leer coordenadas
        x_str = document.getElementById("input_19_2_x").value
        y_str = document.getElementById("input_19_2_y").value
        if x_str.strip() == "" or y_str.strip() == "":
            display("⚠️ Debe ingresar un valor en x o en y", target="resultado19_2_2", append=False)
            return  
        if len(lista_coord) >= n:
            display("⚠️ Ya registraste todos los puntos.", target="resultado19_2_2", append=False)
            return  
        
        x = int(x_str)
        y = int(y_str)
        lista_coord.append((x,y))   # guardo como tupla dentro de lista ej [(1, 2), (-3, 4), (0, -5)]
        document.getElementById("input_19_2_x").value = ""
        document.getElementById("input_19_2_y").value = ""
        # 4. si ya tengo n coordenadas, procesar
        if len(lista_coord) == n:
            for x,y in lista_coord:    #desempaquetado de tuplas para no comparar por posicion
                if (x > 0 and y > 0):
                    cant1 += 1
                elif (x < 0 and y > 0):
                    cant2 += 1
                elif (x < 0 and y < 0):
                    cant3 += 1
                elif (x > 0 and y < 0):
                    
                    cant4 += 1
            
            display(f"cantidad de puntos en primer cuadrante: {cant1}"     
                    f"cantidad de puntos en segundo cuadrante: {cant2}"   
                    f"cantidad de puntos en tercer cuadrante: {cant3}"   
                    f"cantidad de puntos en cuarto cuadrante: {cant4}", 
                    target="resultado19_2_2", append=False)    

    except Exception as e:
        display(f"Error debe ingresar un valor correcto..: {e}", target="resultado19_2_2" , append=False)    

def reiniciar_datos(event):
    global lista_coord, cant1, cant2, cant3, cant4
    lista_coord = []
    cant1, cant2, cant3, cant4 = 0,0,0,0
    
    document.getElementById("input_19_2_puntos").value = ""
    document.getElementById("input_19_2_x").value = ""
    document.getElementById("input_19_2_y").value = ""
    document.getElementById("input_19_2_puntos").disabled = False
    display("🔄 Datos reiniciados.", target="resultado19_2_2", append=False)
