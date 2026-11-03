import mysql.connector

# Datos de conexion
config = {
    'user': 'root',
    'password': '1234',
    'host': '172.17.0.3',
    'database': 'bdcoches'
}

def conectar(config):
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexion establecida a la BD")
        return conexion
    else:
        print("No se ha podido conectar a la BD")
        return None

def consultaCoches():
    conexion = conectar(config)
    if conexion is None:
        return
    # Creo el cursor que gestiona la consulta y el retorno de los datos
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