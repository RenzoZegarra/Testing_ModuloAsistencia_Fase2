# pip install mysql-connector-python
import modulo_registrar_asistencia # Funcionalidad 1
import modulo_justificacion # Funcionalidad 2
import modulo_reporte_asistencia # Funcionalidad 3
import modulo_reporte_fecha # Funcionalidad 4
import modulo_reporte_porcentaje # Funcionalidad 5
from datetime import datetime

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
            modulo_registrar_asistencia.registrar_asistencia(fecha)
        
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
            modulo_justificacion.justificar_inasistencia(id_estudiante, fecha)
            
        elif opcion == "3":
            print("Modulo 3")
            codigo = input("Ingrese el código del estudiante: ")
            modulo_reporte_asistencia.reporte_asistencia_estudiante(codigo)
            
        elif opcion == "4":
            print("Moudlo 4")
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            modulo_reporte_fecha.control_por_fecha(fecha)

        elif opcion == "5":
            codigo = input("Ingrese el código del estudiante: ")
            modulo_reporte_porcentaje.calcular_porcentaje_asistencia(codigo)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break 
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()