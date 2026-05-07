import mysql.connector


def reporte_asistencia_estudiante(codigo_estudiante):

    # Validar formato del código
    if not isinstance(codigo_estudiante, str):
        print("Error: el código debe ser texto.")
        return

    codigo_estudiante = codigo_estudiante.strip()

    # Validar longitud y formato básico
    if len(codigo_estudiante) != 6 or not codigo_estudiante.startswith("E"):
        print("Error: el código ingresado no es válido.")
        return

    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="modulo_asistencia"
        )

        cursor = conexion.cursor()

        # Buscar estudiante
        consulta_estudiante = """
        SELECT id, nombre, apellido
        FROM estudiantes
        WHERE codigo = %s
        """

        cursor.execute(consulta_estudiante, (codigo_estudiante,))
        estudiante = cursor.fetchone()

        # Validar existencia
        if estudiante is None:
            print("Ese estudiante no está registrado.")
            return

        estudiante_id = estudiante[0]
        nombre = estudiante[1]
        apellido = estudiante[2]

        # Contar asistencias
        consulta_reporte = """
        SELECT
            SUM(asistio = 1) AS asistencias,
            SUM(asistio = 0) AS inasistencias,
            SUM(justificado = 1) AS justificaciones
        FROM asistencias
        WHERE estudiante_id = %s
        """

        cursor.execute(consulta_reporte, (estudiante_id,))
        reporte = cursor.fetchone()

        asistencias = reporte[0] if reporte[0] is not None else 0
        inasistencias = reporte[1] if reporte[1] is not None else 0
        justificaciones = reporte[2] if reporte[2] is not None else 0

        # Mostrar reporte
        print("\n===== REPORTE DE ASISTENCIA =====")
        print(f"Estudiante: {nombre} {apellido}")
        print(f"Código: {codigo_estudiante}")
        print(f"Asistencias: {asistencias}")
        print(f"Inasistencias: {inasistencias}")
        print(f"Justificaciones: {justificaciones}")

    except mysql.connector.Error as error:
        print("Error en la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


# MAIN SIMPLE

#codigo = input("Ingrese el código del estudiante: ")

#reporte_asistencia_estudiante(codigo)