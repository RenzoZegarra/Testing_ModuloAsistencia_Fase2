import mysql.connector
from mysql.connector import Error


def conexion_BD(host, usuario, password):
    """
    Función para conectar a MySQL.
    Retorna:
        conexion, cursor
    Si ocurre un error:
        retorna None, None
    """

    # =========================
    # VALIDACIONES
    # =========================
    if not isinstance(host, str) or not host.strip():
        print("ERROR: El host no puede estar vacío.")
        return None, None

    if not isinstance(usuario, str) or not usuario.strip():
        print("ERROR: El usuario no puede estar vacío.")
        return None, None

    #if password is None:
    #    print("ERROR: La contraseña no puede ser None.")
    #    return None, None

    try:
        # =========================
        # CONEXIÓN
        # =========================
        conexion = mysql.connector.connect(
            host=host.strip(),
            user=usuario.strip(),
            password=password,
            database="modulo_asistencia",
            autocommit=False
        )

        # =========================
        # VALIDAR CONEXIÓN
        # =========================
        if conexion.is_connected():

            cursor = conexion.cursor()

            print("-" * 40)
            print("Conexión exitosa a MySQL")
            print("Base de datos: modulo_asistencia")
            print("-" * 40)

            return conexion, cursor

        else:
            print("ERROR: No se pudo establecer la conexión.")
            return None, None

    # =========================
    # ERRORES ESPECÍFICOS MYSQL
    # =========================
    except Error as e:

        print("-" * 40)

        if e.errno == 1045:
            print("ERROR: Usuario o contraseña incorrectos.")

        elif e.errno == 1049:
            print("ERROR: La base de datos 'modulo_asistencia' no existe.")

        elif e.errno == 2003:
            print("ERROR: No se pudo conectar al servidor MySQL.")

        else:
            print(f"ERROR MYSQL: {e}")

        print("-" * 40)

        return None, None

    # =========================
    # CUALQUIER OTRO ERROR
    # =========================
    except Exception as e:
        print("-" * 40)
        print(f"ERROR GENERAL: {e}")
        print("-" * 40)

        return None, None


# =========================================
# USO DEL MÓDULO
# =========================================
if __name__ == "__main__":

    print("--- CONECTAR BD MYSQL ---")

    host = input("Ingrese el host: ")
    usuario = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    conexion, cursor = conexion_BD(host, usuario, password)

    if conexion and cursor:
        print("El módulo puede ser utilizado por otros archivos.")

        # Ejemplo de prueba
        # cursor.execute("SELECT DATABASE();")
        # print(cursor.fetchone())

        cursor.close()
        conexion.close()
        print("Conexión cerrada.")