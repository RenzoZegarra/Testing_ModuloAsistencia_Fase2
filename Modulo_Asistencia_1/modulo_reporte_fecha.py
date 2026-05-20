import mysql.connector
from datetime import datetime


def control_por_fecha(fecha, cursor, conexion):

    # Validar formato de fecha
    try:
        datetime.strptime(fecha, "%Y-%m-%d")

    except ValueError:
        print("Error: la fecha ingresada no es válida.")
        return

    try:


        # Verificar si la fecha existe
        consulta_fecha = """
        SELECT COUNT(*)
        FROM asistencias
        WHERE fecha = %s
        """

        cursor.execute(consulta_fecha, (fecha,))
        existe = cursor.fetchone()[0]

        if existe == 0:
            print("No existen registros para esa fecha.")
            return

        # Contar asistencias e inasistencias
        consulta_control = """
        SELECT
            SUM(asistio = 1) AS asistieron,
            SUM(asistio = 0) AS no_asistieron
        FROM asistencias
        WHERE fecha = %s
        """

        cursor.execute(consulta_control, (fecha,))
        resultado = cursor.fetchone()

        asistieron = resultado[0] if resultado[0] is not None else 0
        no_asistieron = resultado[1] if resultado[1] is not None else 0

        # Mostrar reporte
        print("\n===== CONTROL POR FECHA =====")
        print(f"Fecha: {fecha}")
        print(f"Cantidad de estudiantes que asistieron: {asistieron}")
        print(f"Cantidad de estudiantes que no asistieron: {no_asistieron}")

    except mysql.connector.Error as error:
        print("Error en la base de datos:", error)
        conexion.rollback()



# MAIN SIMPLE

#fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

#control_por_fecha(fecha)