"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    loadCategories(catalog)
    loadSongs(catalog)

def loadSongs(catalog):
    """
    Carga los canciones del archivo. 
    """
    songfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(songfile, encoding='utf-8'))
    for song in input_file:
        model.addVideo(catalog, song)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def songSize(catalog):
    """
    Número de canciones en el catalogo
    """
    return model.songSize(catalog)

def artistsSize(catalog):
    return model.artistsSize(catalog)
def pistaSize(catalog):
    return model.pistaSize(catalog)

def getCaracteristicas(catalog, caracteristica, minimo, maximo, caracteristica_2, minimo_2, maximo_2)
    return model.getCaracteristicas(catalog, caracteristica, minimo, maximo, caracteristica_2, minimo_2, maximo_2)
def getKaraoke(catalog,minimo, maximo, minimo_2, maximo_2)
 return model.getKaraoke(catalog,minimo, maximo, minimo_2, maximo_2)
def getRuptura(catalog,minimo, maximo, minimo_2, maximo_2)
    return model.getRuptura(catalog,minimo, maximo, minimo_2, maximo_2)
def getGeneros(catalog,genero, minimo, maximo)
    return model.getGeneros(catalog,genero, minimo, maximo)