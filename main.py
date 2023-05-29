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
            respuesta = funciones.calcularPromedio()
            print("\n", respuesta)

        case 6:
            pass
        
        case 7:
            pass
        case 8:
            pass

        case 9:
            pass

        case 10:
            pass

        case 11:
            pass

        case 12:
            pass

        case 13:
            pass

        case 14:
            pass        
        case 15:
            pass
        
        case 17:
            pass

        case 18:
            pass

        case 19:
            pass

        case 20:
            pass

        case 23:
            pass

        case 0:
            print("Adios")
            break
       
        case _:
            print("\n\tOpcion invalida, ingrese una opcion valida\n")