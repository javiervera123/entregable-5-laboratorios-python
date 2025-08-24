# -------------------------------------------------------------
# - Escribir un programa que pida ingresar por teclado un número positivo de uno, dos o tres
#dígitos (1..999) mostrar un mensaje indicando si el número tiene uno, dos o tres dígitos.
from js import document
from pyscript import display

def conteo_digitos(n):
    if(n >=1 and n <10 ):       mensaje = (f" {n} tiene 1 dígito")   
    elif(n >=10 and n <100 ):   mensaje = (f" {n} tiene 2 dígitos") 
    elif(n >=100 and n <1000 ): mensaje = (f" {n} tiene 3 dígitos") 
    else:                       mensaje = (f" {n} o  es negativo, o está fuera de rango")
    return mensaje

def mostrarDatosPrincipal19_1_2(event):
    try:
        #entrada por formulario
        n = int(document.getElementById("input_19_1_2").value)

        #llamo a la función 
        mensaje = conteo_digitos(n) 
        #salida por display de py-script en la etiqueta p
        display(f"El número: {mensaje}", target="resultado19_1_2", append=False)
    except Exception as e:
        display(f"Error debe ingresar un valor..: {e}", target="resultado19_1_2", append=False)
