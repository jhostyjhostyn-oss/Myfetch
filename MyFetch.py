import subprocess
from Colores import *
def detectar_kernel():
    resultado = subprocess.run(
        ["uname", "-r", "-m"],
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

def detectar_hostname():
    resultado = subprocess.run(
        ["hostname"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def detectar_User():
    resultado = subprocess.run(
        ["whoami"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()
    

def detectar_uptime():
    resultado = subprocess.run(
        ["uptime", "-p"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def detectar_locale():
    resultado = subprocess.run(
        ["locale", "|", "head", "-n1"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

SystemInfo1 = {
    'USER':detectar_User(),
    'HOSTNAME':detectar_hostname(),
    'CPU':detectar_cpu(),
    'KERNEL':detectar_kernel(),
    'UPTIME':detectar_uptime(),
    'LOCALE':detectar_locale(),
}

for clave, valor in SystemInfo1.items():
    print(f"{VERDE}╭──{AMARILLO}{clave:<12} --> {ROJO}{valor}")