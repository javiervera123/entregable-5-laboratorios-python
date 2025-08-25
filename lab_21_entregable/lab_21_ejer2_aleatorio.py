#número aleatorio con python
from js import document
from pyscript import display
import random

def calcular_21_2(event):
    num_maquina =random.randint(1, 50)  #genero y guardo mi numero para compararlo con el del usuario.
   
    num_usuario_str= (document.getElementById("input_21_2_numero").value.strip())
    if (num_usuario_str ==""):
        raise ValueError("El nombre no puede estar vacío !!")
    num_usuario = int(num_usuario_str)
    if (num_usuario ==num_maquina):
        display(f"Felicitaciones, Haz acertado: {num_maquina}", target ="resultado21_2", append=False)
        return
    display(f"Lo siento, sigue intentando. El número era {num_maquina}", target ="resultado21_2", append=False)

def limpiar_21_2(event):       
        document.getElementById("input_21_2_numero").value = ""
        display("", target="resultado21_2", append=False)