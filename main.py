import funciones
indice = None

print("\nParcial Dream Team\n")
while True:
    #Menu de opciones
    print("""
    Menu de opciones:\n
          1. Mostrar lista de jugadores y su posicion
          2. Mostrar estadisticas de jugador por su indice
          3. Guardar estadisticas del jugador en un archivo CSV
          4. Mostrar logros de jugador por nombre
          5. Calcular el promedio de puntos por partido del equipo entero ordenado por nombre
          6. Mostrar si el jugador deseado pertenece al salon de la fama del baloncesto
          7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales
          8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo
          9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales
          10. Mostrar los jugadores que han promediado más puntos por partido que el valor buscado
          11. Mostrar los jugadores que han promediado más rebotes por partido que el valor buscado
          12. Mostrar los jugadores que han promediado más asistencias por partido que el valor buscado
          13. Calcular y mostrar el jugador con la mayor cantidad de robos totales
          14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales
          15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a el valor buscado
          16. Calcula y muestra promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
          17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
          18. Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a el valor buscado
          19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
          20. Mostrar jugadores ordenados por posicion en la cancha y superior al porcentaje de tiros seleccionados
          23. Punto bonus
          0. Salir del programa""")
    opcion = int(input("\nIngrese la opcion deseada: "))
    
    match opcion:
        case 1:
            funciones.listaJugadores()
        
        case 2:
            respuesta = funciones.estadisticasJugador(int(input("\nSeleccione numero de indice de jugador: ")))
            print(respuesta)

        case 3:
            if not indice:
                funciones.exportarCSV(int(input("\nSeleccione numero de indice de jugador: ")))
            else:
                funciones.exportarCSV(indice)

        case 4:
            respuesta = funciones.logrosJugador(str(input("\nIngrese nombre de jugador a buscar: ")))
            print("\n", respuesta)

        case 5:
            funciones.calcularPromedio()
            
        case 6:
            nombre= input("\nIngrese nombre del jugador: ")
            respuesta = funciones.verificarMiembroSalonFama(nombre)
            print("\n", respuesta)       

        case 7:
            respuesta = funciones.calcularMaximoJugador("rebotes_totales")
            print("\nEl jugador con mayor cantidad de rebotes totales es:", respuesta)

        case 8:
            respuesta = funciones.calcularMaximoJugador("porcentaje_tiros_de_campo")
            print("\nEl jugador con mayor porcentaje de tiros de campo es:", respuesta)

        case 9:
            respuesta = funciones.calcularMaximoJugador("asistencias_totales")
            print("\nEl jugador con mayor cantidad de asistencias totales es:", respuesta)

        case 10:
            numeroIngresado = float(input("\nIngrese el valor de referencia: "))
            print("\nJugadores con promedio de puntos superior a {0}:\n".format(numeroIngresado))
            funciones.calcularPromedioSuperior(numeroIngresado, "promedio_puntos_por_partido")
            
        case 11:
            numeroIngresado = float(input("\nIngrese el valor de referencia: "))
            print("\nJugadores con promedio de rebotes superior a {0}:\n".format(numeroIngresado))
            funciones.calcularPromedioSuperior(numeroIngresado, "promedio_rebotes_por_partido")

        case 12:
            numeroIngresado = float(input("\nIngrese el valor de referencia: "))
            print("\nJugadores con promedio de asistencias superior a {0}:\n".format(numeroIngresado))
            funciones.calcularPromedioSuperior(numeroIngresado, "promedio_asistencias_por_partido")

        case 13:
            respuesta = funciones.calcularMaximoJugador("robos_totales")
            print("\nEl jugador con mayor cantidad de robos totales es:", respuesta)

        case 14:
            respuesta = funciones.calcularMaximoJugador("bloqueos_totales")
            print("\nEl jugador con mayor cantidad de bloqueos totales es:", respuesta)

        case 15:
            numeroIngresado = float(input("\nIngrese el valor de referencia: "))
            print("\nJugadores con porcentaje de tiros libres superior a {0}:\n".format(numeroIngresado))
            funciones.calcularPromedioSuperior(numeroIngresado, "porcentaje_tiros_libres")        
        
        case 16:
            respuesta = funciones.calcularPromedioSinUltimo()
            print("El promedio de puntos por partido del equipo excluyendo al jugador con menor cantidad de puntos es:", respuesta)

        case 17:
            respuesta = funciones.calcularLogros()
            print("\n", respuesta)

        case 18:
            numeroIngresado = float(input("\nIngrese el valor de referencia: "))
            print("\nJugadores con porcentaje de tiros libres superior a {0}:\n".format(numeroIngresado))
            funciones.calcularPromedioSuperior(numeroIngresado, "promedio_puntos_por_partido")   

        case 19:
            respuesta = funciones.calcularMaximoJugador("temporadas")
            print("\nEl jugador con mayor cantidad de temporadas jugadas es:", respuesta)

        case 20:
            pass

        case 23:
            pass

        case 0:
            print("Adios")
            break
       
        case _:
            print("\n\tOpcion invalida, ingrese una opcion valida\n")