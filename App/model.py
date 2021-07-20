﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    catalog = {'canciones': None,
                'categories': None
                }

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    return catalog


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def cancioesSize(catalog):
    """
    Número de canciones en el catalogo
    """
    return lt.size(catalog['canciones'])

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def getCaracteristicas(catalog, caracteristica, minimo, maximo, caracteristica_2, minimo_2, maximo_2):
    pass
def getKaraoke(catalog,minimo, maximo, minimo_2, maximo_2):
    pass
def getRuptura(catalog,minimo, maximo, minimo_2, maximo_2):
    pass
def getGeneros(catalog,genero, minimo, maximo):
    pass