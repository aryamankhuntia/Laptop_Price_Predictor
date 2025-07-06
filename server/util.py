import json
import pickle
import numpy as np
import os

__brands = None
__cpus = None
__data_columns = None
__model = None

def get_estimated_price(brand,cpu,screen_size,disk_size,ram,rating=3):
    try:
        brand_index = __data_columns.index(brand.lower())
    except:
        brand_index = -1

    try:
        cpu_index = __data_columns.index(cpu.lower())
    except:
        cpu_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = screen_size
    x[1] = rating
    x[2] = ram
    x[3] = disk_size
    if brand_index >= 0:
        x[brand_index] = 1
    if cpu_index >= 0:
        x[cpu_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("Loading saved artifacts....")
    global __data_columns
    global __brands
    global __cpus
    global __model

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __brands = __data_columns[4:20]
        __cpus = __data_columns[20:]

    if __model is None:
        with open('./artifacts/laptop_price_model.pickle','rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_brands():
    return __brands

def get_cpus():
    return __cpus

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()