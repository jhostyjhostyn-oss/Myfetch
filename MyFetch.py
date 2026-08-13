import subprocess
from Colores import *
def detectar_kernel():
    resultado = subprocess.run(
        ["uname", "-r"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def detectar_cpu():
    resultado = subprocess.run(
        ["lscpu"],
        capture_output=True,
        text=True
    )

    for linea in resultado.stdout.splitlines():
        if "Nombre del modelo:" in linea:
            return linea.split(":", 1)[1].strip()

SystemInfo = {
    'CPU':detectar_cpu(),
    'KERNEL':detectar_kernel(),

}

for clave, valor in SystemInfo.items():
    print(clave, valor)