import json
import os
import mysql.connector

# Ruta del archivo de configuracion (en la misma carpeta que el script)
RUTA_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def cargarConfig(ruta):
    # Leo los datos de conexion desde el archivo JSON
    with open(ruta, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def conectar(config):
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexion establecida a la BD (datos leidos de config.json)")
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

    print()
    print(f"{'ID':<4}{'MARCA':<12}{'MODELO':<10}{'COLOR':<8}{'KM':>8}{'PRECIO':>11}")
    print("-" * 53)
    for coche in res:
        id, marca, modelo, color, km, precio = coche
        print(f"{id:<4}{marca:<12}{modelo:<10}{color:<8}{km:>8}{precio:>11.2f}")

    cursor.close()
    conexion.close()

consultaCoches()