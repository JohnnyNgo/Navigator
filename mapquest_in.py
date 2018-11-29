#module that interacts with Open MapQuest APIs.
#ex. building URLs, making HTTP requests, and parsing JSON responses

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'LwLRGOV5zsoZJxWitAvvPsXde3FNrjEy'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'

def build_search_url(locations: list) -> str:
    '''turns input of the locations into a url'''
    query_parameters = [
        ('key', MAPQUEST_API_KEY),
        ('from', locations[0])
        ]

    for l in locations[1:]:
        query_parameters.extend([('to',l)])
    
    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)

def build_search_url_2(latlng:str,unit:str) -> str:
    '''builds a search url for elevation using parameters above'''
    query_parameters = [
        ('key', MAPQUEST_API_KEY),
        ('unit', unit),
        ('latLngCollection', latlng)
        ]

    return BASE_ELEVATION_URL + '/profile?' + urllib.parse.urlencode(query_parameters)
    

def get_results(url:str) -> dict:
    '''takes a url and returns json parsed response as a dctionary'''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
