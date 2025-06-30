from bibliotecaexamen import*
from datos import*
while running:
    mostrar_menu()
    opcion = pedir_datos("Selecciona una opcion entre 1 y 5: ","int")
    opcion = validar_dentro_de_un_rango_numerico(limite_inferior,limite_superior,opcion)
    if opcion == 1:
        mostrar_califaciones_y_estudiantes(estudiantes,calificaciones)
    elif opcion == 2:
        promedios = obtener_promedios(calificaciones)
        ordenar_estudiantes_por_promedio(estudiantes,promedios,calificaciones)
        print("El ordenamiento se ha realizado con exito")
    elif opcion == 3:
        estudiante = pedir_datos("Ingrese el nombre del estudiante: ","str")
        posiciones = obtener_posiciones_de_estudiantes(estudiante,estudiantes)
        mostrar_calificaciones_de_estudiantes(estudiantes,posiciones,calificaciones)
    elif opcion == 4:
        nota = pedir_datos("Ingrese la nota a buscar: ","int")
        posiciones = obtener_posiciones_de_nota(nota,calificaciones)
        mostrar_estudiantes_de_una_nota(nota,posiciones,estudiantes,materias)
    elif opcion == 5:
        print("Saliendo del programa...")
        running = False