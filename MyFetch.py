import subprocess
from Colores import *

#IMPORTACION DE LOGOS
from Logos import logos
import os
import random




color = random.choice(colores)
logo = random.choice(logos)

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

def detectar_Escritorio():
    resultado = subprocess.run(
        ["echo", "$XDG_CURRENT_DESKTOP"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def Detectar_Distro():
    datos = {}

    with open("/etc/os-release") as archivo:
        for linea in archivo:
            if "=" in linea:
                clave, valor = linea.strip().split("=", 1)
                datos[clave] = valor.strip('"')

    return datos





SystemInfo1 = {
    '  󰒋 USUARIO ':detectar_User(),
    '   HOSTNAME ':detectar_hostname(),
    '  󰍛 CPU ' :detectar_cpu(),
    '   KERNEL ':detectar_kernel(),
    '  󰅐 UPTIME  ':detectar_uptime(),
    '   LOCALE':os.environ.get("LANG"),
    '   ESCRITORIO ':os.environ.get("XDG_CURRENT_DESKTOP"),
    '   SESION ': os.environ.get("XDG_SESSION_TYPE"),
    '   SHELL ': os.environ.get("SHELL", "Desconocida"),
    '   TERMINAL  ': os.environ.get("TERM", "Desconocida"),
}  

SystemInfo2 = {
    '    󰒋':detectar_User(),
    '    ':detectar_hostname(),
    '    󰍛':detectar_cpu(),
    '    ':detectar_kernel(),
    '    󰅐':detectar_uptime(),
    '    ':os.environ.get("LANG"),
    '    ':os.environ.get("XDG_CURRENT_DESKTOP"),
    '    ': os.environ.get("XDG_SESSION_TYPE"),
    '    ': os.environ.get("SHELL", "Desconocida"),
    '    ': os.environ.get("TERM", "Desconocida"),
}
info = [SystemInfo1, SystemInfo2]
SystemInfo = random.choice(info)

print(f"{color}{logo}{RESET}")
for clave, valor in SystemInfo.items():
    print(f"{color}╭──{AMARILLO}{clave:<15} > {color}{valor}{RESET}")

