# -*- coding: utf-8 -*-
"""
Parte 3: Diccionarios
- Crear un diccionario que almacene los nombres de tres estudiantes y sus respectivas
calificaciones. Escribir un programa que imprima el nombre del estudiante con la calificación
más alta.
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación
de {calificaciones[nombre_max]}.")

def funcion_diccionario_notas(calificaciones):
    # Calcula el nombre con la nota más alta usando el valor (nota) como clave de comparación
    nombre_max = max(calificaciones, key=calificaciones.get)
    # Devuelve el nombre ganador y su nota
    return nombre_max, calificaciones[nombre_max]
   
# 2. entradas //pedir datos
dic_estudiantes = {
                    "José": 3.0,
                    "Javier": 4.0,
                    "Maria": 4.9
                    }
#dic_estudiantes =  str(input("Ingrese nombre primer estudiante" ))

# 3. proceso //llamar a la función
nombre, nota_alta =  funcion_diccionario_notas(dic_estudiantes)

#s 4. salida // imprimir
print(f"El estudiante con la calificación más alta es {nombre} con una calificación"
      f"de {nota_alta}.")
"""# -*- coding: utf-8 -*-
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display

dic_estudiantes = {}    #defin mi diccionario
contador = 0            #contador global
#funcio de obtener el mayor valor
def funcion_diccionario_notas(calificaciones):
    nombre_max = max(calificaciones, key=calificaciones.get) # key= se usa como criterio de comparación.
    return nombre_max, calificaciones[nombre_max]             #.get =dado un nombre (clave), devuelve su nota (valor).

def agregar_estudiantes(event):
    global dic_estudiantes, contador

    if contador >= 3:
        display("⚠️ Ya ingresaste los 3 estudiantes.", target="resultado19_3", append=False)
        return

    nombre = document.getElementById("input_19_3_nombre").value
    nota_str = document.getElementById("input_19_3_calificacion").value

    if nombre.strip() == "" or nota_str.strip() == "":  #compara validando que si  está vacío muestre mensaje
        display("⚠️ Debe ingresar nombre y calificación.", target="resultado19_3", append=False)
        return
    
    nota = float(nota_str)
    dic_estudiantes[nombre] = nota  #agrego nota a la clave nombre
    contador += 1                   #incremento el contador

    # limpiar inputs
    document.getElementById("input_19_3_nombre").value = ""
    document.getElementById("input_19_3_calificacion").value = ""

    if contador < 3:
        display(f" {nombre} agregado con nota {nota} (total: {contador}/3)",target="resultado19_3", append=False)
    else:
        # Al llegar a 3, mostrar directamente el resultado 
        nombre_max, nota_alta = funcion_diccionario_notas(dic_estudiantes)
        display(f" El estudiante con la nota más alta es {nombre_max} con {nota_alta}",
                target="resultado19_3", append=False)

def reiniciar_datos(event):
    global dic_estudiantes, contador
    dic_estudiantes = {}
    contador = 0
    document.getElementById("input_19_3_nombre").value = ""
    document.getElementById("input_19_3_calificacion").value = ""
    display("🔄 Datos reiniciados.", target="resultado19_3", append=False)

def boton_imprimir_estudiantes(event):
    if not dic_estudiantes:
        display("⚠️ No hay datos para imprimir.", target="resultado19_3", append=False)
        return
    nombre_max, nota_alta = funcion_diccionario_notas(dic_estudiantes)
    lista_salida=[]
    # Agregar todos los estudiantes al reporte
    for nombre, nota in dic_estudiantes.items():
        lista_salida.append(f"{nombre}: {nota}\n")

    lista_salida.append("---------------------------------\n")
    lista_salida.append(
        f"El estudiante con la nota más alta es {nombre_max} con {nota_alta}\n"
    )
    
    contenido = "".join(lista_salida)   #une todos los elementos de la lista lista_salida en un solo string
     # Mostrar también en pantalla
    display(contenido.replace("\n", "<br>"), target="resultado19_3", append=False)

    blob = Blob.new([contenido], { "type": "text/plain" })
    url = URL.createObjectURL(blob)

    link = document.createElement("a")
    link.href = url
    link.download = "reporte_estudiante_nota_alta.txt"
    link.click()
