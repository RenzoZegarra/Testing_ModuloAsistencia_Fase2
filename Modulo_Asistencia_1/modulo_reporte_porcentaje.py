import mysql.connector


def calcular_porcentaje_asistencia(codigo_estudiante):

    # Validar que sea texto
    if not isinstance(codigo_estudiante, str):
        print("Error: el código debe ser texto.")
        return

    codigo_estudiante = codigo_estudiante.strip()

    # Validar formato del código
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

        # Obtener cantidades
        consulta_asistencias = """
        SELECT
            COUNT(*) AS total_registros,
            SUM(asistio = 1) AS total_asistencias,
            SUM(asistio = 0) AS total_inasistencias
        FROM asistencias
        WHERE estudiante_id = %s
        """

        cursor.execute(consulta_asistencias, (estudiante_id,))
        resultado = cursor.fetchone()

        total_registros = resultado[0]
        total_asistencias = resultado[1] if resultado[1] is not None else 0
        total_inasistencias = resultado[2] if resultado[2] is not None else 0

        # Evitar división entre cero
        if total_registros == 0:
            print("El estudiante no tiene asistencias registradas.")
            return

        # Calcular porcentajes
        porcentaje_asistencia = (total_asistencias / total_registros) * 100
        porcentaje_inasistencia = (total_inasistencias / total_registros) * 100

        # Mostrar reporte
        print("\n===== PORCENTAJE DE ASISTENCIA =====")
        print(f"Estudiante: {nombre} {apellido}")
        print(f"Código: {codigo_estudiante}")

        print(f"Asistencia: {porcentaje_asistencia:.2f}%")
        print(f"Inasistencia: {porcentaje_inasistencia:.2f}%")

        # Alerta de baja asistencia
        if porcentaje_asistencia < 70:
            print("ALERTA: El estudiante tiene baja asistencia.")

    except mysql.connector.Error as error:
        print("Error en la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


# MAIN SIMPLE

#codigo = input("Ingrese el código del estudiante: ")

#calcular_porcentaje_asistencia(codigo)