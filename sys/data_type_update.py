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

    for document in cursor:

        object_id = document['_id']
        dataset_id = document['dataset_id']
        data_type = document['datasets'][0]['data_type_id']

        # print(data_type)
   
        if data_type == 1:
            
            myquery = { "_id": object_id }
            newvalues = { "$set": { "datasets.0.data_type_id": "microarray"} } 
            collection.update_one(myquery, newvalues)
            
        if data_type == 2:
    
            myquery = { "_id": object_id }
            newvalues = { "$set": { "datasets.0.data_type_id": "RNAseq"} } 
            collection.update_one(myquery, newvalues)
            
    print("Operation complete.")

if __name__ == "__main__":
    main()