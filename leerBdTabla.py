import json
import os
import mysql.connector
from prettytable import PrettyTable

# Ruta del archivo de configuracion (en la misma carpeta que el script)
RUTA_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def cargarConfig(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def conectar(config):
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexion establecida a la BD")
        return conexion
    else:
        print("No se ha podido conectar a la BD")
        return None

def consultaCoches():
    config = cargarConfig(RUTA_CONFIG)
    conexion = conectar(config)
    if conexion is None:
        return
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM coches")
    res = cursor.fetchall()

    # Creo la tabla con PrettyTable
    tabla = PrettyTable(["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])
    for fila in res:
        tabla.add_row(fila)

    # Alineacion: texto a la izquierda y numeros a la derecha
    tabla.align["Marca"] = "l"
    tabla.align["Modelo"] = "l"
    tabla.align["Color"] = "l"
    tabla.align["Kilometraje"] = "r"
    tabla.align["Precio"] = "r"

    print(tabla)

    cursor.close()
    conexion.close()

consultaCoches()