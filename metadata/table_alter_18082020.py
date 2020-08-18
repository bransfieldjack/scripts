import numpy as np
import pandas as pd
import functools 
import csv
import json
import pymongo
from pymongo import MongoClient


"""
Merging nested dictionaries (datasets, dataset_metadata)

Keep: 

 - dataset_id
 - title
 - authors
 - description
 - platform
 - number_of_samples
 - private

Modify:

 - pubmed => pubmed_id
 - handle => name

"""


def main():

    MONGO_URI='mongodb://localhost:27017'
    myclient = pymongo.MongoClient(MONGO_URI) 
    database = myclient["dataportal_prod_meta"]
    collection = database["datasets"]
    cursor = collection.find()

    dict_list = []
    for item in cursor:
        obj = {
            "dataset_id": int(item["dataset_id"]),
            "title": item["dataset_metadata"][0]["title"],
            "authors": item["dataset_metadata"][0]["authors"],
            "description": item["dataset_metadata"][0]["description"],
            "platform": item["dataset_metadata"][0]["platform"],
            "number_of_samples": item["datasets"][0]["number_of_samples"],
            "private": item["datasets"][0]["private"],
            "pubmed_id": item["dataset_metadata"][0]["pubmed"],
            "annotator": item["annotator"],
            "can_annotate": item["can_annotate"],
            "name": item["datasets"][0]["handle"],
        }
        dict_list.append(obj)
        

    sample = dict_list[3]
    store = []

    

    for item in dict_list:
       
        keylist = []
        vallist = []

        for k, v in item.items():

            newkey = str(k).replace("{","").replace("}", "").replace('"', "")
            newval = str(v).replace("{","").replace("}", "").replace('"', "")

            keylist.append(newkey)
            vallist.append(newval)

        fin = dict(zip(keylist, vallist))
        store.append(fin)

    # print(store)
    for item in store:

        myclient = pymongo.MongoClient(MONGO_URI) 
        database = myclient["dataportal_prod_meta"]
        collection = database["datasets_reformat"]
        result = collection.insert(item)

    print("Operation complete")
  
    
if __name__ == "__main__":
    main()