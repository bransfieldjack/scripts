import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient
import psycopg2
import json


"""
Converts data_type_id in mongo dataportal_prod_meta/datasets collection from integer to string: {1:"microarray", 2:"RNAseq"}
"""

def main():

    MONGO_URI='mongodb://localhost:27017'
   
    myclient = pymongo.MongoClient(MONGO_URI) 
    database = myclient["dataportal_prod_meta"]
    collection = database["datasets"]
    # mongo_cursor = collection.find({})

    connection = psycopg2.connect(user = "portaladmin",
                                  host = "localhost",
                                  port = "5432",
                                  database = "dataportal")
    cursor = connection.cursor()

    dataset_ids = cursor.execute("select distinct(dataset_id) from samples;")
    dataset_ids_row = cursor.fetchall() 
    
    sample_types = cursor.execute("select distinct(sample_type) from samples where dataset_id=1000;")
    sample_types_row = cursor.fetchall() 

    flat_dataset_ids = [i[0] for i in dataset_ids_row]
    
    test = []
    values = []
    for item in flat_dataset_ids:

        sample_types = cursor.execute("select distinct(sample_type) from samples where dataset_id={}".format(item))
        sample_types_row = cursor.fetchall() 
        flat_sample_types = [i[0] for i in sample_types_row]

        value_dict = {
            "dataset_id": item,
            "sample_types": flat_sample_types
        }

        values.append(value_dict)

        res = collection.find({'dataset_id': item})
        for i in res:
            
            object_id = i['_id']
            collection.update({'_id':object_id}, {"$set": {'sample_types': value_dict}}, upsert=False) # or use update one, update deprecated 


if __name__ == "__main__":
    main()
