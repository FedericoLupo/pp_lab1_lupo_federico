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
          7.
          8.
          9.
          10.
          11.
          12.
          13.
          14.
          15.
          16.
          17.
          18.
          19.
          20.
          23.
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