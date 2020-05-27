import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Converts data_type_id in mongo dataportal_prod_meta/datasets collection from integer to string: {1:"microarray", 2:"RNAseq"}
"""

def main():

    MONGO_URI='mongodb://localhost:27017'
   
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["dataportal_prod_meta"]
    collection = database["datasets"]
    cursor = collection.find({})

    data_types_list = []
    for datatypes in cursor:

        dataset_id = datatypes["dataset_id"]
        data_type = datatypes["datasets"][0]["data_type_id"]
        _dict = {
            "dataset_id": dataset_id,
            "data_type": data_type
        }
        data_types_list.append(_dict)

    database = myclient["dataportal_prod_meta"]
    collection = database["datasets_datatypes"]
    collection.insert_many(data_types_list)

    print("Operation complete")
   
if __name__ == "__main__":
    main()

    