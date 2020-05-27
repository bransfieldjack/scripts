import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Generates a list of all the datasets Xinyi requires. 
"""

def main():

    MONGO_URI='mongodb://localhost:27017'
   
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["dataportal_prod_meta"]
    collection = database["datasets_datatypes"]
    cursor = collection.find({})

    ds_list = []
    for doc in cursor:
        ds_id = doc['dataset_id']
        data_type = doc['data_type']

        _dict = {
            'dataset_id': ds_id,
            'data_type': data_type
        }

        ds_list.append(_dict)

    result_list = []
    _list = [7224, 7267, 6655, 7311, 7127, 7291, 5019, 6637, 6658, 6659, 6756, 6291, 6300, 6988, 6080, 6106, 6108, 6146, 7269, 6264, 6310, 6831, 6455, 6501, 6593, 7131]
    for item in ds_list:
        
        if item['dataset_id'] in _list:
            # print(item['dataset_id'])
            _value_dict = {
                'dataset_id': item['dataset_id'],
                'data_type': item['data_type']
            }
            result_list.append(_value_dict)
    print(result_list)
            
    print("Operation complete.")

if __name__ == "__main__":
    main()


