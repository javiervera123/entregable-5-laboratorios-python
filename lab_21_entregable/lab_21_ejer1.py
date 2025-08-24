from js import document
from pyscript import display

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b ==0:
        display ("la división no se puede realizar !",target = "resulatdo21_1", append=False)
        return none
    return a/b
def calcular_operacion(event):
    num1= float(document.getElementById("num1_calculadora").value.strip())
    num2= float(document.getElementById("num2_calculadora").value.strip())

def limpiar_21_1(event):
    num1, num2 =0,0
    num1_calculadora =0
    num2_calculadora =0
    operacion= ""
    
    document.getElementById("num1_calculadora").value = ""
    document.getElementById("num2_calculadora").value = ""
    display("", target="resultado21_1", append=False)