# -*- coding: utf-8 -*-
"""
"""
 calc_def_bananas(cantidadAzucar,pesoBananas):
     #calcular o convertir a gramos
     gramosAzucar = cantidadAzucar * 1000
     #calcula cantida azucar que se desperdicia = 10%
     azucarDesperdiciada = cantidadAzucar * 10 /100
     #calcular azucar utilizable 
     azucarUtilizable = gramosAzucar - azucarDesperdiciada
     
     #calcular cantidad de bananas 
     bananasProducidas = (azucarUtilizable // pesoBananas)
     
     return bananasProducidasjavier
#fin de la funcion"""
#programa de las bananas
"""

