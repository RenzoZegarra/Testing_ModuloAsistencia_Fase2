import mysql.connector
from datetime import datetime


def registrar_asistencia(fecha):
    # Validar fecha
    try:
        datetime.strptime(fecha, "%Y-%m-%d")

    except ValueError:
        print("Error: la fecha ingresada no es válida.")
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

        # Verificar si la fecha ya existe
        consulta_fecha = """
        SELECT COUNT(*)
        FROM asistencias
        WHERE fecha = %s
        """

        cursor.execute(consulta_fecha, (fecha,))
        cantidad = cursor.fetchone()[0]

        if cantidad > 0:
            print("Esa fecha ya está registrada.")
            return

        # Obtener todos los estudiantes
        consulta_estudiantes = """
        SELECT id, nombre, apellido
        FROM estudiantes
        """

        cursor.execute(consulta_estudiantes)
        estudiantes = cursor.fetchall()

        # Recorrer estudiantes automáticamente
        for estudiante in estudiantes:

            estudiante_id = estudiante[0]
            nombre = estudiante[1]
            apellido = estudiante[2]

            print(f"\nEstudiante: {nombre} {apellido}")

            # Validar asistencia
            while True:
                try:
                    asistio = int(input("¿Asistió? (1 = Sí / 0 = No): "))

                    if asistio not in [0, 1]:
                        print("Error: solo puede ingresar 0 o 1.")
                        continue

                    break

                except ValueError:
                    print("Error: debe ingresar un número válido.")

            # Si asistió, no se pregunta justificación
            if asistio == 1:
                justificado = 0

            else:
                # Validar justificación
                while True:
                    try:
                        justificado = int(input("¿Se justificó? (1 = Sí / 0 = No): "))

                        if justificado not in [0, 1]:
                            print("Error: solo puede ingresar 0 o 1.")
                            continue

                        break

                    except ValueError:
                        print("Error: debe ingresar un número válido.")

            # Insertar asistencia
            insertar = """
            INSERT INTO asistencias (
                estudiante_id,
                fecha,
                asistio,
                justificado
            )
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                insertar,
                (estudiante_id, fecha, asistio, justificado)
            )

        conexion.commit()

        print("\nRegistro de asistencia completado correctamente.")

    except mysql.connector.Error as error:
        print("Error en la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


# MAIN SIMPLE

#fecha = input("Ingrese la fecha de asistencia (YYYY-MM-DD): ")

#registrar_asistencia(fecha)