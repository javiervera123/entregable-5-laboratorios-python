""" concatenación de cadenas
sesion 18
Manipulación de Cadenas:
- Crea dos variables `string` y concaténalas para formar una frase completa.
- Captura por teclado los textos de las frases
frase1=input(“Ingrese la frase 1:”)
- Usa f-strings para crear una frase similar. """
# entrada
mensaje1 = input("Ingrese un mensaje : ")
mensaje2 = input("Ingrese segundo mensaje: ")

# proceso de concatenar con +
resul_concatenacion =  mensaje1+ " " + mensaje2
print("Concatenación con signo + :", resul_concatenacion)

#salida
# Usar f-string para crear una frase similar
mensaje_fstring = (f"{mensaje1} {mensaje2}")
print("Usando f-string      :", mensaje_fstring)
# o podemos
print(f"unión de los dos mensajes {mensaje1}{mensaje2}")



