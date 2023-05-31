import json
import re

# Abrir el archivo JSON
with open('dt.json', "r", encoding = "utf-8") as archivo:
    lista = json.load(archivo)
    # Obtener la lista de jugadores
    jugadores = lista["jugadores"]

def listaJugadores():
    print("\n-----------------------------------")
    # Iterar sobre los jugadores
    posJugador = 0
    for jugador in jugadores:
        posJugador = posJugador + 1
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        # Imprimir los datos del jugador
        print(posJugador,".", nombre,"-",posicion)
        print("-----------------------------------")

def estadisticasJugador(indice):
    indice = indice - 1
    # Seleccionar jugador a mostrar
    jugador = jugadores[indice]
    estadisticas = jugador["estadisticas"]
    return("""
    Nombre: {12}
    Posicion: {13}
    Temporadas: {0} 
    Puntos totales: {1}
    Promedio de puntos por partido: {2}
    Rebotes totales: {3}
    Promedio de rebotes por partido: {4}
    Asistencias totales: {5}
    Promedio asistencias por partido: {6}
    Robos totales: {7} 
    Bloqueos totales: {8}
    Porcentaje tiros de campo: {9}
    Porcentaje tiros libres: {10}
    Porcentaje tiros triples: {11}""".format(estadisticas["temporadas"], estadisticas["puntos_totales"],
                    estadisticas["promedio_puntos_por_partido"], estadisticas["rebotes_totales"], 
                    estadisticas["promedio_rebotes_por_partido"], estadisticas["asistencias_totales"], 
                    estadisticas["promedio_asistencias_por_partido"], estadisticas["robos_totales"], estadisticas["bloqueos_totales"],
                    estadisticas["porcentaje_tiros_de_campo"], estadisticas["porcentaje_tirosLibres"], 
                    estadisticas["porcentaje_tiros_triples"], jugador["nombre"], jugador["posicion"]))
    
def exportarCSV(indice):
    with open("estadisticas_jugador.csv","w") as file:
            file.write(estadisticasJugador(indice))
    print("\n\t\tArchivo CSV generado exitosamente.")
 
def buscarJugador(nombre):
    patron = re.compile(nombre, re.IGNORECASE)
    jugadoresEncontrados = []

    for jugador in jugadores:
        if re.search(patron, jugador["nombre"]):
            jugadoresEncontrados.append(jugador)
    return jugadoresEncontrados

def logrosJugador (nombre):
    jugadoresEncontrados = buscarJugador(nombre)

    if not jugadoresEncontrados:
        return("No se encontró ningún jugador con ese nombre.")
    else:
        for jugador in jugadoresEncontrados:
            return json.dumps(jugador["logros"],indent=2)
        
def calcularPromedio():
    promedios = []
    for jugador in jugadores:
        promedio = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios.append(promedio)

    promedioEquipo = sum(promedios) / len(promedios)
    promedioEquipo = format(promedioEquipo, ".2f")

    jugadores_ordenados = sorted(jugadores, key=lambda x: x["nombre"])

    print("\nEl promedio general de puntos por partido del equipo es: ", promedioEquipo)
    print("\nJugadores ordenados alfabeticamente: \n")

    for jugador in jugadores_ordenados:
        nombre = jugador["nombre"]
        print("\t",nombre)


def verificarMiembroSalonFama(nombre):
   jugadorEncontrado = buscarJugador(nombre)
   if jugadorEncontrado:
    for jugador in jugadores:
            logros = jugador.get("logros", [])

            if "Miembro del Salon de la Fama del Baloncesto" in logros:
                return ("El jugador {0} es miembro del Salón de la Fama del Baloncesto".format(nombre))
            else:
                return ("El jugador {0} no es miembro del Salón de la Fama del Baloncesto".format(nombre))
    else:
        return("No se encontró ningún jugador con ese nombre.")
    
def calcularMaximoJugador(claveEstadistica):
    maximoValor = 0
    jugadorMaximo = None
    for jugador in jugadores:
        valorEstadistica = jugador["estadisticas"][claveEstadistica]
        if valorEstadistica > maximoValor:
            maximoValor = valorEstadistica
            jugadorMaximo = jugador["nombre"]
    return jugadorMaximo

def calcularPromedioSuperior(valor, atributo):
    flag = 0
    for jugador in jugadores:
        promedio = jugador["estadisticas"][atributo]
        if promedio > valor:
            flag = 1
            print(jugador["nombre"])
    if flag == 0:
        print("No se encuentra jugador con mayor valor")

def calcularLogros():
    jugadorMayorLogros = None
    cantidadMayorLogros = 0
    for jugador in jugadores:
        cantidadLogros = len(jugador["logros"])
        if cantidadLogros > cantidadMayorLogros:
            cantidadMayorLogros = cantidadLogros
            jugadorMayorLogros = jugador
    return("El jugador con mayor cantidad de logros es: {} y tiene {} logros".format(jugadorMayorLogros["nombre"], cantidadMayorLogros))

def calcularPromedioSinUltimo():
    jugadorMenorPuntos = min(jugadores, key=lambda jugador: jugador["estadisticas"]["promedio_puntos_por_partido"])
    menorPuntos = jugadorMenorPuntos["estadisticas"]["promedio_puntos_por_partido"]
    promedios = []
    for jugador in jugadores:
        if jugador["estadisticas"]["promedio_puntos_por_partido"] != menorPuntos:
            promedios.append(jugador["estadisticas"]["promedio_puntos_por_partido"])
    promedio_equipo = sum(promedios) / len(promedios)
    promedio_equipo = format(promedio_equipo, ".2f")
    return promedio_equipo