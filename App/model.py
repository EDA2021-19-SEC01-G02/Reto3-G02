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


from DISClib.ADT.indexminpq import size
from math import ldexp
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import random
assert cf


# Construccion de modelos

def newCatalog():
    catalog = {'events': None,
                'artists': None,
                'tracks': None,
                'caracteristicas': None,
                'generos': None}

    caracteristicas = {'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'mode': None,
                'key': None,}

    caracteristicas["instrumentalness"] =  om.newMap(omaptype='RBT')
    caracteristicas["liveness"] =  om.newMap(omaptype='RBT')
    caracteristicas["speechiness"] =  om.newMap(omaptype='RBT')
    caracteristicas["danceability"] =  om.newMap(omaptype='RBT')
    caracteristicas["valence"] =  om.newMap(omaptype='RBT')
    caracteristicas["tempo"] =  om.newMap(omaptype='RBT')
    caracteristicas["acousticness"] =  om.newMap(omaptype='RBT')
    caracteristicas["mode"] =  om.newMap(omaptype='RBT')
    caracteristicas["key"] =  om.newMap(omaptype='RBT')

    catalog['events'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    catalog['artists'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    catalog['tracks'] = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    catalog['generos'] = mp.newMap(100, maptype='PROBING', loadfactor=0.5)
    catalog["caracteristicas"] = caracteristicas

    return catalog


# Funciones para agregar informacion al catalogo
def loadEvent(catalog, event):
    mp.put(catalog['artists'], event['artist_id'], event)
    mp.put(catalog['tracks'], event['track_id'], event)
    mp.put(catalog['events'], event['id'], event)


# Funciones para creacion de datos
def loadCaracteristica(map, event, caracteristica):
    llave = float(event[caracteristica])
    if om.contains(map, llave):
        valor =  me.getValue(om.get(map, llave))
        lt.addLast(valor, event['id'])
    else:
        valor = lt.newList('ARRAY_LIST')
        lt.addLast(valor, event['id'])
        om.put(map, llave, valor)


def loadCaracteristicas(catalog, event):
    loadCaracteristica(catalog["caracteristicas"]['instrumentalness'], event, "instrumentalness")
    loadCaracteristica(catalog["caracteristicas"]['liveness'], event, "liveness")
    loadCaracteristica(catalog["caracteristicas"]['speechiness'], event, "speechiness")
    loadCaracteristica(catalog["caracteristicas"]['danceability'], event, "danceability")
    loadCaracteristica(catalog["caracteristicas"]['valence'], event, "valence")
    loadCaracteristica(catalog["caracteristicas"]['tempo'], event, "tempo")
    loadCaracteristica(catalog["caracteristicas"]['acousticness'], event, "acousticness")
    loadCaracteristica(catalog["caracteristicas"]['mode'], event, "mode")
    loadCaracteristica(catalog["caracteristicas"]['key'], event, "key")


# Funciones de consulta
def eventSize(catalog):
    return mp.size(catalog['events'])


def artistSize(catalog):
    return mp.size(catalog['artists'])


def trackSize(catalog):
    return mp.size(catalog['tracks'])


def getCaracteristicas(catalog, c1, min1, max1, c2, min2, max2):
    try:
        lista1 = om.values(catalog['caracteristicas'][c1.lower().strip()], min1, max1)
        lista2 = om.values(catalog['caracteristicas'][c2.lower().strip()], min2, max2)
    except:
        print('Verifique el nombre de las características')
        return None

    mapAux = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    listaFinal = lt.newList('ARRAY_LIST')

    repro, art = 0, 0

    for i in range(1, lt.size(lista1)+1):
        ilist = lt.getElement(lista1, i)
        for j in range(1, lt.size(ilist)+1):
            id = lt.getElement(ilist, j)
            mp.put(mapAux, id, id)
    
    for i in range(1, lt.size(lista2)+1): 
        ilist = lt.getElement(lista2, i)
        for j in range(1, lt.size(ilist)+1):
            id = lt.getElement(ilist, j)
            if mp.contains(mapAux, id):
                lt.addLast(listaFinal, id)
    
    if lt.size(listaFinal) != 0:
        mapTracks = getUniqueTracks(catalog, listaFinal)
        mapArtists = getUniqueArtists(catalog, listaFinal)
        
        repro = mp.size(mapTracks)
        art = mp.size(mapArtists)
    
    return repro, art, mapTracks


def getKaraoke(catalog, min1, max1, min2, max2):
    repro, art, map = getCaracteristicas(catalog, 'liveness', min1, max1, 'speechiness', min2, max2)
    eightTracks = lt.newList('ARRAY_LIST')
    tracks = mp.valueSet(map)
    if lt.size(tracks) >= 8:
        num = 0
        listNum = lt.newList('ARRAY_LIST')
        while num < 8:
            n = random.randint(1, lt.size(tracks))
            if lt.isPresent(listNum, n) == 0:
                lt.addLast(eightTracks, lt.getElement(tracks, n))
                lt.addLast(listNum, n)
                num += 1

    return repro, eightTracks


def getBroken(catalog, min1, max1, min2, max2):
    repro, art, map = getCaracteristicas(catalog, 'valence', min1, max1, 'tempo', min2, max2)
    eightTracks = lt.newList('ARRAY_LIST')
    tracks = mp.valueSet(map)
    if lt.size(tracks) >= 8:
        num = 0
        listNum = lt.newList('ARRAY_LIST')
        while num < 8:
            n = random.randint(1, lt.size(tracks))
            if lt.isPresent(listNum, n) == 0:
                lt.addLast(eightTracks, lt.getElement(tracks, n))
                lt.addLast(listNum, n)
                num += 1
    
    return repro, eightTracks


def getGeneros(catalog, names):
    listaNames = lt.newList('ARRAY_LIST')
    listaGen = lt.newList('ARRAY_LIST')
    
    names = names.split(',')
    for name in names:
        lt.addLast(listaNames, name.lower().strip())
    
    for i in range(1, lt.size(listaNames)+1):
        nam = lt.getElement(listaNames, i)
        gen = me.getValue(mp.get(catalog['generos'], nam))
        lt.addLast(listaGen, gen)
    
    return listaGen


def crearGenero(catalog, name, min, max):
    genero = {'name': None,
            'events': None,
            'artists': None}
    
    events = lt.newList('ARRAY_LIST')

    listEvents = om.values(catalog['caracteristicas']['tempo'], min, max)
    for i in range(1, lt.size(listEvents)+1): 
        ilist = lt.getElement(listEvents, i)
        for j in range(1, lt.size(ilist)+1):
            id = lt.getElement(ilist, j)
            lt.addLast(events, id)
    
    artists = getUniqueArtists(catalog, events)

    genero['name'] = name.lower().strip()
    genero['events'] = events
    genero['artists'] = mp.valueSet(artists)

    mp.put(catalog['generos'], genero['name'], genero)

    return genero


def crearGenerosIniciales(catalog):
    crearGenero(catalog, 'reggae', 60, 90)
    crearGenero(catalog, 'down-tempo', 70, 100)
    crearGenero(catalog, 'chill-out', 90, 120)
    crearGenero(catalog, 'hip-hop', 85, 115)
    crearGenero(catalog, 'jazz and funk', 120, 125)
    crearGenero(catalog, 'pop', 100, 130)
    crearGenero(catalog, 'r&b', 60, 80)
    crearGenero(catalog, 'rock', 110, 140)
    crearGenero(catalog, 'metal', 100, 160)


# Funciones auxiliares
def getUniqueArtists(catalog, idEvents):
    map = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    for i in range(1, lt.size(idEvents)+1):
        id = lt.getElement(idEvents, i)
        event = me.getValue(mp.get(catalog['events'], id))
        artist_id = event['artist_id']
        mp.put(map, artist_id, artist_id)
    return map


def getUniqueTracks(catalog, idEvents):
    map = mp.newMap(90000, maptype='PROBING', loadfactor=0.5)
    for i in range(1, lt.size(idEvents)+1):
        id = lt.getElement(idEvents, i)
        event = me.getValue(mp.get(catalog['events'], id))
        track_id = event['track_id']
        mp.put(map, track_id, event)
    return map