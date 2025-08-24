from js import document,Blob, URL #blob y url para imprimir docum, para el dom de js
from pyscript import display

# listas globales
nombre_empleado = []
sueldo_empleado = []
conta1 = 0
conta2 = 0
gastos = 0
num_emp = 0

def agregar_empleados(event):
    global conta1, conta2, gastos, num_emp
    try:
        # número total de empleados
        num_emp = int(document.getElementById("input_19_cant_empl").value)
        #desctivo el input para que no se equivoque el usuario
        document.getElementById("input_19_cant_empl").disabled = True

        if len(nombre_empleado) >= num_emp:
            display("⚠️ Ya registraste todos los empleados.", target="resultado19_2", append=False)
            return    
      
        nombre = document.getElementById("input_19_nom_empl").value
        sueldo = float(document.getElementById("input_19_salario").value)
        # guardo en listas
        nombre_empleado.append(nombre)
        sueldo_empleado.append(sueldo)

        # acumulo gastos
        gastos += sueldo

        # validación de sueldos
        if 1000000 <= sueldo <= 3000000:
            conta1 += 1
        elif 3000000 < sueldo <= 5000000:
            conta2 += 1
        else:
            display("⚠️ Sueldo fuera de rango (1M - 5M)", target="resultado19_2", append=False)

        # muestro registro parcial
        display(f"✅ Empleado agregado: {nombre} - $ {sueldo:,.2f}. "
                f" Total registrados: {len(nombre_empleado)}/{num_emp}",
                target="resultado19_2", append=False)

        # limpio los inputs de nombre, sueldo
        document.getElementById("input_19_nom_empl").value = ""
        document.getElementById("input_19_salario").value = ""
        
    except ValueError:
        display("❌ Error: Falta ingresar información...", target="resultado19_2", append=False)


def finalizar_registro(event):
    global conta1, conta2, gastos, num_emp

    if len(nombre_empleado) < num_emp:
        display("⚠️ Faltan empleados por registrar.", target="resultado19_2", append=False)
        return

    display("📊 RESULTADOS FINALES", target="resultado19_2", append=True)
    display(f" Nómina: {', '.join(nombre_empleado)}", target="resultado19_2", append=True)
    display(f"{conta1} empleado(s) cobran entre 1 Millón y 3 Millones ", target="resultado19_2", append=True)
    display(f"{conta2} empleado(s) cobran más de 3 Millones ", target="resultado19_2", append=True)
    display(f"Total en gastos de nómina: $ {gastos:,.2f}", target="resultado19_2", append=True)
    display(f"Total empleados(nómina): {num_emp}", target="resultado19_2", append=True)
    document.getElementById("input_19_cant_empl").value = "" #limpiar input de cant empleados    
    
    #termina funcion finlizar
    
def reiniciar_datos(event):
    global nombre_empleado, sueldo_empleado, conta1, conta2, gastos, num_emp
    nombre_empleado = []                         #inicializo mis listas para nuevos datos
    sueldo_empleado = []
    conta1 = conta2 = gastos = num_emp = 0       #todas mis variables de nuevo en cero
    document.getElementById("input_19_cant_empl").value = ""
    document.getElementById("input_19_nom_empl").value = ""
    document.getElementById("input_19_salario").value = ""
    #vuelvo a activar el input
    document.getElementById("input_19_cant_empl").disabled = False
    display("🔄 Datos reiniciados.", target="resultado19_2", append=False)

def boton_imprimir(event):
    gastos, num_emp
    lineas = [  # guardamos en una lista las salidas
        f"{num_emp} empleados hay en la empresa -----SOLUCIONES AUTOMÁTICAS VERA-------"
        f"Nombres de empleados: {nombre_empleado}"
        f"Su sueldo es: {sueldo_empleado}"
        f"------Datos globales de la empresa: ---------"
        f"{conta1} empleado(s) cobra(n) entre $1.000.000 y $3.000.000\n",
        f"{conta2} empleado(s) cobra(n) más de $3.000.000\n",
        f"El total que gasta la empresa en sueldos es de ${gastos:,.2f}\n"
]
    contenido = "".join(lineas)
    blob = Blob.new([contenido], { "type": "text/plain" })
    url = URL.createObjectURL(blob)

    link = document.createElement("a")
    link.href = url
    link.download = "reporte_salarios.txt"
    link.click()

