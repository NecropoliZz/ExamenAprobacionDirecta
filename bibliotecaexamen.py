
def obtener_promedios(calificaciones:list)->list:
    """
    Suma todos los elementos de una fila de una matriz,y los va guardando en una lista llamada promedios hasta que termina de recorrer la matriz
    Parametros:
    calificaciones(list): la matriz de la cual se haran las sumas
    Retorno: Retorna la lista promedios
    """
    promedios = []
    total = 0
    for i in range(len(calificaciones)):
        for j in range(len(calificaciones[i])):
            total += calificaciones[i][j]
        promedio = total/len(calificaciones[i])
        promedios.append(promedio)
        total = 0
    return promedios
def ordenar_estudiantes_por_promedio(estudiantes:list,promedios:list,calificaciones:list):
    """
    Esta funcion ordena una matriz de manera descendente(mayor a menor), teniendo como criterio los promedios
    Parametros:
    estudiantes(list): Lista que esta en paralelo con la matriz principal
    promedios(list): Lista de promedios de calificaciones
    calificaciones(list): Matriz principal
    """
    for i in range(len(promedios)-1):
        for j in range(i+1,len(promedios)):
            if promedios[i] < promedios[j]:
                aux_promedios = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux_promedios
                aux_calificaciones = calificaciones[i]
                calificaciones[i] = calificaciones[j]
                calificaciones[j] = aux_calificaciones
                aux_estudiantes = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_estudiantes
def obtener_posiciones_de_estudiantes(estudiante:str,estudiantes:list)->any:
    """
    Obtiene donde esta ubicado(indices) un tipo de dato str dentro de una lista
    Parametros:
    estudiante(str): Dato a buscar
    estudiantes(list): Lista en la que hay que buscar
    Retorno: Retorna una lista
    """
    posiciones = []
    for i in range(len(estudiantes)):
        if estudiante == estudiantes[i]:
            posiciones.append(i)
    return posiciones
def mostrar_calificaciones_de_estudiantes(estudiantes:list,posiciones:list,calificaciones:list):
    """
    Funcion que muestra las ventas de un producto
    Parametros:
    estudiantes(list): lista de estudiantes
    calificaciones(list): lista de calificaciones
    posiciones(list): lista con indices de cada estudiante
    """
    if len(posiciones) != 0:
        for indice in posiciones:
            print(f"Notas de {estudiantes[indice]}: {calificaciones[indice]}")
    else:
       print("No se encontro ningun estudiante con ese nombre")
def obtener_posiciones_de_nota(nota:int,calificaciones:list)->any:
    """
    Obtiene la ubicacion(indices) de un tipo de dato int en concreto dentro de una matriz
    Parametros:
    nota(int): dato a buscar
    calificaciones(list): Matriz principal
    Retorno: Retorna una lista llamda ubicacion, que tiene como  elementos listas con la fila y columna del dato a buscar
    """
    posiciones = []
    for i in range(len(calificaciones)):
        for j in range(len(calificaciones[i])):
            if nota == calificaciones[i][j]:
                posiciones.append([i,j])
    return posiciones     
def mostrar_estudiantes_de_una_nota(nota:int,posiciones:list,estudiantes:list,materias:list):
    """
    Funcion que muestra el estudiante y materia al que pertenece una nota
    Parametros: 
    ubicaciones(list): matriz de indices
    estudiantes(list): Lista de estudiantes
    materias(list): Lista de materias
    """
    if len(posiciones) != 0:
      for i, j in posiciones:
          print(f"Nota encontrada: {nota} -> Estudiante: {estudiantes[i]}, Materia: {materias[j]}")
    else:
        print("No se encontro ninguna nota en la lista")
def validar_dentro_de_un_rango_numerico(limiteinferior:int,limitesuperior:int,numero:int):
    """
    Funcion para validar que un numero este dentro de un rango numero designado
    Parametros:
    limiteinferior(int): Limite inferior del rango numerico
    limitesuperior(int): limite superior del rango numerico
    numero(int): Numero en cuestion a validar
    """
    while numero < limiteinferior or numero > limitesuperior:
        numero = int(input(f"Error, ingrese un dato valido entre {limiteinferior} y {limitesuperior}: "))
    return numero
def pedir_datos(mensaje:str,tipo:str)->any:
    """
    Pide un dato al usuario y lo retorna
    Parametros:
    mensaje(str): Es el mensaje con el cual se la va a pedir al usuario el dato
    Retorno: el tipo de dato pedido
    """
    retorno = None
    if tipo == "str":
       retorno = input(mensaje)
    elif tipo == "int":
        retorno = int(input(mensaje))
    return retorno
def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("--- MENU DE OPCIONES ---")
    print("1. Mostrar lista de estudiantes y calificaciones")
    print("2. Ordenar estudiantes por promedio (mayor a menor)")
    print("3. Buscar estudiante por nombre y mostrar sus calificaciones")
    print("4. Buscar calificación en la matriz")
    print("5. Salir")
def mostrar_califaciones_y_estudiantes(estudiantes:list,califaciones:list):
    print("Estudiantes y calificaciones: ")
    for i in range(len(califaciones)):
        print(f"{estudiantes[i]} -> {califaciones[i]}")
