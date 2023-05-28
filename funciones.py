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
                    estadisticas["porcentaje_tiros_de_campo"], estadisticas["porcentaje_tiros_libres"], 
                    estadisticas["porcentaje_tiros_triples"], jugador["nombre"], jugador["posicion"]))
    
def exportarCSV(indice):
    with open("estadisticas_jugador.csv","w") as file:
            file.write(estadisticasJugador(indice))
    print("\n\t\tArchivo CSV generado exitosamente.")
 
def buscar_jugador(nombre):
    patron = re.compile(nombre, re.IGNORECASE)
    jugadores_encontrados = []

    for jugador in jugadores:
        if re.search(patron, jugador["nombre"]):
            jugadores_encontrados.append(jugador)
    
    return jugadores_encontrados

def logrosJugador (nombre):
    jugadores_encontrados = buscar_jugador(nombre)

    if not jugadores_encontrados:
        return("No se encontró ningún jugador con ese nombre.")
    else:
        for jugador in jugadores_encontrados:
            return json.dumps(jugador["logros"],indent=2)
        
def calcularPromedio():
    for jugador in jugadores:
        estadisticas = jugador["estadisticas"]
        suma = sum(estadisticas["promedio_puntos_por_partido"])
        cantidad = len(jugadores)
    promedio = suma / cantidad
    print(promedio)
    return promedio
