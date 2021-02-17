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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los nombres de los canales,
    una lista vacia para los ids de los videos y una lista vacia para la asociación
    categoría y videos. Retorna el catalogo inicializado.
    """
    catalog = {'n_videos': None,
               'channel': None,
               'video_id': None,
               'category_id': None}

    catalog['n_videos'] = lt.newList()
    catalog['channel'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=comparechannels)
    catalog['video_id'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=compareids)
    catalog['category_id'] = lt.newList('SINGLE_LINKED')

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['n_videos'], video)
    channels = video['channel'].split(",")
    for channel in channels:
        addChannel(catalog, channel.strip(), video)

def addChannel(catalog, channel_name, video):

    channels = catalog['channel']
    poschannel = lt.isPresent(channels, channel_name)

    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)

    else:
        channel = newChannel
        lt.addLast(channels)
    
    lt.addLast(channel['videos'], video)

def addId(catalog, id):
 
    t = newId(id['tag_name'], id['tag_id'])
    lt.addLast(catalog['category_id'], t)


def addVideoID(catalog, videoi_d):
    """
    Adiciona un tag a la lista de tags
    """
    t = newVidId(videoi_d['tag_id'], videoi_d['videos_id'])
    lt.addLast(catalog['video_ids'], t)

# Funciones para creacion de datos

def newChannel(channel):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    channel_name = {'channel': "", "videos": None,  "views": 0}
    channel_name['channel'] = channel
    channel_name['videos'] = lt.newList('ARRAY_LIST')
    return channel_name

def newId(name, id):

    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newVidId(id, video_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    videoid = {'id': id, 'book_id': video_id}
    return videoid


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparechannels(channelname1, channel):
    if (channelname1.lower() in channel['name'].lower()):
        return 0
    return -1

def compareids(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento