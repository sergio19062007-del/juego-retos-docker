import json
import os
from pymongo import MongoClient
from prettytable import PrettyTable

# Ruta del archivo de configuracion (en la misma carpeta que el script)
RUTA_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_mongo.json")

def cargarConfig(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def conectar(cfg):
    # Construccion de la URI de conexion
    uri = f"mongodb://{cfg['usuario']}:{cfg['contrasena']}@{cfg['host']}:{cfg['puerto']}/{cfg['base_datos']}?authSource=admin"
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
    cliente.admin.command("ping")   # Comprueba que la conexion funciona
    print("Conexion establecida a MongoDB")
    print("Bases de datos disponibles:", cliente.list_database_names())
    return cliente

def consultaCoches():
    cfg = cargarConfig(RUTA_CONFIG)
    cliente = conectar(cfg)
    db = cliente[cfg["base_datos"]]
    coleccion = db[cfg["coleccion"]]

    # Obtengo todos los documentos de la coleccion ordenados por id
    coches = coleccion.find().sort("id", 1)

    tabla = PrettyTable(["_id", "ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])
    for coche in coches:
        tabla.add_row([
            str(coche.get("_id", "")),
            coche.get("id", ""),
            coche.get("marca", ""),
            coche.get("modelo", ""),
            coche.get("color", ""),
            coche.get("km", ""),
            coche.get("precio", "")
        ])

    tabla.align["Marca"] = "l"
    tabla.align["Modelo"] = "l"
    tabla.align["Color"] = "l"
    tabla.align["Kilometraje"] = "r"
    tabla.align["Precio"] = "r"

    print(tabla)
    cliente.close()

consultaCoches()