"""4. Parte 4: Conjuntos
- Crea dos conjuntos con números enteros.
- Realiza la unión e intersección de ambos conjuntos.
- Muestra en pantalla el resultado de la intersección.
interseccion= Conjunto1 & Conjunto2"""

#creamos 2 listas
conj1 ={1,2,3,4,5,6,7,8,9,10}
conj2 ={56,32,3,5,9,100,200}

interseccion =conj1 & conj2
union = conj1 | conj2
print("conjunto 1: ",conj1)
print("conjunto 2: ",conj2)
print ("en la intersección de conjuntos son los sgtes: ",interseccion)
print ("en la unión de conjuntos son los sgtes: ",union)