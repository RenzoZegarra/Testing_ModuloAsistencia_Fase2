# pip install mysql-connector-python
import modulo_registrar_asistencia # Funcionalidad 1
import modulo_justificacion # Funcionalidad 2
import modulo_reporte_asistencia # Funcionalidad 3
import modulo_reporte_fecha # Funcionalidad 4
import modulo_reporte_porcentaje # Funcionalidad 5
import conexion
from datetime import datetime

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



def mostrar_menu():
    print("\n" + "="*30)
    print("      SISTEMA DE ASISTENCIA")
    print("="*30)
    print("1. Registrar astiencia (Módulo 1)")
    print("2. Jusitificar inasistencia (Módulo 2)")
    print("3. Generar Reporte de asistencia por estudiante (Módulo 3)")
    print("4. Generar reporte de asistencias por fecha (Módulo 4)")
    print("5. Generar reporte de porcentaje de asistencias individuales (Módulo 5)")
    print("6. Salir")
    print("="*30)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            fecha = input("Ingrese la fecha de asistencia (YYYY-MM-DD): ")
            modulo_registrar_asistencia.registrar_asistencia(fecha, cursor, conexion)
        
        elif opcion == "2":
            while True:
                try:
                    id_estudiante = int(input("Ingrese el ID del estudiante: "))
                    if id_estudiante <= 0:
                        print("El ID debe ser un número positivo")
                        continue
                    break
                except ValueError:
                    print("ERROR: debe ingresar un numero entero valido")

            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            modulo_justificacion.justificar_inasistencia(id_estudiante, fecha, cursor, conexion)
            
        elif opcion == "3":
            print("Modulo 3")
            codigo = input("Ingrese el código del estudiante: ")
            modulo_reporte_asistencia.reporte_asistencia_estudiante(codigo, cursor, conexion)
            
        elif opcion == "4":
            print("Moudlo 4")
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            modulo_reporte_fecha.control_por_fecha(fecha, cursor, conexion)

        elif opcion == "5":
            codigo = input("Ingrese el código del estudiante: ")
            modulo_reporte_porcentaje.calcular_porcentaje_asistencia(codigo, cursor, conexion)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break 
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    while True:
        print("--- CONECTAR BD MYSQL ---")
        host = input("Ingrese el host: ")
        usuario = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        conexion, cursor = conexion_BD(host, usuario, password)
        if conexion and cursor:
            print("Entrando al módulo...")
            break


    main()
    