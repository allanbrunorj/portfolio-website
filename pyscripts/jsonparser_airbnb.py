from geopy.geocoders import Nominatim
from joblib import load
import os
from sklearn.ensemble import ExtraTreesRegressor
import numpy as np
# MODULE TO GET JSON FROM THE WEB, CHECK MISSING OR WRONG VALUES, ENCODE AND RETURN AN NP.ARRAY TO THE MODULE
# address - OK
# amenities - OK
# accommodates - OK
# bedrooms
# bathrooms
# property


def check_conditions(json_file):
    coords = get_coordinates(json_file['address'])
    if not coords:
        return False, ''
    if not json_file['amenities'].isdigit():
        return False, ''
    elif not json_file['accommodates'].isdigit():
        return False, ''
    elif not json_file['bedrooms'].isdigit():
        return False, ''
    elif not json_file['beds'].isdigit():
        return False, ''
    elif not json_file['bathrooms'].isdigit():
        return False, ''
    else:
        return True, coords

def get_coordinates(address):
    geolocator = Nominatim(user_agent='allanportfolio') 
    location = geolocator.geocode(address)
    try:
        return location.latitude, location.longitude
    except:
        return False

#ORDEM: LATITUDE, LONGITUDE 

def get_prediction(data, coords): 
    data['latitude'] = coords[0]
    data['longitude'] = coords[1]   
    encode_list = {'Apartment': 0,
     'Bed and breakfast': 1,
      'Condominium': 2,
       'Guest suite': 3,
        'Guesthouse': 4,
         'Hostel': 5, 'House': 6,
          'Loft': 7, 'Other': 8,
           'Serviced apartment': 9,
            'Townhouse': 10,
             'Villa': 11
                }
    data['property_type'] = encode_list[data['property_type']]
    for num_column in ['accommodates', 'bathrooms', 'bedrooms', 'beds', 'month', 'amenities']:
        data[num_column] = int(data[num_column])
    order = ['latitude', 'longitude', 'property_type', 'accommodates', 'bathrooms',
       'bedrooms', 'beds', 'month', 'amenities']
    input_array = [data[x] for x in order]
    input_array = np.array(input_array).reshape(1, -1)
    path = os.path.join(os.getcwd(), 'model','final_model.pkl')
    with open(path) as mod:
        model = load(path, mmap_mode='r')
        prediction = model.predict(input_array)
    return prediction



    #DATA É O DICIONARIO AINDA CONTENDO ADDRESS
    # COORDS É UMA TUPLE COM LATITUDE AND LO'NGITUDE
