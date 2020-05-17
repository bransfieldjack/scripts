import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient
import json


"""
Creates a color file for mongo. 
"""

def main():

    MONGO_URI='mongodb://localhost:27017'

    with open('data/imac_atlas_colours_v7.1.tsv') as json_file:
        data = json.load(json_file)
        myclient = pymongo.MongoClient(MONGO_URI) 
        database = myclient["imac_v1"]
        collection = database["colors"]
        result = collection.insert_one(data)
        print("Operation complete")

if __name__ == "__main__":
    main()


