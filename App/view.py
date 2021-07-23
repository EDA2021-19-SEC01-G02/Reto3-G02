"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar cuantas reproducciones de piezas musicales tienen 2 características en un rango definido")
    print("3- Consultar cuantas piezas no repetidas tienen Speechness y Liveness en un rango definido")
    print("4- Consultar cuantas piezas no repetidas tienen Valence y Tempo en un rango definido")
    print("5- Consultar cuantas piezas no repetidas se tienen de un genero y cuantos artistas se tienen en el genero")    
    print("0- Salir")

def printCaracteristicas(c1, min1, max1, c2, min2, max2, repro, art):
    print('++++++ Req No. 1 resultados... ++++++')
    print('{} entre {} y {} y {} entre {} y {}.'.format(c1.capitalize(), min1, max1, c2.capitalize(), min2, max2))
    print('Total de reproducciones: {}. Total de artistas únicos: {}'.format(repro, art))

def printKaraoke(min1, max1, min2, max2, num, tracks):
    print('++++++ Req No. 2 resultados... ++++++')
    print('Liveness entre {} y {}'.format(min1, max1))
    print('Speechiness entre {} y {}'.format(min2, max2))
    print('Total de canciones únicas: {}\n'.format(num))
    print('--- Id canciones únicas ---')
    for i in range(1, lt.size(tracks)+1):
        track = lt.getElement(tracks, i)
        print('Track {}: {} con liveness de {:.3f} y speechiness de {:.3f}'.format(i, track['track_id'], float(track['liveness']), float(track['speechiness'])))

def printBroken(min1, max1, min2, max2, num, tracks):
    print('++++++ Req No. 3 resultados... ++++++')
    print('Valence entre {} y {}'.format(min1, max1))
    print('Tempo entre {} y {}'.format(min2, max2))
    print('Total de canciones únicas: {}\n'.format(num))
    print('--- Id canciones únicas ---')
    for i in range(1, lt.size(tracks)+1):
        track = lt.getElement(tracks, i)
        print('Track {}: {} con valence de {:.3f} y tempo de {:.3f}'.format(i, track['track_id'], float(track['valence']), float(track['tempo'])))



catalog = None



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print('Eventos cargados: ' + str(controller.eventSize(catalog)))
        print('Total de artistas unicos cargados: ' + str(controller.artistSize(catalog)))
        print('Total de pistas de audio unicas cargadas: ' + str(controller.trackSize(catalog)))

    elif int(inputs[0]) == 2:
        c1 = input("Ingrese la primera caracteristica a buscar: ")
        min1 = float(input("Ingrese el valor minimo de la primera caracteristica: "))
        max1 = float(input("Ingrese el valor maximo de la primera caracteristica: "))
        c2 = input("Ingrese la segunda caracteristica a buscar: ")
        min2 = float(input("Ingrese el valor minimo de la segunda caracteristica: "))
        max2 = float(input("Ingrese el valor maximo de la segunda caracteristica: "))
        repro, art, map = controller.getCaracteristicas(catalog, c1, min1, max1, c2, min2, max2)
        printCaracteristicas(c1, min1, max1, c2, min2, max2, repro, art)

    elif int(inputs[0]) == 3:
        min1 = float(input("Ingrese el valor minimo de Liveness: "))
        max1 = float(input("Ingrese el valor maximo de Liveness: "))
        min2 = float(input("Ingrese el valor minimo de Speechiness: "))
        max2 = float(input("Ingrese el valor maximo de Speechiness: "))
        num, tracks = controller.getKaraoke(catalog, min1, max1, min2, max2)
        printKaraoke(min1, max1, min2, max2, num, tracks)

    elif int(inputs[0]) == 4:
        min1 = float(input("Ingrese el valor minimo de Valence: "))
        max1 = float(input("Ingrese el valor maximo de Valence: "))
        min2 = float(input("Ingrese el valor minimo de Tempo: "))
        max2 = float(input("Ingrese el valor maximo de Tempo: "))
        num, tracks = controller.getBroken(catalog, min1, max1, min2, max2)
        printBroken(min1, max1, min2, max2, num, tracks)

    elif int(inputs[0]) == 5:
        genero = input("Ingrese el nombre del genero musical a buscar: ")
        minimo = input("Ingrese el valor minimo de Valence: ")
        maximo = input("Ingrese el valor maximo de Valence: ")
        generos_m = controller.getGeneros(catalog,genero, minimo, maximo)
        printRuptura(generos_m)
    else:
        sys.exit(0)
sys.exit(0)
