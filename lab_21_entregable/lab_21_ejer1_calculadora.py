from js import document
from pyscript import display

def suma(a,b):
    return (a+b)

def resta(a,b):
    return (a-b)

def multiplicacion(a,b):
    return (a * b)

def division(a,b):
    if b ==0:
        display ("la división no se puede realizar !",target = "resultado21_1", append=False)
        return None
    return (a/b)
def calcular_operacion(event):
    try:
        num1_str= (document.getElementById("num1_calculadora").value.strip())
        num2_str= (document.getElementById("num2_calculadora").value.strip())
        operacion = document.getElementById("operacion").value
        if num1_str =="" or  num2_str=="":
            display("Falta ingresar uno de los 2 números", target="resultado21_1", append=False)
            return
        num1 = int(num1_str)
        num2 = int(num2_str)
   
        if (operacion == "suma"):
          resultado = suma(num1,num2)
          display(f"la suma es: {resultado}", target="resultado21_1", append=False)
        elif (operacion == "resta"):
           resultado = resta(num1,num2)
           display(f"resultado de la resta es: {resultado}",target="resultado21_1", append=False)
        elif (operacion == "multiplicacion"):
          resultado = multiplicacion(num1,num2)
          display(f"resultado de la multiplicacion: {resultado}",target="resultado21_1", append=False)
        elif (operacion == "division"):
          resultado = division(num1, num2)
          display(f"resultado de la división: {resultado:,.2f}",target="resultado21_1", append=False)    
    except ValueError:
        display("Otra clase de error ...", target="resultado21_1", append=False)

def limpiar_21_1(event):       
    document.getElementById("num1_calculadora").value = ""
    document.getElementById("num2_calculadora").value = ""
    display("", target="resultado21_1", append=False)