"""1. Parte 1: Variables y Operaciones
- Crea dos variables, una de tipo entero y otra de tipo float.
- Realiza una operación matemática (suma, resta, multiplicación o división) entre ambas y muestra el resultado en pantalla.
resultado=entero+45"""
try:
    cant= int(input("Ingrese cantidad de productos a comprar: "))
    precio= float(input("Ingrese el precio del producto "))
    pagar= cant * precio

    print(f"el precio del producto es: {precio}, la cantidad fueron: {cant}, "
      f"el valor a pagar es: {pagar:.2f}")
except ValueError:
        print("Por favor ingresa un número válido.")

#punto 2 
lista_frutas=["pera","banano","uva","Manzana","pera"]
lista_frutas.append("mango")
print("mi lista de frutas es: ",lista_frutas)
print("mi lista de frutas es: ",lista_frutas[2])
