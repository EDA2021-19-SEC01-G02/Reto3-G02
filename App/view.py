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
    print("2- Consultar cuantas reproducciones de piezas musicales tienen Instrumentalness y Acousticness en un rango definido")
    print("3- Consultar cuantas piezas no repetidas tienen Speechness y Liveness en un rango definido")
    print("4- Consultar cuantas piezas no repetidas tienen Valence y Tempo en un rango definido")
    print("5- Consultar cuantas piezas no repetidas se tienen de un genero y cuantos artistas se tienen en el genero")    
    print("0- Salir")

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
        print('Eventos cargados: ' + str(controller.songSize(catalog)))
        print('Total de artistas unicos cargados: ' + str(controller.artistsSize(catalog)))
        print('Total de pistas de audio unicas cargadas: ' + str(controller.pistasSize(catalog)))
        

    elif int(inputs[0]) == 2:
        caracteristica = input("Ingrese la primera caracteristica a buscar: ")
        minimo = input("Ingrese el valor minimo de la primera caracteristica: ")
        maximo = input("Ingrese el valor maximo de la primera caracteristica: ")
        caracteristica_2 = input("Ingrese la segunda caracteristica a buscar: ")
        minimo_2 = input("Ingrese el valor minimo de la segunda caracteristica: ")
        maximo_2 = input("Ingrese el valor maximo de la segunda caracteristica: ")
        caracteristicas = controller.getCaracteristicas(catalog, caracteristica, minimo, maximo, caracteristica_2, minimo_2, maximo_2)
        printCaracteristicas(caracteristicas)
    elif int(inputs[0]) == 3:
        minimo = input("Ingrese el valor minimo de Liveness: ")
        maximo = input("Ingrese el valor maximo de Liveness: ")
        minimo_2 = input("Ingrese el valor minimo de Speechness: ")
        maximo_2 = input("Ingrese el valor maximo de Speechness: ")
        festejar = controller.getKaraoke(catalog,minimo, maximo, minimo_2, maximo_2)
        printFestejar(festejar)
    elif int(inputs[0]) == 4:
        minimo = input("Ingrese el valor minimo de Valence: ")
        maximo = input("Ingrese el valor maximo de Valence: ")
        minimo_2 = input("Ingrese el valor minimo de Tempo: ")
        maximo_2 = input("Ingrese el valor maximo de Tempo: ")
        ruptura = controller.getRuptura(catalog,minimo, maximo, minimo_2, maximo_2)
        printRuptura(ruptura)
    elif int(inputs[0]) == 5:
        genero = input("Ingrese el nombre del genero musical a buscar: ")
        minimo = input("Ingrese el valor minimo de Valence: ")
        maximo = input("Ingrese el valor maximo de Valence: ")
        generos_m = controller.getGeneros(catalog,genero, minimo, maximo)
        printRuptura(generos_m)
    else:
        sys.exit(0)
sys.exit(0)
