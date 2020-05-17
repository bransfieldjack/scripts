import numpy as np
import pandas as pd
import functools 
import csv
import pymongo
from pymongo import MongoClient


"""
Converts the existing atlas imac expression data to a mongo collection.
"""

def main():

    MONGO_URI='mongodb://localhost:27017'

    expression_df = pd.read_csv('data/blood_atlas_expression_v7.1.tsv', sep='\t', index_col=0)
    expression_df.reset_index(level=0, inplace=True)
    temp = expression_df
    final_temp = temp.to_dict('records')
    myclient = pymongo.MongoClient(MONGO_URI) # Mongon container name is 'mongo'. # local mongodb server.   # Connects to the mongodb daabase and returns everything.
    database = myclient["imac_v1"]
    collection = database["expression"]
    result = collection.insert(final_temp)

if __name__ == "__main__":
    main()


