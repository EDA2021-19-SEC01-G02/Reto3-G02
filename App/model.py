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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from math import ldexp
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
    catalog = {'events': None,
                'artists': None,
                'tracks': None,
                'listTracks': None}

    catalog['events'] = lt.newList('ARRAY_LIST')
    catalog['listTracks'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    catalog['tracks'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    catalog['ids'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    artist = {'id': None,
            'events': None}
    
    id = event['artist_id']
    artist['id'] = id
    artist['events'] = lt.newList('ARRAY_LIST')
    mp.put(catalog['artists'], id, artist)

    
    caracteristicas = {'Instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'mode': None,
                'key': None,}
    caracteristicas["Instrumentalness"] =  om.newMap(omaptype='RBT')
    caracteristicas["liveness"] =  om.newMap(omaptype='RBT')
    caracteristicas["speechness"] =  om.newMap(omaptype='RBT')
    caracteristicas["danceability"] =  om.newMap(omaptype='RBT')
    caracteristicas["valence"] =  om.newMap(omaptype='RBT')
    caracteristicas["tempo"] =  om.newMap(omaptype='RBT')
    caracteristicas["acousticness"] =  om.newMap(omaptype='RBT')
    caracteristicas["mode"] =  om.newMap(omaptype='RBT')
    caracteristicas["key"] =  om.newMap(omaptype='RBT')
    catalog["caracteristicas"]= caracteristicas

    return catalog


# Funciones para agregar informacion al catalogo
def loadEvent(catalog, event):
    if mp.contains(catalog['artists'], event['artist_id'].strip()):
        artist = me.getValue(mp.get(catalog['artists'], event['artist_id'].strip()))
        lt.addLast(artist['events'], event)
    else:
        newArtist(catalog, event)
        artist = me.getValue(mp.get(catalog['artists'], event['artist_id'].strip()))
        lt.addLast(artist['events'], event)

    if not mp.contains(catalog['tracks'], event['track_id'].strip()):
        newTrack(catalog, event)
        lt.addLast(catalog['listTracks'], event)

    lt.addLast(catalog['events'], event)
"""""
def loadSentiment(catalog, sentiment):
    newSentiment(catalog, sentiment)
"""""
# Funciones para creacion de datos
"""""
def newSentiment(catalog, sentiment):
    sentiment_value = {"hashtag":None}

    hashtag = sentiment["hashtag"]
    sentiment_value["hashtag"] = hashtag
    mp.put(catalog["sentiments"], hashtag, sentiment)
"""""   
def addID(catalog, event):
    cat = newID(catalog, event)
    mp.put(catalog['ids'], cat["track"], cat["evento"])


def newID(catalog, event):
    """
    Esta estructura almacena los tags utilizados para marcar libros.
    """
    dicc = {'track': None,
            'evento': None}

    dicc['track'] = event['track_id']
    dicc['evento'] = event

    return dicc


def loadCaracteristica(caracteristica_omap, event, caracteristica_s):
    llave = event[caracteristica_s]
    if om.contains(caracteristica_omap, llave):
        valor =  me.getValue(om.get(caracteristica_omap,llave))
        lt.addLast(valor, event['track_id'])
    else:
        valor = lt.newList('ARRAY_LIST')
        om.put(caracteristica_omap, llave, valor,)
        lt.addLast(valor, event['track_id'])

def loadCaracteristicas(catalog, event):
    loadCaracteristica(catalog["carateristicas"]['Instrumentalness'], event,"instrumentalness")
    loadCaracteristica(catalog["carateristicas"]['Instrumentalness'], event,"instrumentalness")

    mapa con track id y el evento

def newTree(catalog, event ):
    tree = {'value': None}

    value = event['Instrumentalness']
    tree['id'] = value
    mp.put(catalog['caracteristicas'], value, tree)



def newTrack(catalog, event):
    track = {'id': None}

    id = event['track_id']
    track['id'] = id
    mp.put(catalog['tracks'], id, track)


def newArtist(catalog, event):
    artist = {'id': None,
            'events': None}
    
    id = event['artist_id']
    artist['id'] = id
    artist['events'] = lt.newList('ARRAY_LIST')
    mp.put(catalog['artists'], id, artist)


# Funciones de consulta
def eventSize(catalog):
    return mp.size(catalog['events'])

def artistSize(catalog):
    return mp.size(catalog['artists'])

def trackSize(catalog):
    return lt.size(catalog['listTracks'])

def getCaracteristicas(catalog, caracteristica, caracteristicas, minimo, maximo, caracteristica_2, minimo_2, maximo_2):
    lista = lt.newList('ARRAY_LIST')
    if caracteristica.lower().strip() in caracteristicas:
        if om.isEmpty(caracteristicas[caracteristica]) == False:
            if caracteristica['caracteris']> minimo and caracteristica['caracteris']<maximo:
                lt.addLast(lista, cancion["id"])
            


def getKaraoke(catalog,minimo, maximo, minimo_2, maximo_2):
    pass

def getRuptura(catalog,minimo, maximo, minimo_2, maximo_2):
    pass

def getGeneros(catalog,genero, minimo, maximo):
    pass

# Funciones de comparación
def compareDates(song1,song2):
    pass

# Funciones de ordenamiento
