# -*- coding: utf-8 -*-
"""
Parte 2: Funciones con Parámetros por Defecto
- Escribe una función llamada `descuento` que tome el precio de un producto y un
porcentaje de descuento. La función debe retornar el precio final después de aplicar el
descuento. Si no se proporciona el porcentaje de descuento, debe asumir que es 10%.
precio=int(input("Ingrese el precio: "))
"""
from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display
#paso 1. defino mi funcion
def descuento(precio, porc=10): #si el usuario n pasa desc, se le asigna 10 automática/m
        descuento = (precio * porc) /100  # aplicamos en desc del 10 %
        precio_final = precio - descuento        
        return precio_final
def limpiar_datos_20_2():   
      document.getElementById("input_20_2_precio").value = ""
      document.getElementById("input_20_2_descuento").value = ""
   #termina funcion limpiar-datos
def mostrar_descuento(event):
        #pas 2. entrada// pido datos valido que precio no esté vacío, desc si puede estar vacío
    precio_str = document.getElementById("input_20_2_precio").value.strip()# strip eliminna espacio vacios
    porc_str= (document.getElementById("input_20_2_descuento").value.strip())
    if (precio_str ==""):
      display("Ingrese precio !",target ="resultado20_2" , append=False)
      return
    try:
        precio = float(precio_str)
    except ValueError:
        display("El precio debe ser un número válido.", target="resultado20_2", append=False)
        return

    # Si no se ingresó descuento, usar el valor por defecto (10)
    if porc_str == "":
        porc = 10
    else:
        try:
            porc = float(porc_str)
        except ValueError:
            display("⚠️ El descuento debe ser un número válido.", target="resultado20_2", append=False)
            return
    
    #paso 3. llamo a mi funcion 
    precio_final =descuento(precio,porc)
    #paso 4. salida // muestro por consola // depurar.
    display(f"precio inicial $ {precio}, \n % de descuento {porc} %,"
      f"\n su producto le queda en $ {precio_final:.2f}", target="resultado20_2", append=False)
    limpiar_datos_20_2()
     #termina mi funcio mostrar_descuento)
