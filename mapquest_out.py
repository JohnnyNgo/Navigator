#module that implements the various outputs

import mapquest_in

class STEPS:

    def get_directions(self, url:dict) -> str:
        directions = ''
        for routes in url['route']['legs']:
            '''iterates each route'''
            for maneuvers in routes['maneuvers']:
                '''finds each narrative'''
                directions += maneuvers['narrative'] + '\n'
        return directions[:-1]
    
    def get_results(self, url:dict) -> str:
        directions = self.get_directions(url)
        return ('DIRECTIONS\n' + directions)

class TOTALDISTANCE:

    def get_distance(self, url:dict) -> float:
        return url['route']['distance']

    def get_results(self, url:dict) -> str:
        distance = round(self.get_distance(url))
        return ('TOTAL DISTANCE: ' + str(distance) + ' miles')

class TOTALTIME:

    def get_time(self, url:dict) -> float:
        return url['route']['time']

    def get_results(self, url:dict) -> str:
        minutes = round(self.get_time(url)/60)
        return ('TOTAL TIME: ' + str(minutes) + ' minutes')

class LATLONG:

    def get_latlng(self, url:dict) -> str:
        '''formats lat/longs and returns the formatted string'''
        latlng = ''
        for locations in url['route']['locations']:
            lat = locations['displayLatLng']['lat']
            lng = locations['displayLatLng']['lng']
            lat_display = str(abs(round(lat,2)))
            lng_display = str(abs(round(lng,2)))
            if lat < 0:
                latlng += lat_display + 'S '
            else:
                latlng += lat_display + 'N '
            if lng < 0:
                latlng += lng_display + 'W\n'
            else:
                latlng += lng_display + 'E\n'
        return latlng[:-1]

    def get_display(self, url:dict) -> str:
        '''finds all latitudes/longitudes and returns it as a list'''
        latlng = []
        for locations in url['route']['locations']:
            lat = str(locations['displayLatLng']['lat'])
            lng = str(locations['displayLatLng']['lng'])
            latlng.append(lat)
            latlng.append(lng)
        return latlng

    def get_results(self, url:dict) -> str:
        latlng = self.get_latlng(url)
        return ('LATLONGS\n' + latlng)

class ELEVATION:

    def get_results(self, url:dict) -> str:
        latlng = LATLONG()
        coordinates = latlng.get_display(url)
        results = []
        elevations = ''
        for i in range(0,len(coordinates),2):
            '''for each pair of coords, build into url and append to for loop'''
            coords = coordinates[i] + ', ' + coordinates[i+1]
            results.append(mapquest_in.get_results(mapquest_in.build_search_url_2(coords,'f')))
        for urls in results:
            '''for each url, find elevation and add it to string'''
            elevations += str(round(urls['elevationProfile'][0]['height'])) + '\n'
        return ('ELEVATIONS\n' + elevations[:-1])

