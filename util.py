
import pickle
import json
import numpy as np

__locality_name = None
__data_columns = None
__model = None

def get_estimated_price(locality_name,sqft,bhk):
    try:
        loc_index = __data_columns.index(locality_name.lower())
    except:
        loc_index = -1

    x = np.zeros(643)
    x[0] = sqft
    x[1] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)
    #return round(__model.predict(([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locality_name

    with open("column.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locality_name = __data_columns[2:]  # first 2 columns are sqft, bhk

    global __model
    if __model is None:
        with open('maharashtra_region_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    
def get_location_names():
    return __locality_name

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Moshi',900, 3))
    print(get_estimated_price('Hadapsar',900,3))
    print(get_estimated_price('Talegaon', 600,2)) # other location
    #print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location