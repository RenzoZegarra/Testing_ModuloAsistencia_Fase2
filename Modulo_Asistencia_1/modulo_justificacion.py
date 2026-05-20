import mysql.connector


def justificar_inasistencia(estudiante_id, fecha, cursor, conexion):
    try:
        # Conexión a la base de datos
        #conexion = mysql.connector.connect(
            #host="localhost",
            #user="root",
            #password="",
            #database="modulo_asistencia")

        #cursor = conexion.cursor()

        # Buscar la asistencia del estudiante en la fecha indicada
        consulta = """
        SELECT asistio, justificado
        FROM asistencias
        WHERE estudiante_id = %s AND fecha = %s
        """

        cursor.execute(consulta, (estudiante_id, fecha))
        resultado = cursor.fetchone()

        # Verificar si existe el registro
        if resultado is None:
            print("No existe un registro de asistencia para ese estudiante y fecha.")
            return

        asistio, justificado = resultado

        # Si el estudiante asistió
        if asistio == 1:
            print("El estudiante sí asistió ese día.")
            return

        # Si ya estaba justificado
        if justificado == 1:
            print("La inasistencia ya estaba justificada.")
            return

        # Actualizar justificación
        actualizar = """
        UPDATE asistencias
        SET justificado = 1
        WHERE estudiante_id = %s AND fecha = %s
        """

        cursor.execute(actualizar, (estudiante_id, fecha))
        conexion.commit()

        print("La inasistencia fue justificada correctamente.")

    except mysql.connector.Error as error:
        print("Error en la base de datos:", error)
        conexion.rollback()

    #finally:
        #if conexion.is_connected():
            #cursor.close()
            #conexion.close()


# MAIN SIMPLE
#id_estudiante = int(input("Ingrese el ID del estudiante: "))
#fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
#justificar_inasistencia(id_estudiante, fecha)