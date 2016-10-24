''' This file is used where ***clarification needed*** ''' 

import geojson

def to_geo_obj(geo_json):
    ''' Takes data and turns it into a geoJSON object. '''
    return geojson.loads(geo_json)

def make_other_attributes_properties(ip): # ***clarification needed*** this is a horrible function name lol
    ''' Returns a geojson feature object with properties that refer to the interest point database fields.'''
    feature = to_geo_obj(ip.geojson_object)
    feature.properties = {"name":ip.title,"db_id":ip.id,"layer":ip.layer,"style":ip.style}
    return feature
