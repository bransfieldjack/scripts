import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Create a new field in a mongo collection. 
"""

def main():

    MONGO_URI='mongodb://localhost:27017'
   
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["dataportal_prod_meta"]
    collection = database["datasets"]
    cursor = collection.find({})

    data_types_list = []
    for item in cursor:

        object_id = item['_id']
        # item.insert({"annotator":""})
        collection.update({'_id':object_id}, {"$set": {"can_annotate": False}}, upsert=False) # or use update one, update deprecated 

    print("Operation complete")
   
if __name__ == "__main__":
    main()


