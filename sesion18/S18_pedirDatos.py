# -*- coding: utf-8 -*-
# esto es un comentario

import math
from pyscript import document, display

#salida por navegador
def mostrarDatos1(event):
    try:
        # entrada
        nombre=(document.getElementById("nombre").value)   
        edad = int(document.getElementById("edad").value) 
        esEstudiante =(document.getElementById("estudiante").value).lower()=="si"
        calificacion = float(document.getElementById("calificacion").value)

        # salida
        display((f"su nombre es {nombre},"
                f" tiene {edad} años, "
                f"usted es estudiante: {esEstudiante} y "
                f" su calificacion es {calificacion}"), target="resultado18_1", append=False)
    except ValueError as e:
        display("Por favor ingresa un dato válido.", target="resultado18_1", append=False)
    except Exception as e:# otro error
        display("Por favor ingresa un dato válido.{e}", target="resultado18_1", append=False)
 

     
     