# -*- coding: utf-8 -*-
"""Parte 4: Combinación de Estructuras
- Escribir un programa que permita al usuario ingresar el nombre de un estudiante y su
calificación. Si el estudiante ya existe en el diccionario, actualizar la calificación; si no existe,
agregarlo al diccionario. Finalmente, mostrar todos los estudiantes y sus calificaciones.
""" 
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display
# Variables globales inicializadas
estudiantes = {}
nombre = ""
calificacion = 0.0

def actualizar_dicc(nombre, calificacion, estudiantes):
    
    if nombre in estudiantes:  #comparamos si nombre está en el dicc estudiantes
        estudiantes[nombre] = calificacion #si es verdadero modifica el valor a esta clave-valor
    else:
       estudiantes[nombre] = calificacion  #si es falso agrega nueva clave-valor
             
    return estudiantes
    #termina funcionactualizar
def guardar_mostrar(event):
    
    nombre_str = document.getElementById("input_19_4_nombre").value.strip() #valida que no venga vacio .strip
    calificacion_str = document.getElementById("input_19_4_calificacion").value.strip()
        # Validación, el nombre o calificcion no esté vacío
    if not nombre_str or not calificacion_str:   
            display("El nombre y/o calificación, no puede estar vacío",
                target="resultado19_4", append=False)
            return
    try:    
        calificacion = float(calificacion_str)
        nombre = nombre_str
    except ValueError:
        display("⚠️ La calificación debe ser un número válido",
                target="resultado19_4", append=False)
        return
       
    
     # actualizar diccionario llamando a la funcion
    actualizar_dicc(nombre, calificacion, estudiantes)
   
    # mostrar resultados
    if not estudiantes:
     display("No hay estudiantes en el diccionario...",
            target="resultado19_4", append=False)
    else:        #de lo contrario"""
        display("📋 Lista de estudiantes:", target="resultado19_4", append=True)
    for n, nota in estudiantes.items():
        display(f"{n}: {nota}", target="resultado19_4", append=True)
          # limpiar inputs
    document.getElementById("input_19_4_nombre").value = ""
    document.getElementById("input_19_4_calificacion").value = ""  
    #termina funcion guardar_mostrar

def reiniciar_datos_4(event):
    global dic_estudiantes, contador
    estudiantes = {}
    
    document.getElementById("input_19_4_nombre").value = ""
    document.getElementById("input_19_4_calificacion").value = ""
    display("🔄 Datos reiniciados.", target="resultado19_4", append=False)

def boton_imprimir_estudiantes_4(event):
    global estudiantes

    if not estudiantes:
        display("⚠️ No hay datos para imprimir.", target="resultado19_4", append=False)
        return

    lista_salida = []

    # Agregar todos los estudiantes al reporte
    for n, nota in estudiantes.items():
        lista_salida.append(f"{n}: {nota}\n")

    lista_salida.append("---------------------------------\n")

    # Unir la lista en un solo string
    contenido = "".join(lista_salida)

    # Mostrar también en pantalla (con saltos de línea HTML)
    display(contenido.replace("\n", "<br>"), target="resultado19_4", append=False)

    # Crear archivo descargable
    blob = Blob.new([contenido], { "type": "text/plain" })
    url = URL.createObjectURL(blob)

    link = document.createElement("a")
    link.href = url
    link.download = "reporte_Diccionario_actualizado.txt"
    link.click()


   

  

   