def haversine(city):
    """
    Return distance in miles between house and city.
    
    Parameters
    city-- tuple, coordinates(lon,lat) for a city
    
    """
    dists = []
    for i in range(0,len(data['long'])):
        lon1, lat1, lon2, lat2 = map(radians, 
                                     [data['long'][i],
                                      data['lat'][i],
                                      city[0], city[1]])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = (sin(dlat/2)**2 + cos(lat1) 
             * cos(lat2) * sin(dlon/2)**2)
        c = 2 * asin(sqrt(a)) 
        r = 3956 # Radius of earth in miles. 
        dists.append(round(c*r,2))
    return np.array(dists)