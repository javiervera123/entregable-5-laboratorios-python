"""3. Parte 3: Diccionarios
- Crea un diccionario que almacene la información de un libro (título, autor, año de publicación).
- Agrega una clave adicional para el género literario del libro.
- Muestra en pantalla el autor del libro.
libro[“genero”]=”Aventura”
Laboratorio 22"""

libro={"titulo": "",
        "autor": "",
        "anio_publ": 0
      }
libro[3]=""  #adiciono una nueva clave
#entrada
libro["titulo"]= input("Ingrese el título del libro: ")
libro["autor"]= input("Ingrese el autor del libro: ")
libro["anio_publ"]= int(input("Ingrese el año de publicación: "))
libro["genero"]= input("Ingrese el género: ")
print("libros de programación:")
print(libro)
        
